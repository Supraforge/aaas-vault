import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { CheckCircle2, Droplets, Scale, Apple } from 'lucide-react';

export function DetoxSlide5() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-32 left-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="05/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E4F1EF] flex items-center justify-center shadow-lg">
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
        
        {/* Intro */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-2xl p-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Skip the $50 juice bottles. Your organs need these instead:
          </p>
        </div>
        
        {/* What works */}
        <div className="max-w-[900px] mx-auto space-y-4">
          {/* Water */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Droplets size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Water Does the Job
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                About 8 glasses daily. Helps kidneys eliminate waste naturally. No lemon, no cayenne needed.
              </p>
            </div>
          </div>
          
          {/* Weight */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Scale size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Weight Management Matters
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                BMI 20-25 kg/m² reduces organ stress. For fatty liver, losing 5-10% body weight improves health more than any supplement.
              </p>
            </div>
          </div>
          
          {/* Mediterranean */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Apple size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Mediterranean Pattern Works
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Strongest evidence for liver and heart health. Vegetables, fruits, whole grains, lean protein, fish. Minimize processed foods.
              </p>
            </div>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
