import { useEffect, useRef } from 'react';
import * as THREE from 'three';

export default function Scene({ reduced = false }: { reduced?: boolean }) {
  const host = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!host.current) return;
    const element = host.current;
    let renderer: THREE.WebGLRenderer;
    try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' }); }
    catch { element.dataset.fallback = 'true'; return; }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.7));
    renderer.setClearColor(0x000000, 0);
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.5;
    element.appendChild(renderer.domElement);
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(36, 1, .1, 100);
    camera.position.set(0, 0, 8.8);
    const sculpture = new THREE.Group();
    scene.add(sculpture);
    const geometry = new THREE.TorusKnotGeometry(1.27, .39, 240, 40, 2, 3);
    const material = new THREE.MeshStandardMaterial({ color: 0xbba06a, metalness: .85, roughness: .28 });
    const knot = new THREE.Mesh(geometry, material);
    sculpture.add(knot);
    const cage = new THREE.Mesh(new THREE.TorusKnotGeometry(1.28, .41, 100, 16, 2, 3), new THREE.MeshBasicMaterial({color:0xf7ddb0,wireframe:true,transparent:true,opacity:.095}));
    sculpture.add(cage);
    sculpture.rotation.set(.55, -.35, -.38);
    scene.add(new THREE.AmbientLight(0xfceac9, 1.5));
    const key = new THREE.DirectionalLight(0xffe4a5, 6); key.position.set(-3, 5, 4); scene.add(key);
    const rim = new THREE.DirectionalLight(0xe9f0ff, 4); rim.position.set(4, 2, -2); scene.add(rim);
    const warm = new THREE.PointLight(0xe1a34e, 50); warm.position.set(-2,-3,2); scene.add(warm);
    const soft = new THREE.DirectionalLight(0xffedc7, 2); soft.position.set(0,-4,4); scene.add(soft);
    const ringMaterial = new THREE.LineBasicMaterial({color:0xb7a06f,transparent:true,opacity:.3});
    const rings: THREE.LineLoop[] = [];
    for (let i=0;i<3;i++) {
      const pts=Array.from({length:160},(_,n)=>new THREE.Vector3(Math.cos(n/160*Math.PI*2)*2.35,Math.sin(n/160*Math.PI*2)*2.35,0));
      const ring=new THREE.LineLoop(new THREE.BufferGeometry().setFromPoints(pts),ringMaterial);
      ring.rotation.set(.4+i*.65,.3+i*.5,.2);scene.add(ring);rings.push(ring);
    }
    const positions = new Float32Array(170*3);
    for(let i=0;i<positions.length;i++) positions[i]=(Math.random()-.5)*10;
    const dustGeometry=new THREE.BufferGeometry();dustGeometry.setAttribute('position',new THREE.BufferAttribute(positions,3));
    const dust=new THREE.Points(dustGeometry,new THREE.PointsMaterial({color:0xe9d3a7,size:.018,transparent:true,opacity:.6}));scene.add(dust);
    let pointerX=0,pointerY=0,frame=0,visible=true;
    const move=(e:PointerEvent)=>{const r=element.getBoundingClientRect();pointerX=((e.clientX-r.left)/r.width-.5)*.5;pointerY=((e.clientY-r.top)/r.height-.5)*.4;};
    const leave=()=>{pointerX=0;pointerY=0;};
    element.addEventListener('pointermove',move);element.addEventListener('pointerleave',leave);
    const resize=()=>{const {width,height}=element.getBoundingClientRect();renderer.setSize(width,height);camera.aspect=width/height;camera.updateProjectionMatrix();};
    const observer=new ResizeObserver(resize);observer.observe(element);resize();
    const intersection=new IntersectionObserver(([entry])=>{visible=entry.isIntersecting;});intersection.observe(element);
    const clock=new THREE.Clock();
    const animate=()=>{frame=requestAnimationFrame(animate);if(!visible||document.hidden)return;const t=clock.getElapsedTime();if(!reduced){sculpture.rotation.y= -.35+t*.10+pointerX;sculpture.rotation.x+=(.55+pointerY-sculpture.rotation.x)*.04;sculpture.position.y=Math.sin(t*.65)*.09;rings.forEach((r,i)=>r.rotation.z=t*.035*(i%2?1:-1));dust.rotation.y=t*.018;}renderer.render(scene,camera);};animate();
    return()=>{cancelAnimationFrame(frame);observer.disconnect();intersection.disconnect();element.removeEventListener('pointermove',move);element.removeEventListener('pointerleave',leave);scene.traverse(o=>{if(o instanceof THREE.Mesh||o instanceof THREE.Line||o instanceof THREE.Points){o.geometry.dispose();(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>m.dispose());}});renderer.dispose();renderer.domElement.remove();};
  },[reduced]);
  return <div className="scene" ref={host} role="img" aria-label="Interactive gold three-dimensional orbital sculpture"><span className="scene-fallback">N</span></div>;
}
