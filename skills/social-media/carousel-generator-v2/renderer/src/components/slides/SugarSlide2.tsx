import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingUp, Zap } from 'lucide-react';

export function SugarSlide2() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-10 right-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-10 left-10 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  const sequence = [
    'You eat refined grains or sugar',
    'Blood glucose shoots up fast',
    'Body releases large amount of insulin',
    'High insulin = fat storage mode activated'
  ];

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <TrendingUp size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '28px',
          textAlign: 'center'
        }}>
          The Insulin Spike Problem
        </h2>
        
        {/* Sequence */}
        <div className="space-y-4 mb-6">
          {sequence.map((step, index) => (
            <div key={index} className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: index === 3 ? 'rgba(230, 57, 70, 0.15)' : 'rgba(32, 113, 120, 0.1)' }}>
              <div className="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center" style={{ backgroundColor: index === 3 ? '#E63946' : '#207178' }}>
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '22px',
                  fontWeight: 700,
                  color: '#F8F9FA'
                }}>
                  {index + 1}
                </span>
              </div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 600,
                color: index === 3 ? '#E63946' : '#333333',
                lineHeight: '1.4'
              }}>
                {step}
              </p>
            </div>
          ))}
        </div>
        
        {/* Bottom emphasis box */}
        <div className="rounded-2xl p-6 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '34px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            High insulin actively tells your body to store fat, especially around organs and belly.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
