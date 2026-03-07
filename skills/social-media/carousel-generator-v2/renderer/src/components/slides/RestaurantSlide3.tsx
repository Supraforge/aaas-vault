import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { AlertTriangle, Activity, Droplets, TrendingUp } from 'lucide-react';

export function RestaurantSlide3() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.07)' }}></div>
      <div className="absolute bottom-24 left-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <AlertTriangle size={44} color="#F8F9FA" strokeWidth={3} />
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
          What This Does to Your Body
        </h2>
        
        {/* Three dangers */}
        <div className="max-w-[900px] mx-auto space-y-4">
          {/* Insulin spikes */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '2px solid #E63946' }}>
            <div className="flex items-start gap-4 mb-3">
              <TrendingUp size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3'
              }}>
                1. Spikes Your Insulin Sharply
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Refined flour and added sugars shoot blood glucose up. Repeated spikes lead to insulin resistance—the gateway to diabetes.
            </p>
          </div>
          
          {/* Cholesterol damage */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.12)', border: '2px solid #F28C81' }}>
            <div className="flex items-start gap-4 mb-3">
              <Activity size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3'
              }}>
                2. Damages Your Cholesterol Profile
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Trans fats raise LDL (bad) while lowering HDL (good). They trigger inflammation and increase blood clotting risk.
            </p>
          </div>
          
          {/* Blood pressure */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)', border: '2px solid #207178' }}>
            <div className="flex items-start gap-4 mb-3">
              <Droplets size={36} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3'
              }}>
                3. Drives Up Your Blood Pressure
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              High sodium in sauces, marinades, and MSG directly elevates BP and strains your cardiovascular system.
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
