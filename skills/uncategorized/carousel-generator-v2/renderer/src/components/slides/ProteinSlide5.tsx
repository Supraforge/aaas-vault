import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { XCircle, TrendingDown, Utensils } from 'lucide-react';

export function ProteinSlide5() {
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
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <XCircle size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          Why Your Current Approach Isn't Working
        </h2>
        
        {/* The myth */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            You might think adding a glass of milk or a small serving of dal does the trick.
          </p>
        </div>
        
        {/* Reality check */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-3xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <div className="flex items-start gap-4 mb-4">
            <Utensils size={38} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3'
            }}>
              A Typical Indian Thali
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            marginBottom: '12px'
          }}>
            Heavy on rice with a small katori of dal gives you maybe 15-20 grams of protein.
          </p>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            You're still 30-40 grams short for the day.
          </p>
        </div>
        
        {/* Higher needs */}
        <div className="max-w-[900px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
          <div className="flex items-start gap-4 mb-3">
            <TrendingDown size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '30px',
              fontWeight: 700,
              color: '#F28C81',
              lineHeight: '1.3'
            }}>
              Losing Weight? Managing Diabetes? Aging?
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3'
          }}>
            You need even more—anywhere from 20-30% of total calories from protein.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
