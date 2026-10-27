import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(
  new URL("../src/sceneLoop.ts", import.meta.url),
  "utf8",
);
const compiled = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext },
}).outputText;
const { createSceneLoop } = await import(
  `data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`
);

function harness(initiallyActive = true) {
  let active = initiallyActive;
  let id = 0;
  const pending = new Map();
  const renders = [];
  const loop = createSceneLoop({
    isActive: () => active,
    render: (time) => renders.push(time),
    requestFrame: (callback) => {
      pending.set(++id, callback);
      return id;
    },
    cancelFrame: (frame) => pending.delete(frame),
  });
  return {
    loop,
    pending,
    renders,
    setActive: (value) => {
      active = value;
    },
    tick(time) {
      const queued = [...pending.values()];
      pending.clear();
      for (const callback of queued) callback(time);
    },
  };
}

test("off-screen, paused, and hidden scenes schedule no animation work", () => {
  const h = harness(false);
  h.loop.start();
  assert.equal(h.pending.size, 0);
  assert.deepEqual(h.renders, []);
});

test("repeated start does not create duplicate loops and rendering stays at 30 fps", () => {
  const h = harness();
  h.loop.start();
  h.loop.start();
  assert.equal(h.pending.size, 1);
  for (const time of [0, 16.7, 33.4, 50.1, 66.8]) h.tick(time);
  assert.deepEqual(h.renders, [0, 33.4, 66.8]);
  assert.equal(h.pending.size, 1);
});

test("a scene becoming inactive before the next frame does not render or reschedule", () => {
  const h = harness();
  h.loop.start();
  h.setActive(false);
  h.tick(16);
  assert.deepEqual(h.renders, []);
  assert.equal(h.pending.size, 0);
});

test("cleanup cancels pending frames and re-entry starts a fresh loop", () => {
  const h = harness();
  h.loop.start();
  h.tick(100);
  h.loop.stop();
  assert.equal(h.pending.size, 0);
  h.setActive(false);
  h.loop.start();
  assert.equal(h.pending.size, 0);
  h.setActive(true);
  h.loop.start();
  h.tick(101);
  assert.deepEqual(h.renders, [100, 101]);
  h.loop.stop();
  h.loop.stop();
  assert.equal(h.pending.size, 0);
});
