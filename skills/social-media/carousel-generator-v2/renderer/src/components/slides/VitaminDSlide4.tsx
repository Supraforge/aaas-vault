import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Droplets, Fish, AlertCircle } from 'lucide-react';

export function VitaminDSlide4() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-28 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E4F1EF] flex items-center justify-center shadow-lg">
            <Droplets size={44} color="#F8F9FA" strokeWidth={3} />
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
          The Numbers Don't Lie
        </h2>
        
        {/* Food sources warning */}
        <div className="max-w-[900px] mx-auto mb-6 rounded-3xl p-6" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '3px solid #F28C81' }}>
          <div className="flex items-start gap-4 mb-4">
            <Fish size={38} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#F28C81',
              lineHeight: '1.3'
            }}>
              Even if you're eating foods with Vitamin D...
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Certain fish, fortified cereals, egg yolks—dietary sources alone rarely provide enough.
          </p>
        </div>
        
        {/* Blood level requirements */}
        <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center',
            marginBottom: '16px'
          }}>
            Blood levels between 20-30 ng/mL are considered sufficient.
          </p>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Many people don't even reach this minimum threshold.
          </p>
        </div>
        
        {/* Bottom warning */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <div className="flex items-center gap-4 justify-center">
            <AlertCircle size={36} color="#207178" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '30px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.3'
            }}>
              The data is stark: most people are silently deficient
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
