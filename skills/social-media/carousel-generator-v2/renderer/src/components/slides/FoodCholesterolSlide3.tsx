import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Flame, X } from 'lucide-react';

export function FoodCholesterolSlide3() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-20 left-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-20 right-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Flame size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          Fried Foods: The Double Threat
        </h2>
        
        {/* Examples */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            French fries • Pakoras • Fried chicken • Samosas
          </p>
        </div>
        
        {/* Threat 1 */}
        <div className="rounded-2xl p-6 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
          <div className="flex items-center gap-3 mb-2">
            <div className="flex-shrink-0 w-12 h-12 rounded-full bg-[#E63946] flex items-center justify-center">
              <span style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 700,
                color: '#F8F9FA'
              }}>
                1
              </span>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.2'
            }}>
              Trans Fats from Hydrogenated Oils
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '24px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Pushes LDL up while dragging HDL down. Worst of both worlds.
          </p>
        </div>
        
        {/* Threat 2 */}
        <div className="rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
          <div className="flex items-center gap-3 mb-2">
            <div className="flex-shrink-0 w-12 h-12 rounded-full bg-[#E63946] flex items-center justify-center">
              <span style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 700,
                color: '#F8F9FA'
              }}>
                2
              </span>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.2'
            }}>
              Saturated Fat from Cooking Oil
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '24px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Single biggest dietary factor that raises LDL cholesterol. Drop from 14% to 6% of calories = measurable LDL drop.
          </p>
        </div>
        
        {/* Bottom message */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.2)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Your arteries pay the price every time you choose fried over grilled.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
