import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { UtensilsCrossed, AlertTriangle } from 'lucide-react';

export function RestaurantSlide1() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-40 left-10 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
      
      {/* Decorative food pattern */}
      <svg className="absolute top-0 left-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <circle cx="200" cy="200" r="60" fill="#E63946" />
        <circle cx="880" cy="300" r="40" fill="#207178" />
        <circle cx="300" cy="800" r="50" fill="#F28C81" />
        <circle cx="750" cy="750" r="45" fill="#E63946" />
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="01/08" backgroundElements={backgroundElements}>
      <div className="text-center px-6">
        {/* Alert icon */}
        <div className="flex justify-center mb-5">
          <div className="relative">
            <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
              <UtensilsCrossed size={44} color="#F8F9FA" strokeWidth={3} />
            </div>
          </div>
        </div>
        
        {/* Main heading */}
        <h1 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '54px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px'
        }}>
          The Restaurant Trap
        </h1>
        
        {/* Subheading */}
        <div className="inline-block px-7 py-5 rounded-2xl mb-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '34px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Even when you match the calories of a home-cooked meal...
          </p>
        </div>
        
        {/* Bottom text */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '40px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.4'
        }}>
          Your body responds completely differently to restaurant food
        </p>
      </div>
    </SlideLayout>
  );
}
