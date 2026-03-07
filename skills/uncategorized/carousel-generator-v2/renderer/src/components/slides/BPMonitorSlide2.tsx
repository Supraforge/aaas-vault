import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Heart, Skull, Activity } from 'lucide-react';

export function BPMonitorSlide2() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-24 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.06)' }}></div>
      <div className="absolute bottom-32 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Heart size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          Why Accuracy Matters More Than You Think
        </h2>
        
        {/* Deaths stat */}
        <div className="max-w-[900px] mx-auto mb-6 rounded-3xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '3px solid #E63946' }}>
          <div className="flex items-center justify-center gap-4 mb-3">
            <Skull size={40} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '38px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3'
            }}>
              9.4 Million Deaths Worldwide
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            High BP is the most important modifiable risk factor for heart disease, stroke, kidney disease, and atrial fibrillation
          </p>
        </div>
        
        {/* Two dangerous scenarios */}
        <div className="max-w-[900px] mx-auto space-y-4">
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#F28C81',
              lineHeight: '1.3',
              marginBottom: '8px'
            }}>
              Scenario 1: Masked Hypertension
            </p>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Home readings look normal, but your actual BP is dangerously high. Your cardiovascular risk silently climbs.
            </p>
          </div>
          
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.3',
              marginBottom: '8px'
            }}>
              Scenario 2: False Diagnosis
            </p>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Diagnosed with hypertension based on flawed measurements. Taking medications you don't actually need.
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
