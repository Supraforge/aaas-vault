import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { AlertTriangle } from 'lucide-react';

export function BPSlide3() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-40 right-40 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.06)' }}></div>
      <div className="absolute bottom-10 left-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      
      {/* Grid pattern */}
      <div className="absolute inset-0 opacity-5" style={{ 
        backgroundImage: 'linear-gradient(#207178 1px, transparent 1px), linear-gradient(90deg, #207178 1px, transparent 1px)',
        backgroundSize: '80px 80px'
      }}></div>
    </>
  );

  const hiddenSources = [
    'Processed foods (bread, cheese, deli meats)',
    'Restaurant/street food',
    'Snacks (chips, crackers, pretzels)',
    'Pickles, sauces, condiments'
  ];

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Reason number badge */}
        <div className="flex justify-center mb-3">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <span style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '42px',
              fontWeight: 700,
              color: '#F8F9FA'
            }}>
              2
            </span>
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '42px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          textAlign: 'center',
          marginBottom: '16px'
        }}>
          Most patients underestimate their sodium intake by 800-1000 mg per day.
        </h2>
        
        {/* Stat callout */}
        <div className="text-center mb-4 rounded-2xl p-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4'
          }}>
            That's massive when you're trying to hit {'<'}2,300 mg daily.
          </p>
        </div>
        
        {/* Arrow */}
        <div className="text-center mb-4">
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#333333',
            lineHeight: '1.3'
          }}>
            High sodium → Uncontrolled BP
          </p>
        </div>
        
        {/* Problem statement */}
        <div className="mb-4">
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            The problem? It's not the salt shaker.
          </p>
        </div>
        
        {/* Hidden sources list */}
        <div className="max-w-[850px] mx-auto rounded-3xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)', border: '3px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#333333',
            lineHeight: '1.4',
            marginBottom: '14px'
          }}>
            Hidden sodium sources:
          </p>
          
          <div className="space-y-2">
            {hiddenSources.map((source, index) => (
              <div key={index} className="flex items-start gap-2">
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#F28C81'
                }}>
                  •
                </span>
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '24px',
                  fontWeight: 500,
                  color: '#333333',
                  lineHeight: '1.4'
                }}>
                  {source}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
