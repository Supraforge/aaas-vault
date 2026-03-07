import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Activity, TrendingDown } from 'lucide-react';

export function BellyFatSlide4() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-16 right-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute bottom-16 left-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  const facts = [
    'At the same BMI, Asians carry higher percentage of body fat',
    'Fat preferentially goes to visceral deposits',
    'South Asians develop diabetes at ~15 lbs lower body weight',
    'The "safe zone" for weight is narrower for you'
  ];

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Activity size={44} color="#F8F9FA" strokeWidth={3} />
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
          Why Asian Bodies Store Fat Differently
        </h2>
        
        {/* Facts list */}
        <div className="space-y-4 mb-6">
          {facts.map((fact, index) => (
            <div key={index} className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
              <div className="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center" style={{ backgroundColor: '#207178' }}>
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '20px',
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
                color: '#333333',
                lineHeight: '1.4'
              }}>
                {fact}
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
            This isn't about genetics being "unfair." It's about understanding your body's blueprint.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
