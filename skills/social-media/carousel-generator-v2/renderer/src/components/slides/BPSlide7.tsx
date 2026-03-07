import React from 'react';
import { Heart, X, CheckCircle2 } from 'lucide-react';

export function BPSlide7() {
  const consequences = [
    'Heart attack',
    'Stroke',
    'Kidney failure requiring dialysis',
    'Blindness'
  ];

  return (
    <div className="relative w-[1080px] h-[1080px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      {/* Vibrant gradient background */}
      <div className="absolute inset-0" style={{ background: 'linear-gradient(to bottom right, rgba(230, 57, 70, 0.15), #F8F9FA, rgba(32, 113, 120, 0.15))' }}></div>
      
      {/* Celebratory circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}></div>
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute bottom-20 left-1/4 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 right-1/4 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}></div>
      
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
            07/08
          </span>
        </div>
        
        {/* Main content area */}
        <div className="flex-1 flex items-center justify-center">
          <div className="w-full px-6">
            {/* Warning box */}
            <div className="max-w-[900px] mx-auto rounded-3xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '36px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                textAlign: 'center',
                marginBottom: '16px'
              }}>
                No. Your 150/100 isn't "normal for you."
              </p>
              
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                Uncontrolled BP leads to:
              </p>
            </div>
            
            {/* Consequences grid */}
            <div className="max-w-[800px] mx-auto grid grid-cols-2 gap-3 mb-5">
              {consequences.map((consequence, index) => (
                <div key={index} className="flex items-center gap-2 p-3 rounded-xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
                  <X size={28} color="#E63946" strokeWidth={3} className="flex-shrink-0" />
                  <span style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '22px',
                    fontWeight: 600,
                    color: '#333333',
                    lineHeight: '1.3'
                  }}>
                    {consequence}
                  </span>
                </div>
              ))}
            </div>
            
            {/* Question */}
            <div className="text-center mb-4">
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#333333',
                lineHeight: '1.4'
              }}>
                You don't want any of these. Right?
              </p>
            </div>
            
            {/* Truth statement */}
            <div className="max-w-[850px] mx-auto rounded-2xl p-4 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                Here's the truth: All of this is preventable.
              </p>
            </div>
            
            {/* Action steps */}
            <div className="max-w-[850px] mx-auto space-y-2 mb-5">
              <div className="flex items-center gap-3 p-4 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                <CheckCircle2 size={30} color="#E63946" strokeWidth={3} />
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '27px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Get a home BP monitor.
                </span>
              </div>
              
              <div className="flex items-center gap-3 p-4 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                <CheckCircle2 size={30} color="#E63946" strokeWidth={3} />
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '27px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Check it 2-3 times weekly. Track it. Act on it.
                </span>
              </div>
            </div>
            
            {/* CTA Box - No footer, integrated call to action */}
            <div className="max-w-[850px] mx-auto rounded-3xl p-8 shadow-2xl" style={{ background: 'linear-gradient(to right, #E63946, #F28C81)' }}>
              <div className="text-center">
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '32px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1.4'
                }}>
                  Take control of your blood pressure, one reading at a time.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
