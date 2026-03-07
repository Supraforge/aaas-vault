import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Building2, Car, Shirt, Sun, XCircle } from 'lucide-react';

export function VitaminDSlide3() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.07)' }}></div>
      <div className="absolute bottom-24 left-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <XCircle size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          Why You're Deficient (Even If You Think You're Not)
        </h2>
        
        {/* Intro */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Your body makes Vitamin D when sunlight hits your skin. Except modern life has eliminated this:
          </p>
        </div>
        
        {/* Reasons list */}
        <div className="max-w-[900px] mx-auto space-y-4">
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Building2 size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              You work indoors under fluorescent lights
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Car size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Your commute happens in a metal box
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Shirt size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              You're covered in clothing or sunscreen (which blocks UV rays)
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Sun size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Darker skin requires significantly more sun exposure to produce the same amount
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
