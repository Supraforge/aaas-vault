import React from 'react';
import { CheckCircle2, Activity } from 'lucide-react';

export function BPMonitorSlide8() {
  return (
    <div className="relative w-[1080px] h-[1080px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      <div className="absolute inset-0" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.15), #F8F9FA, rgba(230, 57, 70, 0.15))' }}></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}></div>
      <div className="absolute bottom-20 left-1/4 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 right-1/4 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      
      {/* BP wave decoration */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,540 Q270,400 540,540 T1080,540" stroke="#E63946" strokeWidth="8" fill="none" />
        <path d="M0,600 Q270,460 540,600 T1080,600" stroke="#207178" strokeWidth="8" fill="none" />
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
                <Activity size={44} color="#F8F9FA" strokeWidth={3} />
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
              The Bottom Line
            </h2>
            
            {/* Key message */}
            <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '3px solid #E63946' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                Your BP monitor is a precision instrument—but it only works if you use it correctly.
              </p>
            </div>
            
            {/* What matters */}
            <div className="max-w-[900px] mx-auto mb-5">
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#333333',
                lineHeight: '1.3',
                textAlign: 'center'
              }}>
                Every detail matters:
              </p>
            </div>
            
            {/* Checklist */}
            <div className="max-w-[880px] mx-auto space-y-3 mb-6">
              <div className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                <CheckCircle2 size={30} color="#E63946" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  5 minutes rest, no talking, empty bladder
                </p>
              </div>
              
              <div className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                <CheckCircle2 size={30} color="#E63946" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Bare skin, correct cuff size, heart-level positioning
                </p>
              </div>
              
              <div className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                <CheckCircle2 size={30} color="#E63946" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Two readings per session, twice daily for 3-7 days
                </p>
              </div>
              
              <div className="flex items-center gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                <CheckCircle2 size={30} color="#E63946" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Average all readings—that's what matters
                </p>
              </div>
            </div>
            
            {/* Final message */}
            <div className="max-w-[880px] mx-auto rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                Less than 10 minutes twice a day. In exchange: reliable data that can literally save your life.
              </p>
            </div>
            
            {/* Final CTA Box */}
            <div className="max-w-[880px] mx-auto rounded-3xl p-7 shadow-2xl" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
              <div className="text-center">
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '32px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1.4'
                }}>
                  You can only modify what you can accurately measure. Master the technique. Track the trends.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
