import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Heart, CheckCircle2 } from 'lucide-react';

export function FoodCholesterolSlide6() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
      <div className="absolute bottom-20 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  const foods = [
    'Vegetables',
    'Fruits',
    'Whole grains',
    'Nuts',
    'Fish',
    'Olive oil'
  ];

  return (
    <SlideLayout slideNumber="06/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Heart size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          What Actually Works to Fix This
        </h2>
        
        {/* Mediterranean result */}
        <div className="rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center',
            marginBottom: '8px'
          }}>
            Mediterranean Eating Pattern
          </p>
          <div className="text-center mb-3">
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '56px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.1'
            }}>
              30%
            </p>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.2'
            }}>
              Reduction in Major Cardiovascular Events
            </p>
          </div>
        </div>
        
        {/* DASH result */}
        <div className="rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '3px solid #F28C81' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#F28C81',
            lineHeight: '1.3',
            textAlign: 'center',
            marginBottom: '8px'
          }}>
            DASH Diet
          </p>
          <div className="text-center mb-3">
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '56px',
              fontWeight: 700,
              color: '#F28C81',
              lineHeight: '1.1'
            }}>
              11 mg/dL
            </p>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.2'
            }}>
              LDL Cholesterol Drop
            </p>
          </div>
        </div>
        
        {/* Focus foods */}
        <div className="rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center',
            marginBottom: '12px'
          }}>
            Both Patterns Emphasize:
          </p>
          <div className="grid grid-cols-2 gap-2">
            {foods.map((food, index) => (
              <div key={index} className="flex items-center gap-2 p-2 rounded-lg" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
                <CheckCircle2 size={20} color="#207178" strokeWidth={3} className="flex-shrink-0" />
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '22px',
                  fontWeight: 600,
                  color: '#333333',
                  lineHeight: '1.2'
                }}>
                  {food}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
