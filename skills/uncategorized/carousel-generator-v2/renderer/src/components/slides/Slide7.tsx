import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Dumbbell, Heart, Activity } from 'lucide-react';

export function Slide7() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-tr from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative fitness elements */}
      <div className="absolute top-20 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
      <div className="absolute bottom-32 left-20 w-[180px] h-[180px]" style={{ backgroundColor: 'rgba(242, 140, 129, 0.05)', borderRadius: '30% 70% 70% 30% / 30% 30% 70% 70%' }}></div>
      
      {/* Activity wave pattern */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,400 L100,400 L150,300 L200,500 L250,400 L400,400 L450,300 L500,500 L550,400 L700,400 L750,300 L800,500 L850,400 L1080,400" 
          stroke="#207178" strokeWidth="6" fill="none" strokeLinecap="round" strokeLinejoin="round"/>
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="07/10" backgroundElements={backgroundElements}>
      <div className="px-10">
        {/* Fitness icons */}
        <div className="flex justify-center gap-8 mb-8">
          <div className="w-24 h-24 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center transform rotate-12">
            <Dumbbell size={48} color="#F8F9FA" strokeWidth={2.5} />
          </div>
          <div className="w-24 h-24 rounded-full bg-gradient-to-br from-[#F28C81] to-[#207178] flex items-center justify-center transform -rotate-12">
            <Activity size={48} color="#F8F9FA" strokeWidth={2.5} />
          </div>
        </div>
        
        {/* Heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '66px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.3',
          textAlign: 'center',
          marginBottom: '30px'
        }}>
          Exercise 3.5-7 hours per week.
        </h2>
        
        {/* Subheading */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '34px',
          fontWeight: 500,
          color: '#333333',
          lineHeight: '1.4',
          textAlign: 'center',
          marginBottom: '35px'
        }}>
          Mix cardio and strength training. Here are the numbers:
        </p>
        
        {/* Visual tracker */}
        <div className="max-w-[700px] mx-auto">
          <div className="rounded-3xl p-8 border-4 border-[#207178]" style={{ backgroundColor: 'rgba(255, 255, 255, 0.5)' }}>
            <div className="flex justify-between items-center mb-6">
              <div className="text-center flex-1">
                <div className="w-16 h-16 rounded-full bg-[#F28C81] flex items-center justify-center mx-auto mb-2">
                  <Heart size={32} color="#F8F9FA" strokeWidth={2.5} />
                </div>
                <div style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '24px',
                  fontWeight: 600,
                  color: '#333333'
                }}>
                  Cardio
                </div>
              </div>
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '40px',
                fontWeight: 700,
                color: '#207178'
              }}>
                +
              </div>
              <div className="text-center flex-1">
                <div className="w-16 h-16 rounded-full bg-[#207178] flex items-center justify-center mx-auto mb-2">
                  <Dumbbell size={32} color="#F8F9FA" strokeWidth={2.5} />
                </div>
                <div style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '24px',
                  fontWeight: 600,
                  color: '#333333'
                }}>
                  Strength
                </div>
              </div>
            </div>
            
            <div className="text-center pt-5 border-t-2 border-[#207178]">
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#207178'
              }}>
                3.5 - 7 hours/week
              </div>
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 400,
                color: '#333333',
                marginTop: '6px'
              }}>
                for optimal results
              </div>
            </div>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}