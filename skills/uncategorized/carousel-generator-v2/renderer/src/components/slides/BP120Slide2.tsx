import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingUp, AlertTriangle } from 'lucide-react';

export function BP120Slide2() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-32 left-16 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 right-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-6">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <TrendingUp size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Main heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '28px',
          textAlign: 'center'
        }}>
          120/80 isn't the ideal blood pressure.
        </h2>
        
        {/* Key insight box */}
        <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '38px',
            fontWeight: 700,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            It's actually the ceiling—the highest reading you can have before your cardiovascular risk starts climbing.
          </p>
        </div>
        
        {/* Analogy */}
        <div className="max-w-[900px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '34px',
            fontWeight: 600,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Think of it like the speed limit. Just because the sign says 65 mph doesn't mean that's the safest speed to drive.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
