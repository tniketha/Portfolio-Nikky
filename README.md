# NIKKY - Interactive portfolio

A responsive portfolio for Niketha Thavaneswaran, built with React 19, Vite, Tailwind CSS 4, Framer Motion, and Three.js.

## Run locally

```sh
npm install
npm run dev
```

Create a production build with `npm run build`. Preview that build with `npm run preview`.

## Features

- Interactive, lazy-loaded 3D gold sculpture with a 30 fps decorative animation budget; animation stops off-screen, in hidden tabs, or when paused.
- Native wheel/touch scrolling, smooth anchor links, responsive project galleries, card tilt, and a scroll-linked timeline.
- Dark and blueprint themes; optional sound; motion pause and system reduced-motion support.
- Accessible terminal dialog (`Ctrl/Cmd + K`): `help`, `cat about.txt`, `ls projects`, `skills`, `contact`, `theme`, `clear`, and `exit`.
- Live public GitHub repository and follower counts, with a graceful unavailable state.
- Smart Attendance and ShopFlow case studies with repository-backed features, engineering decisions, and direct source links.
- Interactive screenshot galleries with all current application screens (nine for Smart Attendance and eight for ShopFlow), full-size image links, and desktop/mobile views.
- One-page CV with education, technical skills, concise project workflows, all eight clickable certificates in two columns, memberships, and a reference listed line by line.
- Filterable certificate cards with confirmed issuers, dates, credential IDs, team names, and original documents.
- Contact form that prepares an email draft. It does not send messages or claim delivery.

## Update content

Project descriptions and the email address are in `src/data.ts`. Project galleries and case studies are in `src/Work.tsx` and `src/work.css`; other sections are in `src/Sections.tsx`; global controls are in `src/App.tsx`. The 3D scene is in `src/Scene.tsx` and styling is in `src/style.css`.

The profile card uses a typographic monogram. Both projects identify `tniketha` as their sole developer and author. Screenshots in `public/projects/` are copied from the project repositories and use fictional demonstration data; mobile images show responsive web layouts. Source provenance is recorded in `public/projects/README.md`. Repository links lead to source code.

Certificate records are shared by the portfolio and CV in `src/certificates.json`. Renamed originals are in `public/certificates/`; the source files supplied by the owner are preserved. Course completions and participation are labeled separately.

To update the CV, edit `scripts/cv_layout.py`, then run `python scripts/create-cv.py` with ReportLab installed. The current version records the 2023-2027 study period. Its layout uses selectable text, consistent section rules, aligned dates, and hanging bullet indents. Reference details are in `src/cv-reference.json`; their phone and email appear as plain text. Replace `public/Niketha-Thavaneswaran-CV.pdf` with an updated CV at any time.

CV readability and targeting follow [Harvard Career Services guidance](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/). Review the role-specific wording against each internship description before applying.

Run `npm test` to check the decorative scene's scheduling: inactive scenes schedule no frames, pause cancels pending work, and re-entry resumes one loop with a 30 fps rendering cap. Wheel and touch scrolling use the browser directly; only anchor navigation uses smooth scrolling. GitHub Actions runs these checks before publishing.

## Deployment

The public portfolio is hosted at https://tniketha.github.io/Portfolio-Nikky/.

GitHub Actions checks, builds, and publishes the site whenever changes are pushed to `main`. The workflow is in `.github/workflows/deploy.yml`. In the repository's Pages settings, the source must be set to **GitHub Actions**.

For a local GitHub Pages build, run `npm run build -- --mode github-pages`. This uses `/Portfolio-Nikky/` for asset and CV links. Normal builds keep `/` for other hosting providers.

The site is a static Vite build. Fonts load from Google Fonts, and live statistics come from the public GitHub API. No API keys are required.

## Verified

Static checks and production build; desktop and mobile layout inspection; terminal commands; both project case studies, screenshot controls, image paths, and repository links; theme switching; contact draft creation; CV rendering.

## Author

tniketha
