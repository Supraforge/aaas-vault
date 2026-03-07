import React from 'react';
import { SlideLayoutData } from './SlideLayoutData';
import { X, Check } from 'lucide-react';
import { BRAND } from '@/theme/brand';

export interface MythSlideData {
  slideNumber: number;
  totalSlides: number;
  myth: string;
  truth: string;
  source?: string;
  dimensions?: 'square' | 'portrait';
}

export function MythSlide({
  slideNumber,
  totalSlides,
  myth,
  truth,
  source,
  dimensions = 'square'
}: MythSlideData) {
  const isPortrait = dimensions === 'portrait';
  const mythSize = isPortrait ? '40px' : '36px';
  const truthSize = isPortrait ? '40px' : '36px';
  const ghostNumber = slideNumber.toString().padStart(2, '0');

  const backgroundElements = (
    <>
      {/* Soft gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#FFF7F8] via-[#F9FBFA] to-[#EEF7F3]"></div>

      {/* Decorative shapes */}
      <div className="absolute top-10 right-10 w-[140px] h-[140px] rounded-full" style={{ backgroundColor: 'rgba(239, 83, 80, 0.18)' }}></div>
      <div className="absolute bottom-28 left-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(39, 174, 96, 0.12)' }}></div>

      {/* Ghost slide number */}
      <div
        className="absolute -top-6 right-8"
        style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '160px',
          fontWeight: 900,
          color: 'rgba(239, 83, 80, 0.1)'
        }}
      >
        {ghostNumber}
      </div>
    </>
  );

  return (
    <SlideLayoutData
      slideNumber={slideNumber.toString()}
      totalSlides={totalSlides}
      backgroundElements={backgroundElements}
      dimensions={dimensions}
    >
      <div className="px-10 h-full flex flex-col justify-center gap-8">
        {/* MYTH Card */}
        <div className="relative rounded-[32px] border border-[#F7C7CB] bg-white/85 p-8 shadow-xl">
          <div className="flex items-center gap-4 mb-4">
            <div className="w-14 h-14 rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg" style={{ backgroundColor: BRAND.alert }}>
              <X size={30} color="#FFFFFF" strokeWidth={3} />
            </div>
            <span style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: '24px',
              fontWeight: 800,
              color: BRAND.alert,
              textTransform: 'uppercase',
              letterSpacing: '2px'
            }}>
              MYTH
            </span>
          </div>
          <p style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: mythSize,
            fontWeight: 600,
            color: '#8E1E1E',
            lineHeight: '1.35',
            textDecoration: 'line-through',
            textDecorationColor: 'rgba(239, 83, 80, 0.6)',
            textDecorationThickness: '2px'
          }}>
            {myth}
          </p>
        </div>

        {/* TRUTH Card */}
        <div className="relative rounded-[32px] border border-[#BFE8CF] bg-white/90 p-8 shadow-xl">
          <div className="flex items-center gap-4 mb-4">
            <div className="w-14 h-14 rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg" style={{ backgroundColor: BRAND.success }}>
              <Check size={30} color="#FFFFFF" strokeWidth={3} />
            </div>
            <span style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: '24px',
              fontWeight: 800,
              color: BRAND.success,
              textTransform: 'uppercase',
              letterSpacing: '2px'
            }}>
              TRUTH
            </span>
          </div>
          <p style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: truthSize,
            fontWeight: 700,
            color: '#1B5E20',
            lineHeight: '1.35'
          }}>
            {truth}
          </p>
        </div>

        {/* Source */}
        {source && (
          <div className="mt-2">
            <span style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: '22px',
              fontWeight: 500,
              color: '#556',
              fontStyle: 'italic'
            }}>
              Source: {source}
            </span>
          </div>
        )}
      </div>
    </SlideLayoutData>
  );
}
