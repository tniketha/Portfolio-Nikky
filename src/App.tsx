import { lazy, Suspense, useEffect, useState } from "react";
import { useReducedMotion, motion, useScroll } from "framer-motion";
import {
  ArrowUpRight,
  ArrowDown,
  ArrowUp,
  Github,
  Terminal,
  Sun,
  Moon,
  Menu,
  X,
  Pause,
  Play,
} from "lucide-react";
import {
  About,
  Work,
  Skills,
  Journey,
  Certificates,
  Contact,
  ProjectDetails,
} from "./Sections";
import { AmbientEffects, TerminalWindow } from "./Effects";
import type { Project } from "./data";
const Scene = lazy(() => import("./Scene"));
export default function App() {
  const systemReduced = useReducedMotion();
  const [paused, setPaused] = useState(false);
  const reduced = !!systemReduced || paused;
  const [theme, setTheme] = useState(() => {
    try {
      return localStorage.getItem("nikky-theme") === "blueprint"
        ? "blueprint"
        : "dark";
    } catch {
      return "dark";
    }
  });
  const [terminal, setTerminal] = useState(false);
  const [menu, setMenu] = useState(false);
  const [selected, setSelected] = useState<Project | null>(null);
  const { scrollYProgress } = useScroll();
  const toggleTheme = () =>
    setTheme((t) => (t === "dark" ? "blueprint" : "dark"));
  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    try {
      localStorage.setItem("nikky-theme", theme);
    } catch {
      /* Theme still works without storage. */
    }
  }, [theme]);
  useEffect(() => {
    document.documentElement.dataset.motion = reduced ? "reduced" : "full";
  }, [reduced]);
  useEffect(() => {
    const key = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setTerminal((t) => !t);
      }
      if (e.key === "Escape") setMenu(false);
    };
    window.addEventListener("keydown", key);
    return () => window.removeEventListener("keydown", key);
  }, []);
  return (
    <>
      <a href="#main" className="skip-link">
        Skip to content
      </a>
      <AmbientEffects reduced={reduced} />
      <motion.div
        className="reading-progress"
        style={{ scaleX: scrollYProgress }}
      />
      <header className="header">
        <a href="#home" className="brand" aria-label="Nikky home">
          <span className="brand-mark">
            N<span>↗</span>
          </span>
          NIKKY<span className="brand-dot">.</span>
        </a>
        <nav aria-label="Main navigation" className={menu ? "is-open" : ""}>
          {[
            ["about", "About"],
            ["work", "Work"],
            ["skills", "Skills"],
            ["journey", "Journey"],
            ["certificates", "Certificates"],
          ].map(([id, label]) => (
            <a key={id} href={`#${id}`} onClick={() => setMenu(false)}>
              {label}
            </a>
          ))}
        </nav>
        <div className="nav-right">
          <a href="#contact" className="nav-cta">
            Let’s talk <ArrowUpRight size={16} />
          </a>
          <button
            className="mobile-menu icon-button"
            onClick={() => setMenu((m) => !m)}
            aria-label={menu ? "Close navigation" : "Open navigation"}
            aria-expanded={menu}
          >
            {menu ? <X size={22} /> : <Menu size={22} />}
          </button>
        </div>
      </header>
      <main id="main">
        <section className="hero" id="home">
          <div className="hero-content">
            <p className="eyebrow">
              <span className="little-line" /> CURIOUS MIND. CREATIVE CODE.
            </p>
            <h1>
              CODE.
              <br />
              <span>CREATE.</span>
              <br />
              EVOLVE<span className="period">.</span>
            </h1>
            <div className="hero-intro">
              <p>
                I’m <strong>Niketha Thavaneswaran.</strong>
              </p>
              <p>
                Turning curiosity into code, data into insight,
                <br className="desktop" /> and ideas into meaningful
                experiences.
              </p>
            </div>
            <div className="hero-actions">
              <a className="button primary" href="#work">
                Explore my work <ArrowUpRight size={18} />
              </a>
              <a
                className="text-link"
                href="https://github.com/tniketha"
                target="_blank"
                rel="noreferrer"
              >
                <Github size={17} /> GitHub <ArrowUpRight size={14} />
              </a>
            </div>
          </div>
          <div className="hero-art">
            <div className="art-caption">
              <span className="status-dot" /> OPEN TO INTERNSHIPS & JUNIOR ROLES
            </div>
            <Suspense
              fallback={
                <div
                  className="scene scene-loading"
                  aria-label="Loading 3D sculpture"
                />
              }
            >
              <Scene reduced={reduced} />
            </Suspense>
            <span className="coordinate coordinate-top">
              FIG. 01 — AN EVOLVING MIND
            </span>
            <span className="coordinate coordinate-bottom">
              IDEAS ARE INFINITE. SO IS CURIOSITY.
            </span>
            <div className="signature">
              Built with curiosity.<span>Nikky</span>
            </div>
          </div>
          <div className="hero-bottom">
            <a href="#about">
              <span className="scroll-icon">
                <ArrowDown size={15} />
              </span>{" "}
              SCROLL TO DISCOVER
            </a>
            <span>
              BASED IN JAFFNA, SRI LANKA <span className="gold">↗</span>
            </span>
            <span className="edition">PORTFOLIO — 2026</span>
          </div>
        </section>
        <About />
        <Work onProject={setSelected} />
        <Skills />
        <Journey />
        <Certificates />
        <Contact />
      </main>
      <footer>
        <a href="#home" className="brand">
          NIKKY<span className="brand-dot">.</span>
        </a>
        <span>© {new Date().getFullYear()} NIKETHA THAVANESWARAN</span>
        <span>CRAFTED WITH CURIOSITY. BUILT TO EVOLVE.</span>
        <a href="#home" aria-label="Back to top">
          <ArrowUp size={20} />
        </a>
      </footer>
      <div className="tools" aria-label="Experience controls">
        <button
          title="Terminal · Ctrl / ⌘ K"
          aria-label="Open terminal"
          onClick={() => setTerminal(true)}
        >
          <Terminal size={17} />
        </button>
        <button
          title={theme === "dark" ? "Blueprint mode" : "Dark mode"}
          aria-label={
            theme === "dark"
              ? "Switch to blueprint theme"
              : "Switch to dark theme"
          }
          onClick={toggleTheme}
        >
          {theme === "dark" ? <Sun size={17} /> : <Moon size={17} />}
        </button>
        <button
          title={paused ? "Resume animations" : "Pause animations"}
          aria-label={paused ? "Resume animations" : "Pause animations"}
          aria-pressed={paused}
          onClick={() => setPaused((p) => !p)}
        >
          {paused ? <Play size={16} /> : <Pause size={16} />}
        </button>
      </div>
      {terminal && (
        <TerminalWindow
          onClose={() => setTerminal(false)}
          onTheme={toggleTheme}
        />
      )}{" "}
      {selected && (
        <ProjectDetails project={selected} onClose={() => setSelected(null)} />
      )}
    </>
  );
}
