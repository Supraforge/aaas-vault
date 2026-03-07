import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Sparkles, DollarSign, Activity } from 'lucide-react';

export function DetoxSlide1() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-40 left-10 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.05)' }}></div>
      
      {/* Kidney/liver shape decoration */}
      <svg className="absolute top-0 left-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="300" cy="400" rx="80" ry="120" fill="#207178" />
        <ellipse cx="450" cy="400" rx="80" ry="120" fill="#F28C81" />
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="01/08" backgroundElements={backgroundElements}>
      <div className="text-center px-6">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="relative">
            <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E4F1EF] flex items-center justify-center shadow-lg">
              <Activity size={44} color="#F8F9FA" strokeWidth={3} />
            </div>
            <div className="absolute -top-1 -right-1 w-8 h-8 rounded-full bg-[#E63946] flex items-center justify-center">
              <Sparkles size={20} color="#F8F9FA" strokeWidth={3} />
            </div>
          </div>
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
          Your Body Already Has a $10 Million Detox System
        </h1>
        
        {/* Subheading */}
        <div className="inline-block px-7 py-5 rounded-2xl mb-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '36px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4'
          }}>
            (And It's Been Working Since Birth)
          </p>
        </div>
        
        {/* The marketing */}
        <div className="max-w-[900px] mx-auto mb-6 rounded-2xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            7-day juice cleanses. Charcoal lemonade rituals. $199 liver cleanse kits.
          </p>
        </div>
        
        {/* Bottom truth */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '34px',
            fontWeight: 700,
            color: '#F28C81',
            lineHeight: '1.4'
          }}>
            Here's what nobody's telling you: Your body came equipped with the most sophisticated detox system ever designed.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
