import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { ShieldPlus, Heart, Target } from 'lucide-react';

export function FluSlide7() {
  const reasons = [
    'Strongly recommended for ACS patients (Class I, Level A)',
    'Reduces CV morbidity, CV death, and all-cause death',
    'Lower risk of recurrent MI in high-risk CAD',
    'Prevents future adverse events in established CVD'
  ];

  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 left-10 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-10 right-10 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="07/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Title */}
        <div className="text-center mb-5">
          <div className="flex justify-center mb-4">
            <div className="w-16 h-16 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center">
              <ShieldPlus size={36} color="#F8F9FA" strokeWidth={3} />
            </div>
          </div>
          <h2 style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '46px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.2',
            marginBottom: '16px'
          }}>
            Why Cardiologists Call It "Secondary Prevention"
          </h2>
        </div>
        
        {/* Definition box */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            It prevents recurrent events in patients with established cardiovascular disease
          </p>
        </div>
        
        {/* Evidence points */}
        <div className="space-y-3 mb-4">
          {reasons.map((reason, index) => (
            <div key={index} className="flex items-start gap-3 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
              <Target size={24} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '25px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                {reason}
              </p>
            </div>
          ))}
        </div>
        
        {/* Bottom emphasis */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#F8F9FA',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            If you have heart disease, the flu shot isn't optional—it's essential prevention
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
