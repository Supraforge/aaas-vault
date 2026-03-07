import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingDown, Wheat, Drumstick } from 'lucide-react';

export function ProteinSlide2() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-24 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.06)' }}></div>
      <div className="absolute bottom-32 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <TrendingDown size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          The Hidden Crisis on Your Plate
        </h2>
        
        {/* The problem */}
        <div className="max-w-[900px] mx-auto mb-6 rounded-3xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center',
            marginBottom: '16px'
          }}>
            India and across Asia:
          </p>
          <div className="flex items-center justify-center gap-4 mb-4">
            <Wheat size={40} color="#F28C81" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '36px',
              fontWeight: 700,
              color: '#F28C81',
              lineHeight: '1.3'
            }}>
              50-70% calories from cereals
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Rice, wheat, and other grains dominate your plate
          </p>
        </div>
        
        {/* The protein gap */}
        <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '3px solid #F28C81' }}>
          <div className="flex items-center justify-center gap-4 mb-4">
            <Drumstick size={40} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '36px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3'
            }}>
              Only 6-9% from protein-rich foods
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Pulses, meat, poultry, and fish are afterthoughts
          </p>
        </div>
        
        {/* The verdict */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            That's not a balanced diet. That's a carbohydrate festival with protein as an afterthought.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
