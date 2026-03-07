import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Activity, AlertTriangle } from 'lucide-react';

export function BPMonitorSlide1() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-40 left-10 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
      
      {/* Warning pattern */}
      <svg className="absolute top-0 left-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <pattern id="warning-pattern" x="0" y="0" width="100" height="100" patternUnits="userSpaceOnUse">
          <circle cx="50" cy="50" r="30" fill="#E63946" />
        </pattern>
        <rect width="100%" height="100%" fill="url(#warning-pattern)" />
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
              <Activity size={44} color="#F8F9FA" strokeWidth={3} />
            </div>
            <div className="absolute -top-1 -right-1 w-8 h-8 rounded-full bg-[#E63946] flex items-center justify-center">
              <AlertTriangle size={20} color="#F8F9FA" strokeWidth={3} />
            </div>
          </div>
        </div>
        
        {/* Main heading */}
        <h1 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '50px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '28px'
        }}>
          Your BP Monitor Might Be Lying to You
        </h1>
        
        {/* Subheading */}
        <div className="inline-block px-7 py-5 rounded-2xl mb-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '36px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4'
          }}>
            (And It's Probably Your Fault)
          </p>
        </div>
        
        {/* The problem */}
        <div className="max-w-[900px] mx-auto mb-6 rounded-2xl p-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '34px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4'
          }}>
            Your readings are probably off by 10-40 points
          </p>
        </div>
        
        {/* Bottom impact */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            That's the difference between normal and hypertensive, between no medication and daily pills
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
