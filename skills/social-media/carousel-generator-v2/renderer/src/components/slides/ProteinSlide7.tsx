import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Sunrise, Sun, Sunset, Drumstick } from 'lucide-react';

export function ProteinSlide7() {
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
            <Drumstick size={44} color="#F8F9FA" strokeWidth={3} />
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
          Diversify Your Protein Sources
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
            Spread protein across the day—breakfast, lunch, snacks, dinner
          </p>
        </div>
        
        {/* Daily protein map */}
        <div className="max-w-[900px] mx-auto space-y-4">
          {/* Breakfast */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Sunrise size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Breakfast
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Eggs or Greek yogurt
              </p>
            </div>
          </div>
          
          {/* Lunch */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Sun size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Lunch
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Dal with vegetables (3:1 cereal-to-pulse ratio)
              </p>
            </div>
          </div>
          
          {/* Snacks */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <Sun size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Evening Snacks
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Roasted chickpeas or a handful of nuts
              </p>
            </div>
          </div>
          
          {/* Dinner */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Sunset size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Dinner
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Lean chicken, fish, or paneer alongside vegetables
              </p>
            </div>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
