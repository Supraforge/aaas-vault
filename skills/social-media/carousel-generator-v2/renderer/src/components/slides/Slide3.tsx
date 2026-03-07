import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { CheckCircle2, Heart } from 'lucide-react';

export function Slide3() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#F8F9FA] via-[#E4F1EF] to-[#F8F9FA]"></div>
      
      {/* Heart wave pattern */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,300 Q100,250 150,300 T300,300 Q400,250 450,300 T600,300 Q700,250 750,300 T900,300 Q1000,250 1080,300" 
          stroke="#F28C81" strokeWidth="4" fill="none" />
        <path d="M0,500 Q100,450 150,500 T300,500 Q400,450 450,500 T600,500 Q700,450 750,500 T900,500 Q1000,450 1080,500" 
          stroke="#F28C81" strokeWidth="4" fill="none" />
      </svg>
      
      {/* Decorative hearts */}
      <div className="absolute top-20 right-32 opacity-5">
        <Heart size={80} color="#F28C81" fill="#F28C81" />
      </div>
      <div className="absolute bottom-60 left-24 opacity-5">
        <Heart size={60} color="#207178" fill="#207178" />
      </div>
    </>
  );

  const benefits = [
    "Your body processes cholesterol better (improved insulin sensitivity)",
    "HDL goes up by 0.4 mg/dL per kg lost",
    "Triglycerides drop significantly",
    "Diet changes work better",
    "Exercise works better"
  ];

  return (
    <SlideLayout slideNumber="03/10" backgroundElements={backgroundElements}>
      <div className="px-10">
        {/* Heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '62px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.3',
          textAlign: 'center',
          marginBottom: '30px'
        }}>
          When you lose weight:
        </h2>
        
        {/* Benefits list */}
        <div className="space-y-6 max-w-[900px] mx-auto">
          {benefits.map((benefit, index) => (
            <div key={index} className="flex items-start gap-6 p-6 rounded-2xl border-2 border-[#207178]" style={{ backgroundColor: 'rgba(255, 255, 255, 0.4)' }}>
              <div className="flex-shrink-0 mt-1">
                <CheckCircle2 size={36} color="#F28C81" strokeWidth={2.5} />
              </div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 400,
                color: '#333333',
                lineHeight: '1.4',
                margin: 0
              }}>
                {benefit}
              </p>
            </div>
          ))}
        </div>
      </div>
    </SlideLayout>
  );
}