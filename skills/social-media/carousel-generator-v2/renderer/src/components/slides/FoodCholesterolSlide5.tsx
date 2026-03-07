import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Cake, TrendingUp } from 'lucide-react';

export function FoodCholesterolSlide5() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-10 left-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-10 right-10 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="05/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Cake size={44} color="#F8F9FA" strokeWidth={3} />
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
          Sweet Desserts: The Hidden Triglyceride Bomb
        </h2>
        
        {/* Examples */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Jalebi • Gulab jamun • Ice cream • Pastries
          </p>
        </div>
        
        {/* Impact box */}
        <div className="rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <div className="flex items-center justify-center gap-2 mb-3">
            <TrendingUp size={36} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.2'
            }}>
              Fructose at 15-20% of calories
            </p>
          </div>
          <div className="text-center mb-4">
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '56px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.1'
            }}>
              30-40%
            </p>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#333333',
              lineHeight: '1.2'
            }}>
              Triglyceride Jump
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '24px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Enough to move you from normal to high-risk territory
          </p>
        </div>
        
        {/* HDL impact */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            High sugar also drops HDL cholesterol (the good kind you want more of)
          </p>
        </div>
        
        {/* Target */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.2)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Keep added sugar below 10% of energy (ideally ~25g daily for 2,000 calories)
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
