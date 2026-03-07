import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { ArrowRight } from 'lucide-react';

export function FluSlide4() {
  const steps = [
    'Progressive lipid accumulation',
    'Inflammation within plaque',
    'Plaque instability',
    'Plaque rupture or erosion',
    'Contents exposed to circulation',
    'Coagulation cascade activation',
    'Thrombosis (Type 1 MI)'
  ];

  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-20 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Title */}
        <div className="text-center mb-5">
          <h2 style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '48px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.2',
            marginBottom: '12px'
          }}>
            The Deadly Cascade
          </h2>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 600,
            color: '#E63946',
            lineHeight: '1.3'
          }}>
            From plaque to heart attack
          </p>
        </div>
        
        {/* Step-by-step flow */}
        <div className="space-y-3">
          {steps.map((step, index) => (
            <div key={index}>
              <div className="flex items-center gap-3 p-4 rounded-xl" style={{ 
                backgroundColor: index === steps.length - 1 
                  ? 'rgba(230, 57, 70, 0.2)' 
                  : 'rgba(32, 113, 120, 0.1)',
                border: index === steps.length - 1 ? '2px solid #E63946' : 'none'
              }}>
                <div className="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center" style={{ 
                  backgroundColor: index === steps.length - 1 ? '#E63946' : '#207178'
                }}>
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
                  fontSize: index === steps.length - 1 ? '28px' : '26px',
                  fontWeight: index === steps.length - 1 ? 700 : 600,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  {step}
                </p>
              </div>
              {index < steps.length - 1 && (
                <div className="flex justify-center py-1">
                  <ArrowRight size={24} color="#207178" strokeWidth={3} className="rotate-90" />
                </div>
              )}
            </div>
          ))}
        </div>
        
        {/* Bottom note */}
        <div className="mt-4 text-center">
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '24px',
            fontWeight: 600,
            color: '#207178',
            lineHeight: '1.4'
          }}>
            Inflammation drives the entire process—from progression to rupture
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
