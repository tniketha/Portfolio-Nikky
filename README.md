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
- Smart Attendance and ShopFlow case studies with repository-backed features, engineering decisions, and direct source links.
- Interactive screenshot galleries with six real application screens per project, full-size image links, and desktop/mobile views.
- Downloadable monochrome, single-column CV with education, skills, projects, courses, and participation.
- Filterable certificate cards with confirmed issuers, dates, credential IDs, team names, and original documents.
- Contact form that prepares an email draft. It does not send messages or claim delivery.

## Update content

Project descriptions and the email address are in `src/data.ts`. Project galleries and case studies are in `src/Work.tsx` and `src/work.css`; other sections are in `src/Sections.tsx`; global controls are in `src/App.tsx`. The 3D scene is in `src/Scene.tsx` and styling is in `src/style.css`.

The profile card uses a typographic monogram. Both projects identify `tniketha` as their sole developer and author. Screenshots in `public/projects/` are copied from the project repositories and use fictional demonstration data; mobile images show responsive web layouts. Source provenance is recorded in `public/projects/README.md`. Repository links lead to source code.

Certificate records are shared by the portfolio and CV in `src/certificates.json`. Renamed originals are in `public/certificates/`; the source files supplied by the owner are preserved. Course completions and participation are labeled separately.

To update the CV, edit `scripts/create-cv.py` and run it with Python and ReportLab installed. Replace `public/Niketha-Thavaneswaran-CV.pdf` with an updated CV at any time.

## Deployment

The public portfolio is hosted at https://tniketha.github.io/Portfolio-Nikky/.

GitHub Actions checks, builds, and publishes the site whenever changes are pushed to `main`. The workflow is in `.github/workflows/deploy.yml`. In the repository's Pages settings, the source must be set to **GitHub Actions**.

For a local GitHub Pages build, run `npm run build -- --mode github-pages`. This uses `/Portfolio-Nikky/` for asset and CV links. Normal builds keep `/` for other hosting providers.

The site is a static Vite build. Fonts load from Google Fonts, and live statistics come from the public GitHub API. No API keys are required.

## Verified

TypeScript compilation and production build; desktop and mobile layout inspection; terminal commands; both project case studies, screenshot controls, image paths, and repository links; theme switching; contact draft creation; CV rendering.

## Author

tniketha
