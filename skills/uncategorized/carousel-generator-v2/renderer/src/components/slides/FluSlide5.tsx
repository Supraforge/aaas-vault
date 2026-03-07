import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Heart, ShieldCheck, TrendingDown } from 'lucide-react';

export function FluSlide5() {
  const benefits = [
    'Reduced all-cause mortality',
    'Reduced cardiovascular mortality',
    'Lower risk of MACE',
    'Fewer cardiovascular hospitalizations'
  ];

  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-20 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="05/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Title section */}
        <div className="text-center mb-5">
          <div className="flex justify-center mb-4">
            <div className="w-16 h-16 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center">
              <ShieldCheck size={36} color="#F8F9FA" strokeWidth={3} />
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
            Flu Vaccine for Heart Failure Patients
          </h2>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 600,
            color: '#E63946',
            lineHeight: '1.3'
          }}>
            Studies show mortality benefit
          </p>
        </div>
        
        {/* Evidence box */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Meta-analyses and large trials consistently show:
          </p>
        </div>
        
        {/* Benefits list */}
        <div className="space-y-3 mb-4">
          {benefits.map((benefit, index) => (
            <div key={index} className="flex items-center gap-3 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
              <TrendingDown size={28} color="#207178" strokeWidth={3} className="flex-shrink-0" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                {benefit}
              </p>
            </div>
          ))}
        </div>
        
        {/* Bottom highlight */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#F8F9FA',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            In patients with CVD and heart failure, flu vaccination = improved prognosis
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
