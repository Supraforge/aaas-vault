import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { ChefHat, XCircle, CheckCircle2, Flame } from 'lucide-react';

export function RestaurantSlide7() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.07)' }}></div>
      <div className="absolute bottom-28 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="07/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <ChefHat size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          More Smart Choices When Eating Out
        </h2>
        
        {/* Strategy items */}
        <div className="max-w-[900px] mx-auto space-y-4">
          {/* Preparation methods */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
            <div className="flex items-start gap-4 mb-3">
              <CheckCircle2 size={36} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3'
              }}>
                Choose Preparation Methods Carefully
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Grilled, baked, or steamed dishes have fewer calories and less saturated fat than fried options. Ask how food is prepared.
            </p>
          </div>
          
          {/* Limit culprits */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
            <div className="flex items-start gap-4 mb-3">
              <XCircle size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3'
              }}>
                Limit the Obvious Culprits
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Deep-fried foods, sugary drinks, and dishes swimming in cream or butter should be occasional choices, not regular habits.
            </p>
          </div>
          
          {/* Don't compensate */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
            <div className="flex items-start gap-4 mb-3">
              <Flame size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3'
              }}>
                Don't Try to Compensate by Starving
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Restricting before or after creates a binge pattern that's worse for your metabolism than eating consistently.
            </p>
          </div>
        </div>
        
        {/* Bottom reminder */}
        <div className="max-w-[900px] mx-auto mt-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Bakery items typically contain both trans fats and refined flour—save these for rare occasions.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
