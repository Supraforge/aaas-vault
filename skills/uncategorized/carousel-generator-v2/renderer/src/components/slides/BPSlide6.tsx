import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Moon, Activity } from 'lucide-react';

export function BPSlide6() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 left-10 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute bottom-10 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      
      {/* Diagonal lines decoration */}
      <div className="absolute inset-0 opacity-5" style={{ 
        backgroundImage: 'repeating-linear-gradient(45deg, #207178 0, #207178 2px, transparent 2px, transparent 40px)',
      }}></div>
    </>
  );

  const conditions = [
    {
      name: 'Obstructive sleep apnea',
      stat: '30-50% of hypertensive patients have it'
    },
    {
      name: 'Chronic kidney disease',
      stat: 'accounts for ~5% of hypertension cases'
    },
    {
      name: 'Obesity',
      stat: 'responsible for 65-78% of primary hypertension cases'
    }
  ];

  return (
    <SlideLayout slideNumber="06/08" backgroundElements={backgroundElements}>
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
              5
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
          Sometimes it's not the medication, the doctor, or the diet.
        </h2>
        
        {/* Intro */}
        <div className="text-center mb-4">
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Your BP might be elevated because of an underlying condition:
          </p>
        </div>
        
        {/* Conditions list */}
        <div className="max-w-[900px] mx-auto space-y-3 mb-4">
          {conditions.map((condition, index) => (
            <div key={index} className="rounded-2xl p-4" style={{ backgroundColor: index === 0 ? 'rgba(230, 57, 70, 0.1)' : index === 1 ? 'rgba(32, 113, 120, 0.1)' : 'rgba(242, 140, 129, 0.15)' }}>
              <div className="flex items-start gap-3 mb-2">
                {index === 0 ? (
                  <Moon size={34} color="#E63946" strokeWidth={2.5} className="flex-shrink-0" />
                ) : (
                  <Activity size={34} color={index === 1 ? '#207178' : '#F28C81'} strokeWidth={2.5} className="flex-shrink-0" />
                )}
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '28px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  {condition.name}
                </p>
              </div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 600,
                color: index === 0 ? '#E63946' : index === 1 ? '#207178' : '#F28C81',
                lineHeight: '1.4',
                paddingLeft: '48px'
              }}>
                {condition.stat}
              </p>
            </div>
          ))}
        </div>
        
        {/* Bottom message */}
        <div className="max-w-[850px] mx-auto rounded-3xl p-5 text-center" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Without addressing these, you're stacking medications while the root problem keeps your BP elevated.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
