import React from 'react';
import { ChevronRight } from 'lucide-react';
import { BRAND } from '@/theme/brand';
import doctorPhoto from '@/assets/5e4311be9235ba207024edfb13240abe8cf20f3f.png';

export interface SlideLayoutProps {
  slideNumber: string;
  totalSlides?: number;
  children: React.ReactNode;
  backgroundElements?: React.ReactNode;
  showFooter?: boolean;
  dimensions?: 'square' | 'portrait';
  authorName?: string;
  authorHandle?: string;
  authorPhoto?: string;
}

export function SlideLayoutData({
  slideNumber,
  totalSlides,
  children,
  backgroundElements,
  showFooter = true,
  dimensions = 'square',
  authorName = 'Dr Shailesh Singh',
  authorHandle = '@dr.shailesh.singh',
  authorPhoto
}: SlideLayoutProps) {
  const height = dimensions === 'square' ? 1080 : 1350;
  const formattedNumber = totalSlides
    ? `${slideNumber.toString().padStart(2, '0')}/${totalSlides.toString().padStart(2, '0')}`
    : slideNumber;

  return (
    <div
      className="relative bg-[#E4F1EF] overflow-hidden flex flex-col"
      style={{ width: 1080, height }}
    >
      {/* Background decorative elements */}
      {backgroundElements}

      {/* Main content container */}
      <div className="relative z-10 flex flex-col h-full p-8">
        {/* Slide number - top left */}
        <div className="mb-4">
          <span style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: '42px',
            fontWeight: 700,
            color: BRAND.primary
          }}>
            {formattedNumber}
          </span>
        </div>

        {/* Main content area */}
        <div className="flex-1 flex items-center justify-center overflow-hidden">
          <div className="w-full">
            {children}
          </div>
        </div>

        {/* Footer */}
        {showFooter && (
          <div className="mt-4 flex-shrink-0">
            {/* Accent line separator */}
            <div className="w-full h-[2px] mb-4" style={{ backgroundColor: BRAND.accent }}></div>

            <div className="flex items-center justify-between">
              {/* Left: Profile and info */}
              <div className="flex items-center gap-3">
                <img
                  src={authorPhoto || doctorPhoto}
                  alt={authorName}
                  className="w-[60px] h-[60px] rounded-full object-cover flex-shrink-0"
                />
                <div>
                  <div style={{
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '26px',
                    fontWeight: 700,
                    color: BRAND.ink,
                    lineHeight: '1.2'
                  }}>
                    {authorName}
                  </div>
                  <div style={{
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '22px',
                    fontWeight: 400,
                    color: BRAND.text,
                    lineHeight: '1.2'
                  }}>
                    {authorHandle}
                  </div>
                </div>
              </div>

              {/* Right: Arrow indicators */}
              <div className="flex gap-1 flex-shrink-0">
                <ChevronRight size={24} color={BRAND.primary} strokeWidth={3} />
                <ChevronRight size={24} color={BRAND.primary} strokeWidth={3} />
                <ChevronRight size={24} color={BRAND.primary} strokeWidth={3} />
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
