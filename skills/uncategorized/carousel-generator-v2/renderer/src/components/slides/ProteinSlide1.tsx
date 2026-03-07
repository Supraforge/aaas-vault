import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { AlertTriangle, Drumstick } from 'lucide-react';

export function ProteinSlide1() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-40 left-10 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
      
      {/* Protein molecule decoration */}
      <svg className="absolute top-0 left-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <circle cx="200" cy="300" r="40" fill="#207178" />
        <circle cx="300" cy="200" r="40" fill="#F28C81" />
        <circle cx="400" cy="300" r="40" fill="#E63946" />
        <circle cx="300" cy="400" r="40" fill="#207178" />
        <line x1="200" y1="300" x2="300" y2="200" stroke="#333333" strokeWidth="4" />
        <line x1="300" y1="200" x2="400" y2="300" stroke="#333333" strokeWidth="4" />
        <line x1="400" y1="300" x2="300" y2="400" stroke="#333333" strokeWidth="4" />
        <line x1="300" y1="400" x2="200" y2="300" stroke="#333333" strokeWidth="4" />
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
              <Drumstick size={44} color="#F8F9FA" strokeWidth={3} />
            </div>
            <div className="absolute -top-1 -right-1 w-8 h-8 rounded-full bg-[#E63946] flex items-center justify-center">
              <AlertTriangle size={20} color="#F8F9FA" strokeWidth={3} />
            </div>
          </div>
        </div>
        
        {/* Main stat */}
        <div className="inline-block px-7 py-5 rounded-3xl mb-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '4px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '56px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.2'
          }}>
            90% of People
          </p>
        </div>
        
        {/* Main heading */}
        <h1 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '24px'
        }}>
          Are Protein Deficient
        </h1>
        
        {/* What you're tracking */}
        <div className="max-w-[900px] mx-auto mb-6 rounded-2xl p-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            You're tracking calories. Watching carbs. Maybe counting steps.
          </p>
        </div>
        
        {/* Bottom impact */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '34px',
            fontWeight: 700,
            color: '#F28C81',
            lineHeight: '1.4'
          }}>
            But you're missing the one macronutrient that controls muscle mass, metabolism, hormones, and immunity
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
