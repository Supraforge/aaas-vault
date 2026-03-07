import React from 'react';
import { BlankSlideLayout } from '../BlankSlideLayout';

export function BlankTemplate() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute bottom-40 left-20 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute top-1/2 right-10 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.06)' }}></div>
      
      {/* Subtle grid pattern */}
      <div className="absolute inset-0 opacity-3" style={{ 
        backgroundImage: 'linear-gradient(#207178 1px, transparent 1px), linear-gradient(90deg, #207178 1px, transparent 1px)',
        backgroundSize: '80px 80px'
      }}></div>
    </>
  );

  return (
    <BlankSlideLayout backgroundElements={backgroundElements}>
      <div className="px-8 h-full flex items-center justify-center">
        {/* Large blank content area for manual writing */}
        <div 
          className="w-full rounded-3xl p-12" 
          style={{ 
            backgroundColor: 'rgba(255, 255, 255, 0.5)',
            border: '2px dashed rgba(32, 113, 120, 0.3)',
            minHeight: '800px'
          }}
        >
          {/* Empty space for manual content */}
        </div>
      </div>
    </BlankSlideLayout>
  );
}
