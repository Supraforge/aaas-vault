import React from 'react';
import { SlideLayoutData } from './SlideLayoutData';
import * as LucideIcons from 'lucide-react';
import { BRAND } from '@/theme/brand';

export interface StatSlideData {
  slideNumber: number;
  totalSlides: number;
  stat: string; // e.g., "25%", "3x", "50M"
  label: string;
  context?: string;
  source?: string;
  icon?: string;
  color?: 'teal' | 'coral' | 'green' | 'red';
  dimensions?: 'square' | 'portrait';
}

function getIcon(iconName: string, size: number = 48, color: string = '#F8F9FA') {
  const Icon = (LucideIcons as any)[iconName];
  if (!Icon) return null;
  return <Icon size={size} color={color} strokeWidth={2} />;
}

export function StatSlide({
  slideNumber,
  totalSlides,
  stat,
  label,
  context,
  source,
  icon,
  color = 'teal',
  dimensions = 'square'
}: StatSlideData) {
  const colorSchemes = {
    teal: { primary: BRAND.primary, bg: 'rgba(22, 105, 122, 0.12)', light: '#E4F1EF' },
    coral: { primary: BRAND.accent, bg: 'rgba(239, 83, 80, 0.14)', light: '#FFF0ED' },
    green: { primary: BRAND.success, bg: 'rgba(39, 174, 96, 0.12)', light: '#E8F5E9' },
    red: { primary: BRAND.alert, bg: 'rgba(231, 76, 60, 0.12)', light: '#FFEBEE' }
  };
  const scheme = colorSchemes[color];
  const isPortrait = dimensions === 'portrait';

  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div
        className="absolute inset-0"
        style={{
          background: `radial-gradient(circle at 10% 20%, ${scheme.light} 0%, transparent 45%),
            radial-gradient(circle at 85% 15%, rgba(239, 83, 80, 0.16) 0%, transparent 40%),
            linear-gradient(160deg, #EEF6F5 0%, #FAFBFC 50%, #EEF6F5 100%)`
        }}
      ></div>

      {/* Decorative circles */}
      <div className="absolute top-10 right-10 w-[160px] h-[160px] rounded-full" style={{ backgroundColor: 'rgba(239, 83, 80, 0.1)' }}></div>
      <div className="absolute bottom-24 left-20 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: scheme.bg }}></div>
    </>
  );

  return (
    <SlideLayoutData
      slideNumber={slideNumber.toString()}
      totalSlides={totalSlides}
      backgroundElements={backgroundElements}
      dimensions={dimensions}
    >
      <div
        className={`h-full px-12 ${isPortrait ? 'flex flex-col justify-center gap-6' : 'grid grid-cols-[1.15fr_0.85fr] items-center gap-10'}`}
      >
        {/* Stat block */}
        <div className="rounded-[40px] p-10 shadow-2xl" style={{ background: `linear-gradient(135deg, ${scheme.bg} 0%, rgba(255,255,255,0.95) 60%)` }}>
          <div className="flex items-end gap-4">
            {icon && (
              <div
                className="w-16 h-16 rounded-2xl flex items-center justify-center shadow-lg"
                style={{ backgroundColor: scheme.primary }}
              >
                {getIcon(icon, 36)}
              </div>
            )}
            <div style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: isPortrait ? '138px' : '128px',
              fontWeight: 900,
              color: scheme.primary,
              lineHeight: '0.95'
            }}>
              {stat}
            </div>
          </div>
          <div style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: isPortrait ? '34px' : '30px',
            fontWeight: 700,
            color: BRAND.ink,
            lineHeight: '1.2',
            marginTop: '18px'
          }}>
            {label}
          </div>
        </div>

        {/* Context block */}
        {(context || source) && (
          <div className="rounded-[28px] border border-white/60 bg-white/75 p-8 shadow-lg">
            {context && (
              <p style={{
                fontFamily: 'Inter, sans-serif',
                fontSize: isPortrait ? '30px' : '28px',
                fontWeight: 500,
                color: BRAND.text,
                lineHeight: '1.45',
                marginBottom: source ? '16px' : '0'
              }}>
                {context}
              </p>
            )}
            {source && (
              <p style={{
                fontFamily: 'Inter, sans-serif',
                fontSize: '22px',
                fontWeight: 600,
                color: '#5F7B80',
                fontStyle: 'italic'
              }}>
                {source}
              </p>
            )}
          </div>
        )}
      </div>
    </SlideLayoutData>
  );
}
