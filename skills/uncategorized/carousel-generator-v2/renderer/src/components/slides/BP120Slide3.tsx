import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Gauge, CheckCircle2, AlertCircle, XCircle } from 'lucide-react';

export function BP120Slide3() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-24 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.06)' }}></div>
      <div className="absolute bottom-32 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E63946] flex items-center justify-center shadow-lg">
            <Gauge size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '44px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          The 2024 European Guidelines: 3 Simple Categories
        </h2>
        
        {/* Category boxes */}
        <div className="max-w-[880px] mx-auto space-y-4">
          {/* Non-elevated BP */}
          <div className="flex items-start gap-4 p-5 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)', border: '2px solid #207178' }}>
            <CheckCircle2 size={36} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Non-elevated BP: Below 120/70
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                This is where you want to be.
              </p>
            </div>
          </div>
          
          {/* Elevated BP */}
          <div className="flex items-start gap-4 p-5 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
            <AlertCircle size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Elevated BP: 120-139/70-89
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                You're here with a 120/80 reading. Time to pay attention.
              </p>
            </div>
          </div>
          
          {/* Hypertension */}
          <div className="flex items-start gap-4 p-5 rounded-2xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
            <XCircle size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Hypertension: 140/90 or higher
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                This requires immediate action and usually medication.
              </p>
            </div>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
