import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { AlertTriangle, Skull, Brain } from 'lucide-react';

export function DetoxSlide4() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-28 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <AlertTriangle size={44} color="#F8F9FA" strokeWidth={3} />
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
          The Hidden Dangers Nobody Mentions
        </h2>
        
        {/* Rapid weight loss */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-3xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <div className="flex items-start gap-4 mb-3">
            <AlertTriangle size={38} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3'
            }}>
              Extreme Detox Regimens Carry Real Risks
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Very-low-calorie cleanses aren't safe for pregnant women, children, or people with kidney disease. Require medical supervision when used.
          </p>
        </div>
        
        {/* Nutrient deficiencies */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
          <div className="flex items-start gap-4 mb-3">
            <Skull size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '30px',
              fontWeight: 700,
              color: '#F28C81',
              lineHeight: '1.3'
            }}>
              Severe Calorie Restriction
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3'
          }}>
            Missing essential amino acids, fatty acids, and micronutrients. Can lead to anemia, affect memory and cognition, increase chronic disease risk.
          </p>
        </div>
        
        {/* Kidney damage */}
        <div className="max-w-[900px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
          <div className="flex items-start gap-4 mb-3">
            <Brain size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '30px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3'
            }}>
              High-Protein "Detox" Plans
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3'
          }}>
            Can damage your kidneys. Excessive restriction taxes the organs you're supposedly helping.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
