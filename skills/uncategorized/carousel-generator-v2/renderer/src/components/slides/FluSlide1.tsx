import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Heart, AlertTriangle } from 'lucide-react';

export function FluSlide1() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-40 left-10 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
      
      {/* Heart rate line decoration */}
      <svg className="absolute top-0 left-0 w-full h-full opacity-10" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,540 L80,540 L120,400 L160,600 L200,540 L400,540 L440,420 L480,600 L520,540 L700,540 L740,420 L780,600 L820,540 L1080,540" 
          stroke="#E63946" strokeWidth="4" fill="none" />
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="01/08" backgroundElements={backgroundElements}>
      <div className="text-center px-6">
        {/* Alert icon */}
        <div className="flex justify-center mb-5">
          <div className="relative">
            <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
              <AlertTriangle size={44} color="#F8F9FA" strokeWidth={3} />
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
          Did you know a simple flu can trigger a heart attack?
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
            And I'm not talking about rare cases.
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
          Let me show you how influenza impacts your heart and what you can do about it.
        </p>
      </div>
    </SlideLayout>
  );
}
