import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { AlertOctagon, Flame } from 'lucide-react';

export function BellyFatSlide5() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-10 left-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-10 right-10 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.04)' }}></div>
    </>
  );

  const dangers = [
    { icon: '🔥', text: 'Insulin resistance develops' },
    { icon: '⚠️', text: 'Chronic inflammation sets in' },
    { icon: '🫀', text: 'Your liver gets infiltrated with fat' },
    { icon: '📊', text: 'Your lipid profile deteriorates' },
    { icon: '💢', text: 'Blood pressure creeps upward' }
  ];

  return (
    <SlideLayout slideNumber="05/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <AlertOctagon size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          What Visceral Fat Does to Your Body
        </h2>
        
        {/* Subtitle */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '28px',
          fontWeight: 600,
          color: '#207178',
          lineHeight: '1.4',
          textAlign: 'center',
          marginBottom: '24px'
        }}>
          It's not just sitting there—it's metabolically active
        </p>
        
        {/* Dangers list */}
        <div className="space-y-3 mb-5">
          {dangers.map((danger, index) => (
            <div key={index} className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
              <span style={{ fontSize: '32px' }}>{danger.icon}</span>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                {danger.text}
              </p>
            </div>
          ))}
        </div>
        
        {/* Bottom box */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Metabolic syndrome = 2-3× higher CVD risk + 5× higher diabetes risk
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
