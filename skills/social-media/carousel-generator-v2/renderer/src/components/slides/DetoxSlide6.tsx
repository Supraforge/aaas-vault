import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Activity, Wine, XCircle, CheckCircle2 } from 'lucide-react';

export function DetoxSlide6() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-24 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-28 left-20 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="06/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <CheckCircle2 size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '44px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          What Actually Supports Your Liver and Kidneys
        </h2>
        
        {/* Continued label */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-2xl p-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            (Continued)
          </p>
        </div>
        
        {/* What works */}
        <div className="max-w-[900px] mx-auto space-y-4">
          {/* Movement */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Activity size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Movement Counts
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                150 minutes of moderate activity weekly. Aerobic and resistance training improve fatty liver. Walking, swimming, cycling—pick what you'll do.
              </p>
            </div>
          </div>
          
          {/* Alcohol */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Wine size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Alcohol Limits Protect You
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Under 100g per week (less than 14 units for men, 8 for women). Better yet, minimize further. Excessive drinking causes the fatty liver detox diets claim to prevent.
              </p>
            </div>
          </div>
          
          {/* Supplements */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <XCircle size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Skip Unnecessary Supplements
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Unless you have a documented deficiency, you don't need extra vitamins. Some supplements actually increase health risks.
              </p>
            </div>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}