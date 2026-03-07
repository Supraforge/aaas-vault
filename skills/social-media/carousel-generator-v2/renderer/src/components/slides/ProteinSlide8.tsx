import React from 'react';
import { CheckCircle2, Drumstick } from 'lucide-react';

export function ProteinSlide8() {
  return (
    <div className="relative w-[1080px] h-[1080px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      <div className="absolute inset-0" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.15), #F8F9FA, rgba(230, 57, 70, 0.15))' }}></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}></div>
      <div className="absolute bottom-20 left-1/4 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 right-1/4 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      
      {/* Protein molecule decoration */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <circle cx="200" cy="300" r="35" fill="#207178" />
        <circle cx="300" cy="200" r="35" fill="#F28C81" />
        <circle cx="400" cy="300" r="35" fill="#E63946" />
        <circle cx="300" cy="400" r="35" fill="#207178" />
        <line x1="200" y1="300" x2="300" y2="200" stroke="#333333" strokeWidth="4" />
        <line x1="300" y1="200" x2="400" y2="300" stroke="#333333" strokeWidth="4" />
        <line x1="400" y1="300" x2="300" y2="400" stroke="#333333" strokeWidth="4" />
        <line x1="300" y1="400" x2="200" y2="300" stroke="#333333" strokeWidth="4" />
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
              <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
                <Drumstick size={44} color="#F8F9FA" strokeWidth={3} />
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
              Starting Today
            </h2>
            
            {/* Key message */}
            <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '34px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                You don't need to track macros obsessively or weigh every morsel.
              </p>
            </div>
            
            {/* The one question */}
            <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '3px solid #E63946' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '36px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.4',
                textAlign: 'center',
                marginBottom: '16px'
              }}>
                Just ask yourself at each meal:
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '42px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                textAlign: 'center'
              }}>
                "Where's my protein?"
              </p>
            </div>
            
            {/* The problem indicator */}
            <div className="max-w-[880px] mx-auto rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#333333',
                lineHeight: '1.3',
                textAlign: 'center'
              }}>
                If the answer is "nowhere" or "just a little dal," you've identified the problem.
              </p>
            </div>
            
            {/* What's waiting */}
            <div className="max-w-[880px] mx-auto space-y-3 mb-5">
              <div className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)' }}>
                <CheckCircle2 size={30} color="#207178" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Your muscles need it
                </p>
              </div>
              
              <div className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)' }}>
                <CheckCircle2 size={30} color="#207178" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Your metabolism needs it
                </p>
              </div>
              
              <div className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)' }}>
                <CheckCircle2 size={30} color="#207178" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Your hormones and immune system need it
                </p>
              </div>
            </div>
            
            {/* Final CTA Box */}
            <div className="max-w-[880px] mx-auto rounded-3xl p-7 shadow-2xl" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
              <div className="text-center">
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '34px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1.4'
                }}>
                  The question is: Will you fix it?
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
