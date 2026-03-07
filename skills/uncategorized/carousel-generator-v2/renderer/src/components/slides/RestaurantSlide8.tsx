import React from 'react';
import { Target, CheckCircle2 } from 'lucide-react';

export function RestaurantSlide8() {
  return (
    <div className="relative w-[1080px] h-[1080px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      <div className="absolute inset-0" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.15), #F8F9FA, rgba(230, 57, 70, 0.15))' }}></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}></div>
      <div className="absolute bottom-20 left-1/4 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 right-1/4 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      
      {/* Food pattern decoration */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <circle cx="200" cy="400" r="60" fill="#E63946" />
        <circle cx="880" cy="500" r="40" fill="#207178" />
        <circle cx="400" cy="700" r="50" fill="#F28C81" />
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
                <Target size={44} color="#F8F9FA" strokeWidth={3} />
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
            <div className="max-w-[900px] mx-auto rounded-3xl p-6 mb-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '3px solid #E63946' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                Your body processes restaurant food differently than home-cooked meals, even at the same calorie count.
              </p>
            </div>
            
            {/* The truth */}
            <div className="max-w-[900px] mx-auto rounded-2xl p-5 mb-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                Refined ingredients, engineered palatability, and hidden fats trigger insulin resistance, inflammation, and cardiovascular risk.
              </p>
            </div>
            
            {/* What to remember */}
            <div className="max-w-[880px] mx-auto mb-4">
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '34px',
                fontWeight: 700,
                color: '#333333',
                lineHeight: '1.3',
                textAlign: 'center'
              }}>
                What to remember:
              </p>
            </div>
            
            {/* Key points */}
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
                  The goal isn't perfection—it's understanding how choices compound
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
                  Choose quality over quantity, protein and fiber over refined carbs
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
                  Preparation methods matter—grilled beats fried every time
                </p>
              </div>
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
                  When you eat out, make it count. Your body will thank you decades from now.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
