# React Performance Optimization Skill

Best Practices für schnelle, effiziente React-Apps (digitalTwin, DresdenAIInsights, ManufacturingInsideAnalyzer)

## Wann aktiviert?

- Keywords: performance, optimization, slow, lag, useMemo, useCallback, React.memo
- Du untersuchst Performance-Probleme
- Bundle Size, Rendering-Issues

## Goldene Regel

**Optimiere nur, was gemessen wurde!**

```bash
# React DevTools Profiler
# Chrome: Lighthouse
# Bundle Analyzer
npm run build && npx vite-bundle-visualizer
```

## 1. useMemo - Teure Berechnungen cachen

### Wann nutzen?

✅ **JA bei:**
- Filter/Map/Reduce über große Arrays (>1000 Items)
- Komplexe Berechnungen (>1ms)
- Derived State aus Props

❌ **NEIN bei:**
- Einfache Operationen (<1ms)
- Primitive Values (Strings, Numbers)

### Beispiele

**✅ GUT:**
```tsx
function DataTable({ items }: { items: Product[] }) {
  // Teurer Filter - nur bei items-Änderung neu berechnen
  const filteredItems = useMemo(
    () => items.filter(item => item.price > 100 && item.inStock),
    [items]
  );

  // Komplexe Aggregation
  const stats = useMemo(() => {
    return {
      total: items.length,
      avgPrice: items.reduce((sum, i) => sum + i.price, 0) / items.length,
      maxPrice: Math.max(...items.map(i => i.price))
    };
  }, [items]);

  return <Table data={filteredItems} stats={stats} />;
}
```

**❌ SCHLECHT - Unnötiges Memoizing:**
```tsx
// ❌ Zu simpel
const doubled = useMemo(() => count * 2, [count]);

// ❌ Schon optimiert
const Component = useMemo(() => <div>{text}</div>, [text]);
```

## 2. useCallback - Funktionen stabilisieren

### Wann nutzen?

✅ **JA bei:**
- Callbacks in Dependency-Arrays (`useEffect`, `useMemo`)
- Props an `React.memo` Components
- Event-Handler in Listen-Items

❌ **NEIN bei:**
- Top-Level Event-Handler (onClick in Parent)
- Einmalige Renders

### Beispiele

**✅ GUT:**
```tsx
function ParentComponent() {
  const [items, setItems] = useState([]);

  // Stabilisiert - verhindert Re-Render aller Kinder
  const handleDelete = useCallback((id: number) => {
    setItems(prev => prev.filter(item => item.id !== id));
  }, []); // Keine Dependencies - nutzt Updater-Function

  return items.map(item => (
    <MemoizedListItem key={item.id} item={item} onDelete={handleDelete} />
  ));
}

const MemoizedListItem = React.memo(({ item, onDelete }) => (
  <div>
    {item.name}
    <button onClick={() => onDelete(item.id)}>Delete</button>
  </div>
));
```

**❌ SCHLECHT:**
```tsx
// ❌ Callback wird trotzdem neu erstellt (closure über state)
const handleClick = useCallback(() => {
  console.log(count); // count in closure!
}, []); // ⚠️ Missing dependency

// ✅ Richtig
const handleClick = useCallback(() => {
  console.log(count);
}, [count]);
```

## 3. React.memo - Component Memoization

### Wann nutzen?

✅ **JA bei:**
- Pure Components (gleiche Props = gleiches Rendering)
- Teure Renders (>16ms)
- Listen-Items (viele Re-Renders)

❌ **NEIN bei:**
- Components mit wenig Re-Renders
- Props ändern sich häufig

### Beispiele

```tsx
// Vor Optimierung - Re-Rendert bei jedem Parent-Update
function ExpensiveComponent({ data }: { data: Data }) {
  // Teures Rendering (Diagramm, Visualisierung)
  return <HeavyChart data={data} />;
}

// ✅ Nach Optimierung
const ExpensiveComponent = React.memo(({ data }) => {
  return <HeavyChart data={data} />;
});

// Mit Custom Comparison
const ExpensiveComponent = React.memo(
  ({ data }) => <HeavyChart data={data} />,
  (prevProps, nextProps) => {
    // true = skip render, false = re-render
    return prevProps.data.id === nextProps.data.id;
  }
);
```

## 4. Code Splitting & Lazy Loading

### Route-Based Splitting

```tsx
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';

const Dashboard = lazy(() => import('./pages/Dashboard'));
const Analytics = lazy(() => import('./pages/Analytics'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  );
}
```

### Component-Based Splitting

```tsx
// Heavy component nur bei Bedarf laden
const HeavyEditor = lazy(() => import('./HeavyEditor'));

function Page() {
  const [showEditor, setShowEditor] = useState(false);

  return (
    <>
      <button onClick={() => setShowEditor(true)}>Edit</button>
      {showEditor && (
        <Suspense fallback={<Spinner />}>
          <HeavyEditor />
        </Suspense>
      )}
    </>
  );
}
```

## 5. Virtualization (Große Listen)

**Problem:** 10.000 List-Items = 10.000 DOM-Nodes = Lag

**Lösung:** Nur sichtbare Items rendern

```bash
npm install @tanstack/react-virtual
```

```tsx
import { useVirtualizer } from '@tanstack/react-virtual';

function LargeList({ items }: { items: Item[] }) {
  const parentRef = useRef<HTMLDivElement>(null);

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50, // Item-Höhe in px
    overscan: 5
  });

  return (
    <div ref={parentRef} style={{ height: '400px', overflow: 'auto' }}>
      <div style={{ height: `${virtualizer.getTotalSize()}px`, position: 'relative' }}>
        {virtualizer.getVirtualItems().map(virtualItem => (
          <div
            key={virtualItem.index}
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: `${virtualItem.size}px`,
              transform: `translateY(${virtualItem.start}px)`
            }}
          >
            {items[virtualItem.index].name}
          </div>
        ))}
      </div>
    </div>
  );
}
```

**ManufacturingInsideAnalyzer:** Für 1567×591 Datasets!

## 6. Bundle Size Optimization

### Analyze Bundle

```bash
npm run build
npx vite-bundle-visualizer
```

### Tree-Shaking

```ts
// ❌ Importiert gesamte Library
import _ from 'lodash';

// ✅ Nur benötigte Funktion
import debounce from 'lodash/debounce';
```

### Dynamic Imports

```ts
// ❌ Immer geladen
import { HeavyLibrary } from 'heavy-lib';

// ✅ Nur bei Bedarf
async function processData() {
  const { HeavyLibrary } = await import('heavy-lib');
  return HeavyLibrary.process(data);
}
```

## 7. Projekt-spezifische Optimierungen

### DresdenAIInsights (Particle Animations)

```tsx
import { useEffect, useRef } from 'react';

function ParticleBackground() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const animationRef = useRef<number>();

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    let lastTime = 0;
    const fps = 30; // Reduziert von 60fps
    const fpsInterval = 1000 / fps;

    function animate(currentTime: number) {
      animationRef.current = requestAnimationFrame(animate);

      const elapsed = currentTime - lastTime;
      if (elapsed < fpsInterval) return;

      lastTime = currentTime - (elapsed % fpsInterval);

      // Render particles...
    }

    animate(0);

    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, []);

  return <canvas ref={canvasRef} />;
}
```

### digitalTwin (Camera Stream)

```tsx
function CameraView() {
  const videoRef = useRef<HTMLVideoElement>(null);

  // Throttle AI-Analysis (nicht jedes Frame!)
  const analyzeFrame = useMemo(
    () => debounce(async (frame: ImageData) => {
      await geminiAnalysis(frame);
    }, 1000), // Max 1x pro Sekunde
    []
  );

  return <video ref={videoRef} />;
}
```

### ManufacturingInsideAnalyzer (Large Data)

```tsx
// Smart Sampling statt Full Dataset
function useSmartSampling<T>(data: T[], maxSize = 5000): T[] {
  return useMemo(() => {
    if (data.length <= maxSize) return data;

    // Stratified Sampling
    const step = Math.ceil(data.length / maxSize);
    return data.filter((_, i) => i % step === 0);
  }, [data, maxSize]);
}
```

## 8. Performance Checklist

- [ ] React DevTools Profiler genutzt?
- [ ] Bundle < 500KB (gzipped)?
- [ ] Code-Splitting aktiviert?
- [ ] Virtualization bei Listen > 100 Items?
- [ ] useMemo nur für teure Ops (>1ms)?
- [ ] useCallback nur wo nötig?
- [ ] React.memo nur für Pure Components?
- [ ] Images optimiert (WebP, lazy loading)?
- [ ] Keine Memory Leaks (cleanup in useEffect)?

## Ressourcen

- [React DevTools Profiler](https://react.dev/learn/react-developer-tools)
- [React.memo Guide](https://react.dev/reference/react/memo)
- [TanStack Virtual](https://tanstack.com/virtual/latest)
