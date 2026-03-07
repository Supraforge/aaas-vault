import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Home, TrendingUp } from 'lucide-react';

export function BPSlide2() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 right-10 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute bottom-20 left-20 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      
      {/* Wave decoration */}
      <svg className="absolute bottom-0 right-0 w-full h-[300px] opacity-5" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,150 Q270,50 540,150 T1080,150 L1080,300 L0,300 Z" fill="#207178"/>
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Reason number badge */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <span style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '42px',
              fontWeight: 700,
              color: '#F8F9FA'
            }}>
              1
            </span>
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          textAlign: 'center',
          marginBottom: '20px'
        }}>
          Most patients have zero idea what their average BP actually is.
        </h2>
        
        {/* Main content box */}
        <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)', border: '3px solid #E63946' }}>
          <div className="flex items-start gap-3 mb-4">
            <Home size={40} color="#E63946" strokeWidth={2.5} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '30px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.4'
            }}>
              The reason? They're not measuring at home.
            </p>
          </div>
          
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 500,
            color: '#333333',
            lineHeight: '1.4',
            marginBottom: '14px'
          }}>
            22-59% of hypertensive patients never use home BP monitors.
          </p>
          
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 500,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            They depend entirely on clinic visits—maybe once every 3-6 months.
          </p>
        </div>
        
        {/* Bottom stat */}
        <div className="text-center rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4'
          }}>
            Meanwhile, office measurements fail to detect 15-25% of hypertension cases.
          </p>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            marginTop: '10px'
          }}>
            No home data = no real control.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
