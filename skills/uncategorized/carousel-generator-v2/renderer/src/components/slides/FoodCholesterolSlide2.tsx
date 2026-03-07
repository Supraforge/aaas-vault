import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Activity, TrendingUp, TrendingDown } from 'lucide-react';

export function FoodCholesterolSlide2() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-10 right-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-10 left-10 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Activity size={44} color="#F8F9FA" strokeWidth={3} />
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
          The Real Story Behind Those Numbers
        </h2>
        
        {/* LDL - Bad */}
        <div className="rounded-2xl p-6 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <div className="flex items-center justify-center gap-3 mb-2">
            <TrendingUp size={32} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.2'
            }}>
              LDL Cholesterol (Bad)
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Delivery trucks that crash into artery walls, leaving deposits that block blood flow to heart and brain
          </p>
        </div>
        
        {/* HDL - Good */}
        <div className="rounded-2xl p-6 mb-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
          <div className="flex items-center justify-center gap-3 mb-2">
            <TrendingDown size={32} color="#207178" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.2'
            }}>
              HDL Cholesterol (Good)
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Garbage trucks that pick up excess cholesterol and haul it back to liver for disposal
          </p>
        </div>
        
        {/* Triglycerides */}
        <div className="rounded-2xl p-6" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '3px solid #F28C81' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#F28C81',
            lineHeight: '1.2',
            textAlign: 'center',
            marginBottom: '8px'
          }}>
            Triglycerides
          </p>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Fat molecules in blood. High numbers mean particles loaded with cholesterol damaging arteries
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
