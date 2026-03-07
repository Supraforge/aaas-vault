import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { X } from 'lucide-react';

export function Slide1() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
      <div className="absolute bottom-40 left-10 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.05)' }}></div>
      
      {/* Pulse line decoration */}
      <svg className="absolute top-0 left-0 w-full h-full opacity-10" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,540 Q200,540 250,450 T350,540 T450,540 Q600,540 650,450 T750,540 T850,540 Q1000,540 1080,450" 
          stroke="#207178" strokeWidth="3" fill="none" />
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="01/10" backgroundElements={backgroundElements}>
      <div className="text-center px-6">
        {/* Main heading with emphasis box */}
        <div className="relative inline-block mb-8">
          <div className="absolute inset-0 rounded-3xl transform rotate-1" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
          <div className="relative p-6">
            <h1 style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '58px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.3',
              maxWidth: '850px',
              margin: '0 auto'
            }}>
              Your cholesterol isn't high because of genetics. It's high because you eat like shit, don't move, and pretend you'll 'start Monday.'
            </h1>
          </div>
        </div>
        
        {/* Crossed DNA icon */}
        <div className="flex justify-center mb-6">
          <div className="relative">
            <div className="w-20 h-20 rounded-full bg-[#F8F9FA] flex items-center justify-center">
              <svg width="50" height="50" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10 15 C10 15, 25 30, 50 15 M10 45 C10 45, 25 30, 50 45" stroke="#207178" strokeWidth="3" strokeLinecap="round"/>
                <circle cx="15" cy="15" r="3" fill="#207178"/>
                <circle cx="45" cy="15" r="3" fill="#207178"/>
                <circle cx="30" cy="30" r="3" fill="#F28C81"/>
                <circle cx="15" cy="45" r="3" fill="#207178"/>
                <circle cx="45" cy="45" r="3" fill="#207178"/>
              </svg>
            </div>
            <X size={36} color="#E63946" strokeWidth={4} className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" />
          </div>
        </div>
        
        {/* Subheading */}
        <div style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '40px',
          fontWeight: 500,
          color: '#333333',
          lineHeight: '1.4'
        }}>
          Here are 3 changes that actually work:
        </div>
      </div>
    </SlideLayout>
  );
}