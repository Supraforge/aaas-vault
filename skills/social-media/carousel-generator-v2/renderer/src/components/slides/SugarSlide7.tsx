import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Target, ArrowRight } from 'lucide-react';

export function SugarSlide7() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-16 left-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
      <div className="absolute bottom-16 right-16 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  const changes = [
    {
      from: 'Sugary drinks (soda, juice, energy drinks)',
      to: 'Water, herbal tea, buttermilk'
    },
    {
      from: 'White bread, white rice',
      to: 'Whole grain versions (at least half your intake)'
    },
    {
      from: 'Added sugar foods (biscuits, cakes, sweets)',
      to: 'Less than 10% daily calories (20-25g/day)'
    }
  ];

  return (
    <SlideLayout slideNumber="07/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Target size={44} color="#F8F9FA" strokeWidth={3} />
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
          Starting Point: Reduce the Obvious Sources
        </h2>
        
        {/* Subtitle */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '28px',
          fontWeight: 600,
          color: '#E63946',
          lineHeight: '1.4',
          textAlign: 'center',
          marginBottom: '24px'
        }}>
          You do not need to eliminate carbs. Swap refined for better options.
        </p>
        
        {/* Changes */}
        <div className="space-y-4">
          {changes.map((change, index) => (
            <div key={index} className="rounded-xl p-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
              <div className="flex items-center gap-3 mb-2">
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '20px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  backgroundColor: '#207178',
                  width: '32px',
                  height: '32px',
                  borderRadius: '50%',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}>
                  {index + 1}
                </span>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '22px',
                  fontWeight: 600,
                  color: '#E63946',
                  lineHeight: '1.3',
                  textDecoration: 'line-through'
                }}>
                  {change.from}
                </p>
              </div>
              <div className="flex items-center gap-2 ml-11">
                <ArrowRight size={20} color="#207178" strokeWidth={3} />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '22px',
                  fontWeight: 700,
                  color: '#207178',
                  lineHeight: '1.3'
                }}>
                  {change.to}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </SlideLayout>
  );
}
