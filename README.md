# NIKKY - Interactive portfolio

A responsive portfolio for Niketha Thavaneswaran, built with React 19, TypeScript, Vite, Tailwind CSS 4, Framer Motion, Lenis, and Three.js.

## Run locally

```sh
npm install
npm run dev
```

Create a production build with `npm run build`. Preview that build with `npm run preview`.

## Features

- Interactive, lazy-loaded 3D gold sculpture with an animated orbital particle field.
- Smooth scrolling, responsive project stack, 3D card tilt, cursor spotlight, and scroll-linked timeline.
- Dark and blueprint themes; optional sound; motion pause and system reduced-motion support.
- Accessible terminal dialog (`Ctrl/Cmd + K`): `help`, `cat about.txt`, `ls projects`, `skills`, `contact`, `theme`, `clear`, and `exit`.
- Live public GitHub repository and follower counts, with a graceful unavailable state.
- DNA-sequence analysis with validation and CSV export, plus a browser-only attendance concept demo.
- Downloadable one-page CV with education, skills, and projects.
- Contact form that prepares an email draft. It does not send messages or claim delivery.

## Update content

Project descriptions and the email address are in `src/data.ts`. Sections and project demos are in `src/Sections.tsx`; global controls are in `src/App.tsx`. The 3D scene is in `src/Scene.tsx` and styling is in `src/style.css`.

The profile card uses a typographic monogram. Project cards open details and interactive demos, with links to my GitHub profile.

To update the CV, edit `scripts/create-cv.py` and run it with Python and ReportLab installed. Replace `public/Niketha-Thavaneswaran-CV.pdf` with an updated CV at any time.

## Deployment

The site is a static Vite build. Fonts load from Google Fonts, and live statistics come from the public GitHub API. No API keys are required.

## Verified

TypeScript compilation and production build; desktop and mobile layout inspection; terminal commands; attendance total updates; DNA GC-content calculation and invalid-input handling; theme switching; contact draft creation; CV rendering.
