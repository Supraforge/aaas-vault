import React from 'react';
import { SlideLayoutData } from './SlideLayoutData';
import * as LucideIcons from 'lucide-react';
import { BRAND } from '@/theme/brand';

export interface HookSlideData {
  slideNumber: number;
  totalSlides: number;
  headline: string;
  subtitle?: string;
  icon?: string; // Lucide icon name
  theme?: 'teal' | 'coral' | 'red';
  dimensions?: 'square' | 'portrait';
}

function getIcon(iconName: string, size: number = 50, color: string = '#F8F9FA') {
  const Icon = (LucideIcons as any)[iconName];
  if (!Icon) return null;
  return <Icon size={size} color={color} strokeWidth={2.5} />;
}

export function HookSlide({
  slideNumber,
  totalSlides,
  headline,
  subtitle,
  icon,
  theme = 'teal',
  dimensions = 'square'
}: HookSlideData) {
  const themeColors = {
    teal: { accent: BRAND.accent },
    coral: { accent: BRAND.accent },
    red: { accent: BRAND.alert }
  };
  const colors = themeColors[theme];
  const isPortrait = dimensions === 'portrait';
  const headlineSize = isPortrait ? '78px' : '68px';
  const subtitleSize = isPortrait ? '32px' : '28px';

  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div
        className="absolute inset-0"
        style={{
          background: `radial-gradient(circle at 20% 20%, rgba(33, 131, 128, 0.45) 0%, transparent 45%),
            radial-gradient(circle at 85% 15%, rgba(239, 83, 80, 0.35) 0%, transparent 40%),
            linear-gradient(140deg, ${BRAND.primary} 0%, ${BRAND.secondary} 100%)`
        }}
      ></div>

      {/* Accent glow */}
      <div className="absolute -top-10 right-[-40px] w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(239, 83, 80, 0.18)' }}></div>

      {/* Pulse line decoration */}
      <svg className="absolute top-0 left-0 w-full h-full opacity-25" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,560 Q200,560 250,460 T350,560 T450,560 Q600,560 650,460 T750,560 T850,560 Q1000,560 1080,460"
          stroke={BRAND.accent} strokeWidth="4" fill="none" />
      </svg>
    </>
  );

  return (
    <SlideLayoutData
      slideNumber={slideNumber.toString()}
      totalSlides={totalSlides}
      backgroundElements={backgroundElements}
      dimensions={dimensions}
      showFooter={false}
    >
      <div className="h-full flex flex-col items-center justify-center px-12 text-center">
        {/* Icon */}
        {icon && (
          <div className="mb-8">
            <div
              className="w-24 h-24 rounded-3xl flex items-center justify-center shadow-2xl"
              style={{ background: `linear-gradient(135deg, ${BRAND.accent}, ${BRAND.alert})` }}
            >
              {getIcon(icon, 54)}
            </div>
          </div>
        )}

        {/* Main heading */}
        <div className="max-w-[900px]">
          <h1 style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: headlineSize,
            fontWeight: 900,
            color: '#FFFFFF',
            lineHeight: '1.05'
          }}>
            {headline}
          </h1>
        </div>

        {/* Supporting line */}
        {subtitle && (
          <div className="mt-6 max-w-[760px]">
            <p style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: subtitleSize,
              fontWeight: 500,
              color: 'rgba(255, 255, 255, 0.85)',
              lineHeight: '1.3'
            }}>
              {subtitle}
            </p>
          </div>
        )}

        <div className="mt-10 h-[6px] w-[180px] rounded-full" style={{ backgroundColor: colors.accent }}></div>
      </div>
    </SlideLayoutData>
  );
}
