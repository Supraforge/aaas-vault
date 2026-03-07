import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingDown, CheckCircle2 } from 'lucide-react';

export function BellyFatSlide7() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-16 left-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
      <div className="absolute bottom-16 right-16 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  const strategies = [
    'Create a 300-500 calorie deficit daily',
    'Adopt a Mediterranean eating pattern',
    'Brisk walk 25-30 km per week',
    'Both aerobic + resistance training work'
  ];

  return (
    <SlideLayout slideNumber="07/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <TrendingDown size={44} color="#F8F9FA" strokeWidth={3} />
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
          What Actually Reduces Visceral Fat
        </h2>
        
        {/* Good news box */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Good news: Visceral fat responds well to lifestyle changes
          </p>
        </div>
        
        {/* Weight loss stat */}
        <div className="rounded-2xl p-5 mb-5 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Just 3-5% weight loss produces measurable improvements
          </p>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '24px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center',
            marginTop: '8px'
          }}>
            (That's 3.5-4 kg if you weigh 70-80 kg—Achievable!)
          </p>
        </div>
        
        {/* Strategies */}
        <div className="space-y-3">
          {strategies.map((strategy, index) => (
            <div key={index} className="flex items-center gap-3 p-4 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
              <CheckCircle2 size={28} color="#207178" strokeWidth={3} className="flex-shrink-0" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                {strategy}
              </p>
            </div>
          ))}
        </div>
      </div>
    </SlideLayout>
  );
}
