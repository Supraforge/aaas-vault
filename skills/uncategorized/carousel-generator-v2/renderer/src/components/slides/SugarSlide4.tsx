import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { AlertCircle, X, Check } from 'lucide-react';

export function SugarSlide4() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-16 right-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute bottom-16 left-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <AlertCircle size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '28px',
          textAlign: 'center'
        }}>
          The Hidden Calorie Trap
        </h2>
        
        {/* Comparison */}
        <div className="grid grid-cols-2 gap-5 mb-6">
          {/* White rice/sugary drink */}
          <div className="rounded-2xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
            <div className="flex justify-center mb-3">
              <X size={40} color="#E63946" strokeWidth={3} />
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3',
              marginBottom: '12px',
              textAlign: 'center'
            }}>
              White Rice / Sugary Drink
            </p>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '22px',
              fontWeight: 500,
              color: '#333333',
              lineHeight: '1.4',
              textAlign: 'center'
            }}>
              Plenty of calories<br/>
              No vitamins<br/>
              No minerals<br/>
              Minimal protein<br/>
              = Stored as fat
            </p>
          </div>
          
          {/* Whole grains + vegetables */}
          <div className="rounded-2xl p-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
            <div className="flex justify-center mb-3">
              <Check size={40} color="#207178" strokeWidth={3} />
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.3',
              marginBottom: '12px',
              textAlign: 'center'
            }}>
              Whole Grains + Vegetables
            </p>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '22px',
              fontWeight: 500,
              color: '#333333',
              lineHeight: '1.4',
              textAlign: 'center'
            }}>
              Body works harder<br/>
              Fiber slows absorption<br/>
              Feel satisfied longer<br/>
              No insulin spike<br/>
              = Better regulation
            </p>
          </div>
        </div>
        
        {/* Bottom message */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            The difference is not just calories. It is what those calories do once they are inside you.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
