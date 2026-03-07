import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Ruler, Target } from 'lucide-react';

export function BellyFatSlide6() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
      <div className="absolute bottom-20 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  const thresholds = [
    { gender: 'Men', threshold: '90 cm (35.5 inches)' },
    { gender: 'Women', threshold: '80 cm (31.5 inches)' }
  ];

  return (
    <SlideLayout slideNumber="06/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Ruler size={44} color="#F8F9FA" strokeWidth={3} />
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
          The Measurement That Matters More Than Your Weight
        </h2>
        
        {/* Subtitle */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '30px',
          fontWeight: 600,
          color: '#333333',
          lineHeight: '1.4',
          textAlign: 'center',
          marginBottom: '24px'
        }}>
          Waist circumference predicts cardiometabolic risk better than BMI
        </p>
        
        {/* Thresholds for Asian populations */}
        <div className="rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center',
            marginBottom: '20px'
          }}>
            Asian Population Thresholds:
          </p>
          <div className="space-y-4">
            {thresholds.map((item, index) => (
              <div key={index} className="flex items-center justify-between p-4 rounded-xl" style={{ backgroundColor: 'rgba(255, 255, 255, 0.7)' }}>
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '30px',
                  fontWeight: 700,
                  color: '#333333'
                }}>
                  {item.gender}:
                </span>
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '30px',
                  fontWeight: 700,
                  color: '#E63946'
                }}>
                  {item.threshold}
                </span>
              </div>
            ))}
          </div>
        </div>
        
        {/* Comparison note */}
        <div className="rounded-xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Western cutoffs: 102 cm (men) / 88 cm (women)<br/>
            <span style={{ color: '#E63946', fontWeight: 700 }}>Metabolic complications develop at lower thresholds in Asian bodies</span>
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
