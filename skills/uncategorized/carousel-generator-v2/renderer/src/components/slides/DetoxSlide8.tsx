import React from 'react';
import { CheckCircle2, Activity } from 'lucide-react';

export function DetoxSlide8() {
  return (
    <div className="relative w-[1080px] h-[1080px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      <div className="absolute inset-0" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.15), #F8F9FA, rgba(230, 57, 70, 0.15))' }}></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}></div>
      <div className="absolute bottom-20 left-1/4 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 right-1/4 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      
      {/* Kidney/liver decoration */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="300" cy="400" rx="70" ry="110" fill="#207178" />
        <ellipse cx="450" cy="400" rx="70" ry="110" fill="#F28C81" />
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
              <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E4F1EF] flex items-center justify-center shadow-lg">
                <Activity size={44} color="#F8F9FA" strokeWidth={3} />
              </div>
            </div>
            
            {/* Main heading */}
            <h2 style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '46px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.2',
              marginBottom: '20px',
              textAlign: 'center'
            }}>
              The Bottom Line
            </h2>
            
            {/* Key message */}
            <div className="max-w-[900px] mx-auto rounded-3xl p-5 mb-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3',
                textAlign: 'center'
              }}>
                Your liver and kidneys have been detoxifying your body since before your first breath.
              </p>
            </div>
            
            {/* What they don't need */}
            <div className="max-w-[900px] mx-auto rounded-2xl p-4 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '27px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3',
                textAlign: 'center'
              }}>
                They don't need activated charcoal, celery juice, or Instagram-famous tea blends.
              </p>
            </div>
            
            {/* What they need */}
            <div className="max-w-[880px] mx-auto space-y-2 mb-4">
              <div className="flex items-center gap-3 p-3 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                <CheckCircle2 size={26} color="#207178" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '24px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Adequate water • Balanced nutrition • Regular movement
                </p>
              </div>
              
              <div className="flex items-center gap-3 p-3 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
                <CheckCircle2 size={26} color="#207178" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '24px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3'
                }}>
                  Healthy weight • Limited alcohol
                </p>
              </div>
            </div>
            
            {/* Final CTA Box */}
            <div className="max-w-[880px] mx-auto rounded-3xl p-5 shadow-2xl" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
              <div className="text-center">
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '30px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1.3'
                }}>
                  Your body isn't broken. Save your money. Drink water. Eat real food. Move your body.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}