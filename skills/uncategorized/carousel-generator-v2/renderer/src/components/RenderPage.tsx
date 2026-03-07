import React, { useEffect, useState } from 'react';
import { HookSlide, HookSlideData } from './templates/HookSlide';
import { MythSlide, MythSlideData } from './templates/MythSlide';
import { StatSlide, StatSlideData } from './templates/StatSlide';
import { TipsSlide, TipsSlideData } from './templates/TipsSlide';
import { CTASlide, CTASlideData } from './templates/CTASlide';
import { DataSlide, DataSlideData } from './templates/DataSlide';

type SlideType = 'hook' | 'myth' | 'stat' | 'tips' | 'cta' | 'data';

interface SlideData {
  type: SlideType;
  data: HookSlideData | MythSlideData | StatSlideData | TipsSlideData | CTASlideData | DataSlideData;
}

export function RenderPage() {
  const [slideData, setSlideData] = useState<SlideData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Read slide data from localStorage (set by Puppeteer)
    const dataStr = localStorage.getItem('slideData');
    if (dataStr) {
      try {
        const data = JSON.parse(dataStr);
        setSlideData(data);
      } catch (e) {
        setError(`Failed to parse slide data: ${e}`);
      }
    }

    // Also expose a function for Puppeteer to call directly
    (window as any).setSlideData = (data: SlideData) => {
      setSlideData(data);
    };

    // Listen for custom events
    const handleSetData = (e: CustomEvent) => {
      setSlideData(e.detail);
    };
    window.addEventListener('setSlideData', handleSetData as EventListener);

    return () => {
      window.removeEventListener('setSlideData', handleSetData as EventListener);
    };
  }, []);

  if (error) {
    return (
      <div className="p-8 text-red-500">
        <h1>Error</h1>
        <p>{error}</p>
      </div>
    );
  }

  if (!slideData) {
    return (
      <div className="p-8">
        <h1 className="text-2xl font-bold mb-4">Carousel Slide Renderer</h1>
        <p className="text-gray-600">Waiting for slide data...</p>
        <p className="text-sm text-gray-400 mt-4">
          Set slide data via localStorage.setItem('slideData', JSON.stringify(data))
          or window.setSlideData(data)
        </p>
      </div>
    );
  }

  const renderSlide = () => {
    switch (slideData.type) {
      case 'hook':
        return <HookSlide {...(slideData.data as HookSlideData)} />;
      case 'myth':
        return <MythSlide {...(slideData.data as MythSlideData)} />;
      case 'stat':
        return <StatSlide {...(slideData.data as StatSlideData)} />;
      case 'tips':
        return <TipsSlide {...(slideData.data as TipsSlideData)} />;
      case 'cta':
        return <CTASlide {...(slideData.data as CTASlideData)} />;
      case 'data':
        return <DataSlide {...(slideData.data as DataSlideData)} />;
      default:
        return <div>Unknown slide type: {slideData.type}</div>;
    }
  };

  const dimensions =
    slideData && 'dimensions' in slideData.data
      ? (slideData.data as { dimensions?: 'square' | 'portrait' }).dimensions
      : 'square';
  const height = dimensions === 'portrait' ? 1350 : 1080;

  return (
    <div id="slide-container" style={{ width: 1080, height }}>
      {renderSlide()}
    </div>
  );
}
