import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Bone, Heart, Shield, Dna } from 'lucide-react';

export function ProteinSlide3() {
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
            <Dna size={44} color="#F8F9FA" strokeWidth={3} />
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
          What You're Actually Losing
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
            Protein isn't just for gym bros. Every single cell in your body depends on it.
          </p>
        </div>
        
        {/* What's at risk */}
        <div className="max-w-[900px] mx-auto space-y-4">
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Bone size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Half your protein is in muscles, bones, cartilage, and skin. Low intake = weak bones, muscle loss, sarcopenia
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Heart size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Metabolism slows. Insulin sensitivity drops. Risk of diabetes, stroke, heart attacks climbs
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Dna size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Hormones for stress and sleep? Made from protein. Digestive enzymes? Also protein.
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Shield size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Your immune system's antibodies? You guessed it—protein.
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
