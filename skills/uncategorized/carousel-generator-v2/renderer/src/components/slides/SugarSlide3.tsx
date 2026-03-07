import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Clock, Frown } from 'lucide-react';

export function SugarSlide3() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-20 left-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-20 right-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  const fiberBenefits = [
    'Slows down sugar entering bloodstream',
    'Keeps you feeling full longer'
  ];

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Clock size={44} color="#F8F9FA" strokeWidth={3} />
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
          Why You Are Hungry Again in Two Hours
        </h2>
        
        {/* Problem statement */}
        <div className="rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Refined grains have had their fiber stripped away during processing
          </p>
        </div>
        
        {/* What fiber does */}
        <div className="rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            marginBottom: '16px',
            textAlign: 'center'
          }}>
            What Fiber Does (That You Are Missing):
          </p>
          <div className="space-y-3">
            {fiberBenefits.map((benefit, index) => (
              <div key={index} className="p-4 rounded-xl" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 600,
                  color: '#333333',
                  lineHeight: '1.4',
                  textAlign: 'center'
                }}>
                  {benefit}
                </p>
              </div>
            ))}
          </div>
        </div>
        
        {/* The result */}
        <div className="rounded-2xl p-6 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Quick spike, then crash. Crash triggers hunger. You eat more calories than you need.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
