import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingUp, Heart, Skull } from 'lucide-react';

export function RestaurantSlide5() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-32 left-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="05/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <TrendingUp size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          The Real Cost of "Just This Once"
        </h2>
        
        {/* Warning text */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            A dietary pattern heavy in fried foods, processed meats, added fats, and sugary beverages:
          </p>
        </div>
        
        {/* Statistics boxes */}
        <div className="max-w-[900px] mx-auto space-y-4">
          {/* Heart disease */}
          <div className="p-6 rounded-2xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-4">
                <Heart size={42} color="#E63946" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '32px',
                  fontWeight: 700,
                  color: '#E63946',
                  lineHeight: '1.3'
                }}>
                  Heart Disease Risk
                </p>
              </div>
              <div className="px-6 py-3 rounded-xl" style={{ backgroundColor: '#E63946' }}>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '42px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1'
                }}>
                  +56%
                </p>
              </div>
            </div>
          </div>
          
          {/* Stroke */}
          <div className="p-6 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '3px solid #F28C81' }}>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-4">
                <Heart size={42} color="#F28C81" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '32px',
                  fontWeight: 700,
                  color: '#F28C81',
                  lineHeight: '1.3'
                }}>
                  Stroke Risk
                </p>
              </div>
              <div className="px-6 py-3 rounded-xl" style={{ backgroundColor: '#F28C81' }}>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '42px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1'
                }}>
                  +30%
                </p>
              </div>
            </div>
          </div>
          
          {/* Mortality */}
          <div className="p-6 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-4">
                <Skull size={42} color="#207178" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '30px',
                  fontWeight: 700,
                  color: '#207178',
                  lineHeight: '1.3'
                }}>
                  Cardiovascular Mortality (Processed Meat)
                </p>
              </div>
              <div className="px-6 py-3 rounded-xl" style={{ backgroundColor: '#207178' }}>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '42px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1'
                }}>
                  +34%
                </p>
              </div>
            </div>
          </div>
        </div>
        
        {/* Bottom warning */}
        <div className="max-w-[900px] mx-auto mt-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            One meal won't ruin you. But the pattern creates chronic inflammation and metabolic dysfunction.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
