import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Scale } from 'lucide-react';

export function Slide2() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-tl from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative waves */}
      <svg className="absolute bottom-0 left-0 w-full opacity-5" viewBox="0 0 1080 400" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,100 Q270,200 540,100 T1080,100 L1080,400 L0,400 Z" fill="#207178"/>
      </svg>
      
      {/* Decorative shapes */}
      <div className="absolute top-10 right-10 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.05)' }}></div>
      <div className="absolute top-1/3 left-20 w-[100px] h-[100px]" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)', borderRadius: '30% 70% 70% 30% / 30% 30% 70% 70%' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="02/10" backgroundElements={backgroundElements}>
      <div className="px-12">
        {/* Scale icon */}
        <div className="flex justify-center mb-6">
          <div className="w-24 h-24 rounded-full bg-[#207178] flex items-center justify-center">
            <Scale size={48} color="#F8F9FA" strokeWidth={2.5} />
          </div>
        </div>
        
        {/* Heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '68px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.3',
          textAlign: 'center',
          marginBottom: '30px'
        }}>
          Lose 10 kg if you're obese.
        </h2>
        
        {/* Body text */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '32px',
          fontWeight: 400,
          color: '#333333',
          lineHeight: '1.4',
          textAlign: 'center',
          marginBottom: '40px'
        }}>
          That's an 8 mg/dL LDL drop. But here's what matters more: weight loss amplifies everything else.
        </p>
        
        {/* Progress bar visualization */}
        <div className="max-w-[700px] mx-auto">
          <div className="flex items-center gap-4 mb-4">
            <span style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '24px',
              fontWeight: 500,
              color: '#333333',
              minWidth: '80px'
            }}>
              Before
            </span>
            <div className="flex-1 h-7 bg-[#F8F9FA] rounded-full overflow-hidden border-2 border-[#207178]">
              <div className="h-full bg-[#E63946] rounded-full" style={{ width: '100%' }}></div>
            </div>
          </div>
          <div className="flex items-center gap-4">
            <span style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '24px',
              fontWeight: 500,
              color: '#333333',
              minWidth: '80px'
            }}>
              After
            </span>
            <div className="flex-1 h-7 bg-[#F8F9FA] rounded-full overflow-hidden border-2 border-[#207178]">
              <div className="h-full bg-[#207178] rounded-full" style={{ width: '60%' }}></div>
            </div>
          </div>
          <div className="text-center mt-5" style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#F28C81'
          }}>
            -10 kg = Better Results
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}