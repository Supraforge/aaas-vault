import React from 'react';
import { SlideLayoutData } from './SlideLayoutData';
import * as LucideIcons from 'lucide-react';

export interface Tip {
  text: string;
  icon?: string;
}

export interface TipsSlideData {
  slideNumber: number;
  totalSlides: number;
  title: string;
  tips: Tip[];
  dimensions?: 'square' | 'portrait';
}

function getIcon(iconName: string, size: number = 24, color: string = '#207178') {
  const Icon = (LucideIcons as any)[iconName];
  if (!Icon) return null;
  return <Icon size={size} color={color} strokeWidth={2.5} />;
}

export function TipsSlide({
  slideNumber,
  totalSlides,
  title,
  tips,
  dimensions = 'square'
}: TipsSlideData) {
  const backgroundElements = (
    <>
      {/* Clean gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>

      {/* Subtle decorative elements */}
      <div className="absolute top-20 right-10 w-[100px] h-[100px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.03)' }}></div>
      <div className="absolute bottom-32 left-10 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.03)' }}></div>
    </>
  );

  return (
    <SlideLayoutData
      slideNumber={slideNumber.toString()}
      totalSlides={totalSlides}
      backgroundElements={backgroundElements}
      dimensions={dimensions}
    >
      <div className="px-10">
        {/* Title */}
        <h2 style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '40px',
          textAlign: 'center'
        }}>
          {title}
        </h2>

        {/* Tips cards */}
        <div className="space-y-6">
          {tips.map((tip, index) => (
            <div
              key={index}
              className="flex items-start gap-5 p-6 rounded-2xl bg-white shadow-md"
              style={{ border: '2px solid rgba(32, 113, 120, 0.1)' }}
            >
              {/* Number circle */}
              <div
                className="w-14 h-14 rounded-full flex items-center justify-center flex-shrink-0"
                style={{ backgroundColor: '#207178' }}
              >
                {tip.icon ? (
                  getIcon(tip.icon, 28, '#F8F9FA')
                ) : (
                  <span style={{
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '28px',
                    fontWeight: 800,
                    color: '#F8F9FA'
                  }}>
                    {index + 1}
                  </span>
                )}
              </div>

              {/* Tip text */}
              <p style={{
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 500,
                color: '#333333',
                lineHeight: '1.4',
                paddingTop: '6px'
              }}>
                {tip.text}
              </p>
            </div>
          ))}
        </div>
      </div>
    </SlideLayoutData>
  );
}
