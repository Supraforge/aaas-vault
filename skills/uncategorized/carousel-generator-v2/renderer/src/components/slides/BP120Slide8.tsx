import React from 'react';
import { GitBranch, CheckCircle2, Calendar, Home, ClipboardCheck } from 'lucide-react';

export function BP120Slide8() {
  const actionSteps = [
    { icon: Home, text: 'Buy a home blood pressure monitor' },
    { icon: Calendar, text: 'Schedule a follow-up with your doctor in 3 months' },
    { icon: CheckCircle2, text: 'Pick one lifestyle change to start this week (not five—just one)' },
    { icon: ClipboardCheck, text: 'Measure your BP at the same time daily and keep a simple log' }
  ];

  return (
    <div className="relative w-[1080px] h-[1080px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      <div className="absolute inset-0" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.15), #F8F9FA, rgba(230, 57, 70, 0.15))' }}></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}></div>
      <div className="absolute bottom-20 left-1/4 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 right-1/4 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      
      {/* BP monitor wave decoration */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,300 L80,300 L120,200 L160,380 L200,300 L400,300 L440,220 L480,380 L520,300 L700,300 L740,220 L780,380 L820,300 L1080,300" 
          stroke="#E63946" strokeWidth="4" fill="none" />
        <path d="M0,700 L80,700 L120,600 L160,780 L200,700 L400,700 L440,620 L480,780 L520,700 L700,700 L740,620 L780,780 L820,700 L1080,700" 
          stroke="#207178" strokeWidth="4" fill="none" />
      </svg>
      
      {/* Main content container */}
      <div className="relative z-10 flex flex-col h-full p-8">
        {/* Slide number - top left */}
        <div className="mb-4">
          <span style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '42px',
            fontWeight: 700,
            color: '#207178'
          }}>
            08/08
          </span>
        </div>
        
        {/* Main content area */}
        <div className="flex-1 flex items-center justify-center">
          <div className="w-full px-6">
            {/* Icon */}
            <div className="flex justify-center mb-5">
              <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E63946] flex items-center justify-center shadow-lg">
                <GitBranch size={44} color="#F8F9FA" strokeWidth={3} />
              </div>
            </div>
            
            {/* Main heading */}
            <h2 style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '48px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.2',
              marginBottom: '24px',
              textAlign: 'center'
            }}>
              You're at a crossroads
            </h2>
            
            {/* The choice */}
            <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)', border: '3px solid #207178' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                One path leads to gradually worsening BP and eventually medication. The other leads to better numbers, lower risk, and more years of healthy life.
              </p>
            </div>
            
            {/* Truth */}
            <div className="max-w-[900px] mx-auto rounded-2xl p-5 mb-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                Make some changes now while they're still relatively easy, or wait until the problem forces your hand.
              </p>
            </div>
            
            {/* What to do next heading */}
            <div className="max-w-[880px] mx-auto mb-4">
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '36px',
                fontWeight: 700,
                color: '#333333',
                lineHeight: '1.3',
                textAlign: 'center'
              }}>
                What to do next:
              </p>
            </div>
            
            {/* Action steps */}
            <div className="max-w-[880px] mx-auto space-y-3 mb-6">
              {actionSteps.map((step, index) => {
                const Icon = step.icon;
                return (
                  <div key={index} className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                    <CheckCircle2 size={30} color="#E63946" strokeWidth={3} className="flex-shrink-0" />
                    <p style={{ 
                      fontFamily: 'Inter, sans-serif',
                      fontSize: '26px',
                      fontWeight: 700,
                      color: '#333333',
                      lineHeight: '1.3'
                    }}>
                      {step.text}
                    </p>
                  </div>
                );
              })}
            </div>
            
            {/* Final CTA Box */}
            <div className="max-w-[880px] mx-auto rounded-3xl p-8 shadow-2xl" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
              <div className="text-center">
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '34px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1.4'
                }}>
                  Your body just gave you advance notice. Most people don't get that luxury.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
