import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Building2, X, Wine } from 'lucide-react';

export function Slide5() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-bl from-[#F8F9FA] via-[#E4F1EF] to-[#F8F9FA]"></div>
      
      {/* Decorative elements */}
      <div className="absolute top-1/4 right-10 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.05)' }}></div>
      <div className="absolute bottom-1/3 left-16 w-[220px] h-[220px]" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)', borderRadius: '40% 60% 60% 40% / 40% 40% 60% 60%' }}></div>
      
      {/* Subtle grid pattern */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#207178" strokeWidth="1"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid)" />
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="05/10" backgroundElements={backgroundElements}>
      <div className="px-10">
        {/* Organization icons */}
        <div className="flex justify-center gap-8 mb-8">
          <div className="text-center">
            <div className="w-24 h-24 rounded-xl bg-[#207178] flex items-center justify-center mb-3">
              <Building2 size={48} color="#F8F9FA" strokeWidth={2.5} />
            </div>
            <div style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '24px',
              fontWeight: 600,
              color: '#207178'
            }}>
              WHO
            </div>
          </div>
          <div className="text-center">
            <div className="w-24 h-24 rounded-xl bg-[#207178] flex items-center justify-center mb-3">
              <Heart size={48} color="#F8F9FA" strokeWidth={2.5} />
            </div>
            <div style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '22px',
              fontWeight: 600,
              color: '#207178',
              maxWidth: '160px'
            }}>
              World Heart Federation
            </div>
          </div>
        </div>
        
        {/* Main heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '58px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.3',
          textAlign: 'center',
          marginBottom: '35px',
          maxWidth: '900px',
          margin: '0 auto 35px'
        }}>
          WHO and World Heart Federation both say no amount of alcohol is safe.
        </h2>
        
        {/* Visual representation */}
        <div className="flex justify-center items-center gap-8 mb-6">
          <div className="relative">
            <Wine size={70} color="#333333" strokeWidth={2} />
            <div className="absolute inset-0 flex items-center justify-center">
              <X size={90} color="#E63946" strokeWidth={6} />
            </div>
          </div>
        </div>
        
        {/* Body text */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '36px',
          fontWeight: 500,
          color: '#333333',
          lineHeight: '1.4',
          textAlign: 'center',
          maxWidth: '800px',
          margin: '0 auto',
          backgroundColor: 'rgba(255, 255, 255, 0.5)',
          padding: '24px',
          borderRadius: '16px',
          border: '3px solid #E63946'
        }}>
          There's no threshold where it 'helps' your heart.
        </p>
      </div>
    </SlideLayout>
  );
}

function Heart({ size, color, strokeWidth }: { size: number; color: string; strokeWidth: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" 
        stroke={color} 
        strokeWidth={strokeWidth} 
        strokeLinecap="round" 
        strokeLinejoin="round"
      />
    </svg>
  );
}