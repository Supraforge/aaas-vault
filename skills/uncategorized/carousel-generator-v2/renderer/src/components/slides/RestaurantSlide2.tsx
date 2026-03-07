import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Sparkles, Droplet, Flame } from 'lucide-react';

export function RestaurantSlide2() {
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
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#F28C81] to-[#E63946] flex items-center justify-center shadow-lg">
            <Sparkles size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '44px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          The Hidden Chemistry of Restaurant Food
        </h2>
        
        {/* Intro text */}
        <div className="max-w-[880px] mx-auto mb-6 rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Chefs aren't just cooking—they're engineering palatability for profit
          </p>
        </div>
        
        {/* The three ingredients */}
        <div className="max-w-[880px] mx-auto space-y-4">
          {/* Fat */}
          <div className="flex items-start gap-4 p-5 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
            <Flame size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3',
                marginBottom: '4px'
              }}>
                Fats
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                9 calories per gram. Enhances flavor and texture.
              </p>
            </div>
          </div>
          
          {/* Sugar */}
          <div className="flex items-start gap-4 p-5 rounded-2xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
            <Sparkles size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                marginBottom: '4px'
              }}>
                Sugar
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Creates instant satisfaction and cravings.
              </p>
            </div>
          </div>
          
          {/* Salt */}
          <div className="flex items-start gap-4 p-5 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
            <Droplet size={36} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3',
                marginBottom: '4px'
              }}>
                Salt
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Amplifies taste and makes you want more.
              </p>
            </div>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
