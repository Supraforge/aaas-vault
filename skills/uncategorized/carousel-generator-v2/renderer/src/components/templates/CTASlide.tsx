import React from 'react';
import { SlideLayoutData } from './SlideLayoutData';
import { Heart, Users, Bell } from 'lucide-react';
import doctorPhoto from '@/assets/5e4311be9235ba207024edfb13240abe8cf20f3f.png';
import { BRAND } from '@/theme/brand';

export interface CTASlideData {
  slideNumber: number;
  totalSlides: number;
  name?: string;
  credentials?: string;
  handle?: string;
  valueProposition: string;
  secondaryText?: string;
  followerCount?: string;
  photoPath?: string;
  dimensions?: 'square' | 'portrait';
}

export function CTASlide({
  slideNumber,
  totalSlides,
  name = 'Dr Shailesh Singh',
  credentials = 'Cardiologist | Evidence-Based Medicine',
  handle = '@dr.shailesh.singh',
  valueProposition,
  secondaryText,
  followerCount,
  photoPath,
  dimensions = 'square'
}: CTASlideData) {
  const isPortrait = dimensions === 'portrait';
  const backgroundElements = (
    <>
      {/* Rich gradient background */}
      <div
        className="absolute inset-0"
        style={{
          background: `radial-gradient(circle at 15% 20%, rgba(239, 83, 80, 0.4) 0%, transparent 45%),
            radial-gradient(circle at 85% 15%, rgba(255,255,255,0.14) 0%, transparent 45%),
            linear-gradient(135deg, ${BRAND.primary} 0%, ${BRAND.secondary} 55%, ${BRAND.ink} 100%)`
        }}
      ></div>

      {/* Decorative elements */}
      <div className="absolute -top-10 right-0 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(239, 83, 80, 0.25)' }}></div>
      <div className="absolute bottom-10 left-10 w-[320px] h-[320px] rounded-full" style={{ backgroundColor: 'rgba(255, 255, 255, 0.08)' }}></div>

      {/* Subtle heart pattern */}
      <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 opacity-10">
        <Heart size={400} color="#FFFFFF" strokeWidth={0.5} />
      </div>
    </>
  );

  return (
    <SlideLayoutData
      slideNumber={slideNumber.toString()}
      totalSlides={totalSlides}
      backgroundElements={backgroundElements}
      showFooter={false}
      dimensions={dimensions}
    >
      <div className="px-12 h-full flex flex-col justify-center text-left">
        {/* Profile row */}
        <div className="flex items-center gap-6 mb-10">
          <div className="relative">
            <div
              className="w-[160px] h-[160px] rounded-full overflow-hidden shadow-2xl"
              style={{ border: '6px solid rgba(255, 255, 255, 0.35)' }}
            >
              <img
                src={photoPath || doctorPhoto}
                alt={name}
                className="w-full h-full object-cover"
              />
            </div>
            <div
              className="absolute bottom-2 right-2 w-10 h-10 rounded-full flex items-center justify-center shadow-lg"
              style={{ backgroundColor: BRAND.accent }}
            >
              <Heart size={20} color="#FFFFFF" fill="#FFFFFF" />
            </div>
          </div>
          <div>
            <h2 style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: isPortrait ? '52px' : '46px',
              fontWeight: 800,
              color: '#FFFFFF',
              lineHeight: '1.1',
              marginBottom: '8px'
            }}>
              {name}
            </h2>
            <p style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: isPortrait ? '28px' : '24px',
              fontWeight: 500,
              color: 'rgba(255, 255, 255, 0.85)',
              lineHeight: '1.3'
            }}>
              {credentials}
            </p>
            <p style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: isPortrait ? '26px' : '22px',
              fontWeight: 700,
              color: BRAND.accent,
              lineHeight: '1.3',
              marginTop: '6px'
            }}>
              {handle}
            </p>
          </div>
        </div>

        {/* Value proposition */}
        <div className="max-w-[880px]">
          <h3 style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: isPortrait ? '46px' : '40px',
            fontWeight: 800,
            color: '#FFFFFF',
            lineHeight: '1.25',
            marginBottom: secondaryText ? '18px' : '0'
          }}>
            {valueProposition}
          </h3>
          {secondaryText && (
            <p style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: isPortrait ? '28px' : '24px',
              fontWeight: 500,
              color: 'rgba(255, 255, 255, 0.75)',
              lineHeight: '1.4'
            }}>
              {secondaryText}
            </p>
          )}
        </div>

        {/* CTA row */}
        <div className="mt-10 flex flex-wrap items-center gap-6">
          <div
            className="inline-flex items-center gap-3 rounded-full shadow-xl"
            style={{
              padding: isPortrait ? '18px 36px' : '16px 32px',
              background: `linear-gradient(135deg, ${BRAND.accent} 0%, ${BRAND.alert} 100%)`
            }}
          >
            <Bell size={26} color="#FFFFFF" />
            <span style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: isPortrait ? '28px' : '24px',
              fontWeight: 800,
              color: '#FFFFFF'
            }}>
              Follow for more
            </span>
          </div>

          {followerCount && (
            <div className="flex items-center gap-3 px-5 py-3 rounded-full" style={{ backgroundColor: 'rgba(255, 255, 255, 0.15)' }}>
              <Users size={22} color="#F28C81" />
              <span style={{
                fontFamily: 'Inter, sans-serif',
                fontSize: '22px',
                fontWeight: 600,
                color: '#FFFFFF'
              }}>
                {followerCount} followers
              </span>
            </div>
          )}
        </div>
      </div>
    </SlideLayoutData>
  );
}
