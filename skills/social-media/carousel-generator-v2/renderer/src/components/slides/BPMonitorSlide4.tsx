import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Shirt, XCircle, AlertCircle } from 'lucide-react';

export function BPMonitorSlide4() {
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
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Shirt size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          The Clothing Mistake That Costs You 40 Points
        </h2>
        
        {/* The wrong way */}
        <div className="max-w-[900px] mx-auto mb-6 rounded-3xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <div className="flex items-start gap-4 mb-4">
            <XCircle size={40} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '34px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3'
            }}>
              Roll up your sleeves? WRONG.
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Bunched fabric creates a tourniquet effect around your upper arm, constricting blood flow and artificially inflating your reading.
          </p>
        </div>
        
        {/* The right way */}
        <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center',
            marginBottom: '16px'
          }}>
            The Fix: Remove Your Shirt or Wear Short Sleeves
          </p>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            The cuff must sit directly on bare skin.
          </p>
        </div>
        
        {/* Error ranges */}
        <div className="max-w-[880px] mx-auto space-y-3">
          <div className="p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              📊 Thin t-shirt: +5-10 points error
            </p>
          </div>
          
          <div className="p-4 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.2)' }}>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              📊 Thick sweater: +20-40 points error
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
