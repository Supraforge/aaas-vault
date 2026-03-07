import React from 'react';
import { SlideLayoutData } from './SlideLayoutData';
import { TrendingUp, BarChart3, LineChart } from 'lucide-react';
import { BRAND } from '@/theme/brand';

export interface DataSlideData {
  slideNumber: number;
  totalSlides: number;
  title: string;
  chartPath: string; // Path to the Plotly-generated chart PNG
  caption?: string;
  source?: string;
  icon?: string;
  dimensions?: 'square' | 'portrait';
}

function getIcon(iconName: string, size: number = 48, color: string = '#FFFFFF') {
  const iconMap: { [key: string]: any } = {
    'TrendingUp': TrendingUp,
    'BarChart': BarChart3,
    'BarChart3': BarChart3,
    'LineChart': LineChart,
    'Chart': BarChart3,
  };

  const Icon = iconMap[iconName] || BarChart3;
  return <Icon size={size} color={color} strokeWidth={2} />;
}

export function DataSlide({
  slideNumber,
  totalSlides,
  title,
  chartPath,
  caption,
  source,
  icon = 'BarChart3',
  dimensions = 'square'
}: DataSlideData) {
  const isPortrait = dimensions === 'portrait';

  const backgroundElements = (
    <>
      {/* Gradient background optimized for data visualization */}
      <div
        className="absolute inset-0"
        style={{
          background: `radial-gradient(circle at 85% 10%, rgba(242, 140, 129, 0.12) 0%, transparent 40%),
            linear-gradient(165deg, #F8F9FA 0%, #FFFFFF 50%, #EEF6F5 100%)`
        }}
      ></div>

      {/* Decorative corner element */}
      <div className="absolute top-0 right-0 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayoutData
      slideNumber={slideNumber.toString()}
      totalSlides={totalSlides}
      backgroundElements={backgroundElements}
      dimensions={dimensions}
    >
      <div className={`h-full px-12 ${isPortrait ? 'py-6' : 'py-8'} flex flex-col justify-between`}>
        {/* Header with title and icon */}
        <div className="flex items-center gap-4 mb-6">
          <div
            className="w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg"
            style={{ backgroundColor: BRAND.primary }}
          >
            {getIcon(icon, 28)}
          </div>
          <h2 style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: isPortrait ? '40px' : '36px',
            fontWeight: 800,
            color: BRAND.ink,
            lineHeight: '1.2',
            flex: 1
          }}>
            {title}
          </h2>
        </div>

        {/* Chart image container - publication-grade presentation */}
        <div
          className={`flex-1 rounded-[32px] overflow-hidden shadow-2xl ${isPortrait ? 'mb-6' : 'mb-4'}`}
          style={{
            background: 'linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(248,249,250,0.95) 100%)',
            border: '1px solid rgba(32, 113, 120, 0.15)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: isPortrait ? '24px' : '20px'
          }}
        >
          <img
            src={chartPath}
            alt={title}
            style={{
              maxWidth: '100%',
              maxHeight: '100%',
              objectFit: 'contain',
              borderRadius: '12px'
            }}
          />
        </div>

        {/* Caption and source */}
        {(caption || source) && (
          <div className="rounded-[24px] bg-white/80 px-6 py-4 shadow-md">
            {caption && (
              <p style={{
                fontFamily: 'Inter, sans-serif',
                fontSize: isPortrait ? '26px' : '24px',
                fontWeight: 500,
                color: BRAND.text,
                lineHeight: '1.4',
                marginBottom: source ? '8px' : '0'
              }}>
                {caption}
              </p>
            )}
            {source && (
              <p style={{
                fontFamily: 'Inter, sans-serif',
                fontSize: '20px',
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
