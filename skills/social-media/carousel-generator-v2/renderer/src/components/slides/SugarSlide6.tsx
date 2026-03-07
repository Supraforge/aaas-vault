import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { CheckCircle2, Wheat } from 'lucide-react';

export function SugarSlide6() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
      <div className="absolute bottom-20 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  const benefits = [
    'Fiber acts like a brake on digestion',
    'Blood sugar rises gradually (no spike)',
    'Insulin release stays moderate',
    'You feel full and satisfied'
  ];

  return (
    <SlideLayout slideNumber="06/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Wheat size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          The Whole Grains Difference
        </h2>
        
        {/* Subtitle */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '28px',
          fontWeight: 600,
          color: '#333333',
          lineHeight: '1.4',
          textAlign: 'center',
          marginBottom: '24px'
        }}>
          Whole grains contain fiber, vitamins, and minerals that were stripped from refined versions
        </p>
        
        {/* Examples */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Whole wheat roti • Brown rice • Millets
          </p>
        </div>
        
        {/* Benefits */}
        <div className="space-y-3 mb-5">
          {benefits.map((benefit, index) => (
            <div key={index} className="flex items-center gap-3 p-4 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
              <CheckCircle2 size={28} color="#207178" strokeWidth={3} className="flex-shrink-0" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                {benefit}
              </p>
            </div>
          ))}
        </div>
        
        {/* Bottom box */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Your body can actually regulate itself the way it is designed to.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
