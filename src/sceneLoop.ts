/** Schedule decorative frames only while the scene can actually be seen. */
export function createSceneLoop({
  render,
  isActive,
  requestFrame = requestAnimationFrame,
  cancelFrame = cancelAnimationFrame,
  interval = 1000 / 30,
}: {
  render: (time: number) => void;
  isActive: () => boolean;
  requestFrame?: typeof requestAnimationFrame;
  cancelFrame?: typeof cancelAnimationFrame;
  interval?: number;
}) {
  let frame: number | null = null;
  let previous: number | null = null;

  function tick(time: number) {
    frame = null;
    if (!isActive()) return;
    if (previous === null || time - previous >= interval - .5) {
      previous = time;
      render(time);
    }
    frame = requestFrame(tick);
  }

  return {
    start() {
      if (frame !== null || !isActive()) return;
      previous = null;
      frame = requestFrame(tick);
    },
    stop() {
      if (frame !== null) cancelFrame(frame);
      frame = null;
      previous = null;
    },
  };
}
