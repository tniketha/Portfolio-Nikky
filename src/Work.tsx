import { useId, useState } from 'react';
import { ArrowLeft, ArrowRight, ArrowUpRight, Check, ChevronLeft, ChevronRight, Github, Maximize2 } from 'lucide-react';
import { Modal, Reveal } from './Effects';
import { projects } from './data';
import type { Project, ProjectScreenshot } from './data';
import './work.css';

function screenshotPath(project: Project, shot: ProjectScreenshot) {
 return `${import.meta.env.BASE_URL}projects/${project.kind}/${shot.file}?v=20261025-js-projects`;
}

function ScreenshotGallery({ project }: { project: Project }) {
 const [active, setActive] = useState(0);
 const captionId = useId();
 const shot = project.screenshots[active];
 return <div className="project-gallery" role="region" aria-label={`${project.title} screenshots`}>
  <div className="gallery-bar">
   <span><i aria-hidden="true"/><i aria-hidden="true"/><i aria-hidden="true"/></span>
   <span>INSIDE THE APPLICATION</span>
   <a href={screenshotPath(project, shot)} target="_blank" rel="noreferrer" aria-label={`Open full-size ${project.title} ${shot.label} screenshot`} title="Open full-size screenshot"><Maximize2 size={15}/></a>
  </div>
  <figure className="gallery-figure">
   <div className="gallery-stage">
    <img src={screenshotPath(project, shot)} alt={shot.alt} aria-describedby={captionId} loading="lazy" decoding="async"/>
   </div>
   <figcaption id={captionId} aria-live="polite" aria-atomic="true">{shot.caption}</figcaption>
  </figure>
  <div className="gallery-navigation">
   <div className="gallery-choices" role="group" aria-label={`Choose a ${project.title} screen`}>
    {project.screenshots.map((item, index) => <button type="button" key={item.file} aria-pressed={active === index} onClick={() => setActive(index)}>{item.label}</button>)}
   </div>
   <div className="gallery-arrows">
    <button type="button" aria-label={`Previous ${project.title} screenshot`} onClick={() => setActive(i => (i - 1 + project.screenshots.length) % project.screenshots.length)}><ChevronLeft size={17}/></button>
    <span aria-hidden="true">{String(active + 1).padStart(2, '0')} / {String(project.screenshots.length).padStart(2, '0')}</span>
    <button type="button" aria-label={`Next ${project.title} screenshot`} onClick={() => setActive(i => (i + 1) % project.screenshots.length)}><ChevronRight size={17}/></button>
   </div>
  </div>
  <p className="gallery-note">Actual app screens · Fictional demo data · Mobile screens are responsive web views.</p>
 </div>;
}

function ProjectCard({ project, index, onOpen }: { project: Project; index: number; onOpen: () => void }) {
 return <Reveal>
  <article className="case-study-card" aria-labelledby={`${project.kind}-title`}>
   <div className="case-study-meta"><span>SELECTED WORK / {String(index + 1).padStart(2, '0')}</span><span>SOLE DEVELOPER · <a href="https://github.com/tniketha" target="_blank" rel="noreferrer">{project.author}</a></span></div>
   <div className="case-study-body">
    <div className="case-study-copy">
     <p className="eyebrow">{project.category}</p>
     <h3 id={`${project.kind}-title`}>{project.title}</h3>
     <p className="case-study-subtitle">{project.subtitle}</p>
     <p className="case-study-description">{project.description}</p>
     <ul className="case-study-highlights">{project.highlights.map(item => <li key={item}><Check size={15}/>{item}</li>)}</ul>
     <div className="case-study-actions"><button className="button primary" type="button" onClick={onOpen} aria-label={`Read ${project.title} case study`}>Read case study <ArrowUpRight size={17}/></button><a className="text-link" href={project.repository} target="_blank" rel="noreferrer" aria-label={`View ${project.title} source on GitHub`}><Github size={17}/> Source code <ArrowUpRight size={14}/></a></div>
    </div>
    <ScreenshotGallery project={project}/>
   </div>
   <div className="case-study-stack"><span>BUILT WITH</span><div className="chips">{project.stack.map(item => <span key={item}>{item}</span>)}</div></div>
  </article>
 </Reveal>;
}

export function Work({ onProject }: { onProject: (project: Project) => void }) {
 return <section className="section work selected-work" id="work" aria-labelledby="work-heading">
  <Reveal className="section-heading"><div><p className="eyebrow">02 / SELECTED PROJECTS</p><h2 id="work-heading">REAL PROBLEMS.<br/><span>WORKING SOFTWARE.</span></h2></div><p className="section-description">Two full-stack projects, from the interface to the API and database. Explore the screens and the engineering behind them.</p></Reveal>
  <div className="case-study-list">{projects.map((project, index) => <ProjectCard key={project.kind} project={project} index={index} onOpen={() => onProject(project)}/>)}</div>
  <div className="work-next-step"><span>Interested in how I build?</span><a className="text-link" href="#contact">Let’s talk about an opportunity <ArrowUpRight size={17}/></a></div>
 </section>;
}

export function ProjectDetails({ project, onClose }: { project: Project; onClose: () => void }) {
 return <Modal title={`${project.title.toUpperCase()} / CASE STUDY`} onClose={onClose} className="project-modal case-study-modal">
  <div className="project-detail case-study-detail">
   <p className="eyebrow">{project.category}</p><h2>{project.title}</h2><p className="detail-subtitle">{project.subtitle}</p>
   <p className="case-study-author">Sole developer & author: <a href="https://github.com/tniketha" target="_blank" rel="noreferrer">{project.author} <ArrowUpRight size={13}/></a></p>
   <h3>The problem & my approach</h3><p>{project.problem}</p>
   <ScreenshotGallery project={project}/>
   <h3>What I built</h3><ul className="case-study-features">{project.features.map(feature => <li key={feature}><Check size={16}/>{feature}</li>)}</ul>
   <h3>How it fits together</h3><div className="case-study-architecture">{project.architecture.map((item, index) => <div key={item.name}><span className="architecture-number">0{index + 1}</span><strong>{item.name}</strong><p>{item.role}</p>{index < project.architecture.length - 1 && <ArrowRight size={16} aria-hidden="true"/>}</div>)}</div>
   <h3>Engineering decisions</h3><div className="case-study-decisions">{project.decisions.map(item => <div key={item.title}><h4>{item.title}</h4><p>{item.description}</p></div>)}</div>
   <div className="case-study-scope"><h3>Project scope</h3><p>{project.scope}</p><p>Implementation and test scenarios are available in the repository.</p></div>
   <div className="case-study-detail-actions"><a className="button primary" href={project.repository} target="_blank" rel="noreferrer"><Github size={17}/> Explore the repository <ArrowUpRight size={16}/></a><button className="text-link" type="button" onClick={onClose}><ArrowLeft size={16}/> Back to portfolio</button></div>
  </div>
 </Modal>;
}
