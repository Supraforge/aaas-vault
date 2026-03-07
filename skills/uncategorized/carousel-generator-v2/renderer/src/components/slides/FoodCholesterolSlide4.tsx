import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Pizza, AlertOctagon } from 'lucide-react';

export function FoodCholesterolSlide4() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-16 right-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute bottom-16 left-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  const threats = [
    'Saturated fat from cheese and meat',
    'Trans fats if anything was fried',
    'Refined carbs from white flour bun/crust'
  ];

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Pizza size={44} color="#F8F9FA" strokeWidth={3} />
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
          Fast Food: The Triple Combo You Do Not Want
        </h2>
        
        {/* Examples */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Pizza • Burgers • Fried chicken sandwiches
          </p>
        </div>
        
        {/* Triple combo */}
        <div className="rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center',
            marginBottom: '16px'
          }}>
            A Calculated Assault on Your Lipid Profile:
          </p>
          <div className="space-y-3">
            {threats.map((threat, index) => (
              <div key={index} className="flex items-center gap-3 p-4 rounded-xl" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
                <div className="flex-shrink-0 w-10 h-10 rounded-full bg-[#E63946] flex items-center justify-center">
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
                  fontSize: '24px',
                  fontWeight: 600,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  {threat}
                </p>
              </div>
            ))}
          </div>
        </div>
        
        {/* Processed meats warning */}
        <div className="rounded-2xl p-5 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '24px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Processed meats directly linked to increased cardiovascular death
          </p>
        </div>
        
        {/* Bottom message */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.2)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            You are not just raising one number. You are systematically breaking down multiple protective systems.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
