import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingUp, AlertCircle } from 'lucide-react';

export function FluSlide2() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 right-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-20 left-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Title section */}
        <div className="text-center mb-6">
          <div className="flex justify-center mb-4">
            <div className="w-16 h-16 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center">
              <TrendingUp size={36} color="#F8F9FA" strokeWidth={3} />
            </div>
          </div>
          <h2 style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '48px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.2',
            marginBottom: '20px'
          }}>
            The Risk Numbers Are Shocking
          </h2>
        </div>
        
        {/* Main stat box */}
        <div className="rounded-3xl p-6 mb-5 shadow-xl" style={{ background: 'linear-gradient(to right, #E63946, #F28C81)' }}>
          <div className="text-center">
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '72px',
              fontWeight: 700,
              color: '#F8F9FA',
              lineHeight: '1.1',
              marginBottom: '12px'
            }}>
              4×
            </p>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 600,
              color: '#F8F9FA',
              lineHeight: '1.3'
            }}>
              Higher risk of heart attack or stroke after a respiratory infection
            </p>
          </div>
        </div>
        
        {/* Secondary stat */}
        <div className="rounded-2xl p-5 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <div className="flex items-center justify-center gap-3 mb-3">
            <AlertCircle size={32} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '36px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.2'
            }}>
              Highest Risk Period
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            First 3 days after diagnosis
          </p>
        </div>
        
        {/* Bottom text */}
        <div className="text-center">
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#207178',
            lineHeight: '1.4'
          }}>
            This isn't theoretical—it's backed by multiple studies showing a significant association between respiratory infections and acute MI.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
