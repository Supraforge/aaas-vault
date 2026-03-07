import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Repeat, ArrowRight } from 'lucide-react';

export function FoodCholesterolSlide7() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-16 left-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
      <div className="absolute bottom-16 right-16 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  const swaps = [
    {
      from: 'Butter and ghee',
      to: 'Olive oil or vegetable oils'
    },
    {
      from: 'White bread and rice',
      to: 'Whole grain versions'
    },
    {
      from: 'Red and processed meat',
      to: 'Fish, skinless poultry, lean cuts'
    },
    {
      from: 'Full cream milk/yogurt',
      to: 'Skimmed milk and yogurt'
    },
    {
      from: 'Sugary drinks and juices',
      to: 'Water or herbal tea'
    }
  ];

  return (
    <SlideLayout slideNumber="07/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Repeat size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          Five Swaps That Move Your Numbers
        </h2>
        
        {/* Swaps */}
        <div className="space-y-3 mb-5">
          {swaps.map((swap, index) => (
            <div key={index} className="rounded-xl p-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
              <div className="flex items-center gap-2 mb-1">
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '18px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  backgroundColor: '#207178',
                  width: '28px',
                  height: '28px',
                  borderRadius: '50%',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  flexShrink: 0
                }}>
                  {index + 1}
                </span>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '20px',
                  fontWeight: 600,
                  color: '#E63946',
                  lineHeight: '1.2',
                  textDecoration: 'line-through'
                }}>
                  {swap.from}
                </p>
              </div>
              <div className="flex items-center gap-2 ml-9">
                <ArrowRight size={18} color="#207178" strokeWidth={3} />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '20px',
                  fontWeight: 700,
                  color: '#207178',
                  lineHeight: '1.2'
                }}>
                  {swap.to}
                </p>
              </div>
            </div>
          ))}
        </div>
        
        {/* Bottom message */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            You do not need to overhaul everything overnight. Start with one swap this week.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
