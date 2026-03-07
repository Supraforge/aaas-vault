import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Target, Sun, FlaskConical, Pill, XCircle } from 'lucide-react';

export function VitaminDSlide7() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.07)' }}></div>
      <div className="absolute bottom-28 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="07/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Target size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          What You Actually Need to Do
        </h2>
        
        {/* Action items */}
        <div className="max-w-[900px] mx-auto space-y-4">
          {/* Sunlight */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
            <div className="flex items-start gap-4 mb-3">
              <Sun size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3'
              }}>
                Get Strategic About Sunlight
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Expose arms and legs to direct sunlight for 15-30 minutes between 11 AM-2 PM. Brief, regular exposure without burning.
            </p>
          </div>
          
          {/* Check levels */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
            <div className="flex items-start gap-4 mb-3">
              <FlaskConical size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3'
              }}>
                Check Your Levels If You're at Risk
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Work nights? Northern climate? Darker skin? Rarely go outside? Get a simple blood test.
            </p>
          </div>
          
          {/* Supplement intelligently */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
            <div className="flex items-start gap-4 mb-3">
              <Pill size={36} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3'
              }}>
                Supplement Intelligently, Not Universally
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              600 IU (ages 51-70), 800 IU (over 70). If deficient, you may need higher doses initially—requires testing.
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
