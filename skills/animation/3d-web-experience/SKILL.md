---
name: 3d-web-experience
description: "3D Web Experience Architect. Build immersive 3D websites using Spline, Three.js, React Three Fiber, and WebGL. Covers product configurators, 3D portfolios, immersive landing pages, scroll-driven 3D animations, and interactive scenes. Use when: 3D website, three.js, WebGL, react three fiber, spline, 3D landing page, interactive 3D, scroll animation, product viewer, immersive web experience."
---

# 3D Web Experience Architect

You bring the third dimension to the web. You know when 3D enhances an experience versus when it's decorative waste. You balance visual impact with performance. You make 3D accessible to users who've never touched a 3D app.

## Stack Selection Decision Tree

Match the tool to the job:

| Need | Tool | Complexity | Control |
|------|------|-----------|---------|
| Quick 3D element, no-code | **Spline** | Low | Medium |
| React-based app | **React Three Fiber + Drei** | Medium | High |
| Maximum control, vanilla JS | **Three.js** | High | Maximum |
| Heavy 3D / games | **Babylon.js** | High | Maximum |

**Default recommendation**: Start with Spline for prototyping, graduate to React Three Fiber for production React apps.

---

## Spline Integration (Fastest Path)

### Workflow
1. Browse community assets at [spline.design/community](https://spline.design/community)
2. Remix or create custom 3D scenes in Spline
3. Export via URL or vanilla.js export
4. Integrate into your web project

### React Integration
```jsx
import Spline from '@splinetool/react-spline';

export default function Hero() {
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <Spline scene="https://prod.spline.design/YOUR_SCENE_ID/scene.splinecode" />
    </div>
  );
}
```

### Vanilla JS Integration
```html
<script type="module">
  import { Application } from '@splinetool/runtime';
  const canvas = document.getElementById('canvas3d');
  const app = new Application(canvas);
  app.load('https://prod.spline.design/YOUR_SCENE_ID/scene.splinecode');
</script>
```

### Spline Best Practices
- Set scene background to transparent when overlaying on web content
- Use Spline events for click/hover interactivity
- Export as vanilla.js for non-React projects
- Ensure full-viewport display for hero sections (width: 100vw, height: 100vh)
- Test mobile performance — Spline scenes can be heavy on low-end devices

---

## React Three Fiber (Production React)

### Setup
```bash
npm install three @react-three/fiber @react-three/drei
```

### Basic Scene
```jsx
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Environment, useGLTF } from '@react-three/drei';
import { Suspense } from 'react';

function Model({ url }) {
  const { scene } = useGLTF(url);
  return <primitive object={scene} />;
}

export default function Scene3D() {
  return (
    <Canvas camera={{ position: [0, 2, 5], fov: 45 }}>
      <Suspense fallback={null}>
        <ambientLight intensity={0.5} />
        <directionalLight position={[10, 10, 5]} intensity={1} />
        <Model url="/models/product.glb" />
        <OrbitControls enableZoom={false} />
        <Environment preset="studio" />
      </Suspense>
    </Canvas>
  );
}
```

### Loading States (Non-Negotiable)
```jsx
import { Html, useProgress } from '@react-three/drei';

function Loader() {
  const { progress } = useProgress();
  return <Html center>{progress.toFixed(0)}% loaded</Html>;
}

// Use in Canvas:
<Suspense fallback={<Loader />}>
  <Model url="/models/product.glb" />
</Suspense>
```

---

## Scroll-Driven 3D Animations

### Using Drei ScrollControls
```jsx
import { ScrollControls, Scroll, useScroll } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import { useRef } from 'react';

function AnimatedModel() {
  const ref = useRef();
  const scroll = useScroll();

  useFrame(() => {
    const offset = scroll.offset; // 0 to 1
    ref.current.rotation.y = offset * Math.PI * 2;
    ref.current.position.y = offset * -5;
  });

  return <Model ref={ref} url="/models/product.glb" />;
}

export default function ScrollScene() {
  return (
    <Canvas>
      <ScrollControls pages={3} damping={0.25}>
        <AnimatedModel />
        <Scroll html>
          <section style={{ height: '100vh' }}>
            <h1>Section One</h1>
          </section>
          <section style={{ height: '100vh' }}>
            <h2>Section Two</h2>
          </section>
        </Scroll>
      </ScrollControls>
    </Canvas>
  );
}
```

### Using GSAP for Camera Choreography
```jsx
import { useRef, useEffect } from 'react';
import { useThree } from '@react-three/fiber';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

function CameraRig() {
  const { camera } = useThree();

  useEffect(() => {
    gsap.to(camera.position, {
      x: 5, y: 3, z: 2,
      scrollTrigger: {
        trigger: '#section-2',
        start: 'top center',
        end: 'bottom center',
        scrub: 1,
      },
    });
  }, [camera]);

  return null;
}
```

### Scroll-Driven Effects Catalog
- **Camera movement**: Pan, zoom, orbit tied to scroll position
- **Model rotation**: Progressive rotation revealing different angles
- **Material transitions**: Color/texture morphing between scroll sections
- **Exploded views**: Parts separating on scroll to reveal internals
- **Scale transitions**: Objects growing/shrinking based on viewport
- **Opacity fades**: Elements appearing/disappearing with depth

---

## 3D Model Optimization Pipeline

Web 3D demands aggressive optimization. Follow this pipeline:

### 1. Polygon Reduction
- Target: **< 100K polygons** for web models
- Use Blender's Decimate modifier or meshopt
- Preserve silhouette edges, reduce interior geometry

### 2. Texture Optimization
- Bake multiple materials into single texture atlases
- Use WebP format for texture compression
- Max texture size: 2048x2048 for web (1024 for mobile)

### 3. Export & Compress
```bash
# Install gltf-transform
npm install -g @gltf-transform/cli

# Optimize with Draco compression + WebP textures
gltf-transform optimize input.glb output.glb --compress draco --texture-compress webp
```

### 4. Size Targets
| Asset Type | Max Size | Polygon Budget |
|-----------|----------|----------------|
| Hero model | 5 MB | 100K |
| Product viewer | 3 MB | 50K |
| Background element | 1 MB | 20K |
| Mobile fallback | 500 KB | 10K |

---

## Anti-Patterns — What NOT to Do

### 3D for Decoration
Using 3D without functional purpose:
- Slows the site
- Confuses users
- Drains mobile battery
- Doesn't improve conversion
- **Ask**: Would a static image or CSS animation work just as well?

### Desktop-Only 3D
Most traffic is mobile. Unoptimized 3D crashes low-end devices.
- Always test on real mobile hardware
- Provide 2D fallbacks for < 4GB RAM devices
- Use `navigator.deviceMemory` and `navigator.hardwareConcurrency` for adaptive quality

### Missing Loading States
Users see a blank canvas and think the site is broken.
- Always show loading progress
- Use skeleton screens while 3D initializes
- Lazy-load 3D scenes below the fold

### Performance Ignorance
- Never skip FPS monitoring during development
- Use `@react-three/drei`'s `PerformanceMonitor` to auto-adjust quality
- Cap draw calls, monitor GPU memory

---

## Adaptive Quality (Mobile-First)

```jsx
import { PerformanceMonitor } from '@react-three/drei';
import { useState } from 'react';

function AdaptiveScene() {
  const [dpr, setDpr] = useState(1.5);

  return (
    <Canvas dpr={dpr}>
      <PerformanceMonitor
        onIncline={() => setDpr(2)}
        onDecline={() => setDpr(1)}
      >
        <Scene />
      </PerformanceMonitor>
    </Canvas>
  );
}
```

---

## Full-Stack Integration Patterns

### Email Capture with Beehiiv
Connect 3D landing pages to email collection:
```js
async function subscribeEmail(email) {
  const res = await fetch('https://api.beehiiv.com/v2/publications/YOUR_PUB_ID/subscriptions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.BEEHIIV_API_KEY}`,
    },
    body: JSON.stringify({ email, reactivate_existing: true }),
  });
  return res.json();
}
```

### Webhook Automation with GoHighLevel
Trigger workflows on form submission:
```js
async function triggerWorkflow(data) {
  await fetch(process.env.GHL_WEBHOOK_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
}
```

### Database with Supabase
Store user interactions without SQL:
```js
import { createClient } from '@supabase/supabase-js';
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY);

async function saveInteraction(userId, action) {
  const { data, error } = await supabase
    .from('interactions')
    .insert({ user_id: userId, action, timestamp: new Date() });
  return { data, error };
}
```

---

## Deployment Checklist

1. **Optimize all 3D assets** (Draco compression, WebP textures)
2. **Test mobile performance** on real devices
3. **Implement loading states** for all 3D scenes
4. **Add 2D fallbacks** for low-end devices
5. **Verify scroll animations** work on touch devices
6. **Push to GitHub** and deploy via Vercel
7. **Lighthouse audit** — target > 70 performance score with 3D

---

## Complementary Skills

This skill works best alongside:
- `frontend-design` — Distinctive visual aesthetics for the 2D layer
- `ui-ux-pro-max` — Component design and accessibility
- `stitch-web-designer` — AI-assisted page generation
- `canvas-design` — Visual design philosophy for mood/direction