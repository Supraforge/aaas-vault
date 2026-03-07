import React, { useState } from 'react';
import { RestaurantSlide1 } from './slides/RestaurantSlide1';
import { RestaurantSlide2 } from './slides/RestaurantSlide2';
import { RestaurantSlide3 } from './slides/RestaurantSlide3';
import { RestaurantSlide4 } from './slides/RestaurantSlide4';
import { RestaurantSlide5 } from './slides/RestaurantSlide5';
import { RestaurantSlide6 } from './slides/RestaurantSlide6';
import { RestaurantSlide7 } from './slides/RestaurantSlide7';
import { RestaurantSlide8 } from './slides/RestaurantSlide8';
import { ChevronLeft, ChevronRight, Download } from 'lucide-react';
import { Button } from './ui/button';

const slides = [
  { id: 1, component: <RestaurantSlide1 /> },
  { id: 2, component: <RestaurantSlide2 /> },
  { id: 3, component: <RestaurantSlide3 /> },
  { id: 4, component: <RestaurantSlide4 /> },
  { id: 5, component: <RestaurantSlide5 /> },
  { id: 6, component: <RestaurantSlide6 /> },
  { id: 7, component: <RestaurantSlide7 /> },
  { id: 8, component: <RestaurantSlide8 /> }
];

export function RestaurantCarousel() {
  const [currentSlide, setCurrentSlide] = useState(0);

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % slides.length);
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + slides.length) % slides.length);
  };

  const downloadSlide = async () => {
    const slideElement = document.getElementById('current-slide-restaurant');
    if (!slideElement) return;

    try {
      // Using html2canvas for screenshot
      const html2canvas = (await import('html2canvas')).default;
      const canvas = await html2canvas(slideElement, {
        width: 1080,
        height: 1080,
        scale: 2,
        backgroundColor: '#E4F1EF',
        logging: false,
        useCORS: true,
        allowTaint: false,
        removeContainer: true
      });
      
      // Convert to blob and download
      canvas.toBlob((blob) => {
        if (blob) {
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = `restaurant-trap-slide-${currentSlide + 1}.png`;
          a.click();
          URL.revokeObjectURL(url);
        }
      }, 'image/png');
    } catch (error) {
      console.error('Error downloading slide:', error);
      alert(`Error downloading slide: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  };

  const downloadAllSlides = async () => {
    for (let i = 0; i < slides.length; i++) {
      setCurrentSlide(i);
      // Wait for slide to render
      await new Promise(resolve => setTimeout(resolve, 500));
      await downloadSlide();
      // Wait between downloads
      await new Promise(resolve => setTimeout(resolve, 300));
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 flex flex-col items-center justify-center p-8">
      <div className="mb-6 text-center">
        <h1 className="mb-2" style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '36px',
          fontWeight: 700,
          color: '#F8F9FA'
        }}>
          The Restaurant Trap: Why Your Body Reacts Differently
        </h1>
        <p style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '18px',
          fontWeight: 400,
          color: '#94A3B8'
        }}>
          Instagram Carousel - 8 Slides
        </p>
      </div>

      {/* Slide preview */}
      <div className="relative mb-6 shadow-2xl rounded-lg overflow-hidden">
        <div id="current-slide-restaurant">
          {slides[currentSlide].component}
        </div>
      </div>

      {/* Controls */}
      <div className="flex items-center gap-4 mb-4">
        <Button
          onClick={prevSlide}
          variant="outline"
          size="lg"
          className="bg-white/10 hover:bg-white/20 text-white border-white/20"
        >
          <ChevronLeft className="mr-2" size={20} />
          Previous
        </Button>
        
        <div className="px-6 py-3 bg-white/10 rounded-lg">
          <span style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: '20px',
            fontWeight: 700,
            color: '#F8F9FA'
          }}>
            {currentSlide + 1} / {slides.length}
          </span>
        </div>
        
        <Button
          onClick={nextSlide}
          variant="outline"
          size="lg"
          className="bg-white/10 hover:bg-white/20 text-white border-white/20"
        >
          Next
          <ChevronRight className="ml-2" size={20} />
        </Button>
      </div>

      {/* Download controls */}
      <div className="flex gap-3">
        <Button
          onClick={downloadSlide}
          className="bg-gradient-to-r from-[#E63946] to-[#F28C81] hover:opacity-90"
        >
          <Download className="mr-2" size={18} />
          Download Current Slide
        </Button>
        
        <Button
          onClick={downloadAllSlides}
          className="bg-gradient-to-r from-[#207178] to-[#F28C81] hover:opacity-90"
        >
          <Download className="mr-2" size={18} />
          Download All Slides
        </Button>
      </div>

      {/* Thumbnail navigation */}
      <div className="mt-8 flex gap-3 flex-wrap justify-center max-w-[1200px]">
        {slides.map((slide, index) => (
          <button
            key={slide.id}
            onClick={() => setCurrentSlide(index)}
            className={`w-20 h-20 rounded-lg border-2 transition-all ${
              currentSlide === index
                ? 'border-[#E63946] shadow-lg scale-110'
                : 'border-white/20 hover:border-white/40 opacity-60 hover:opacity-100'
            }`}
            style={{
              background: currentSlide === index 
                ? 'linear-gradient(135deg, #E63946, #F28C81)' 
                : '#1e293b'
            }}
          >
            <span style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: '16px',
              fontWeight: 700,
              color: '#F8F9FA'
            }}>
              {slide.id}
            </span>
          </button>
        ))}
      </div>
    </div>
  );
}
