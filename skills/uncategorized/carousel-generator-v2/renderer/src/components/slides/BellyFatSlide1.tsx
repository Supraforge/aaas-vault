import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Scale, AlertCircle } from 'lucide-react';

export function BellyFatSlide1() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-40 left-10 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="01/08" backgroundElements={backgroundElements}>
      <div className="text-center px-6">
        {/* Scale icon */}
        <div className="flex justify-center mb-5">
          <div className="relative">
            <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
              <Scale size={44} color="#F8F9FA" strokeWidth={3} />
            </div>
          </div>
        </div>
        
        {/* Main heading */}
        <h1 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '56px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px'
        }}>
          Why Your Belly Fat is More Dangerous Than You Think
        </h1>
        
        {/* Subheading */}
        <div className="inline-block px-7 py-5 rounded-2xl mb-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '38px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            (If You're Asian)
          </p>
        </div>
        
        {/* Bottom text */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '40px',
          fontWeight: 500,
          color: '#207178',
          lineHeight: '1.4'
        }}>
          Same weight. Same BMI. Different risk.
        </p>
      </div>
    </SlideLayout>
  );
}
