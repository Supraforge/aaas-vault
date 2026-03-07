import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Activity, Flame, Droplets } from 'lucide-react';

export function FluSlide3() {
  const mechanisms = [
    { icon: Flame, text: 'Proinflammatory mediators', color: '#E63946' },
    { icon: Activity, text: 'Sympathetic system stimulation', color: '#F28C81' },
    { icon: Droplets, text: 'Coagulation cascade activation', color: '#207178' }
  ];

  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 left-10 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-10 right-10 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Title */}
        <div className="text-center mb-6">
          <h2 style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '46px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.2',
            marginBottom: '16px'
          }}>
            How Does Flu Trigger Heart Attacks?
          </h2>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3'
          }}>
            The mechanism: Inflammation-induced plaque rupture
          </p>
        </div>
        
        {/* The Process Box */}
        <div className="rounded-3xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)', border: '2px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center',
            marginBottom: '16px'
          }}>
            Viral illness triggers systemic biological responses that destabilize existing atherosclerosis
          </p>
        </div>
        
        {/* Three mechanisms */}
        <div className="space-y-3 mb-5">
          {mechanisms.map((mechanism, index) => (
            <div key={index} className="flex items-center gap-4 p-4 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
              <div className="flex-shrink-0 w-14 h-14 rounded-full flex items-center justify-center" style={{ backgroundColor: mechanism.color }}>
                <mechanism.icon size={28} color="#F8F9FA" strokeWidth={3} />
              </div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                {mechanism.text}
              </p>
            </div>
          ))}
        </div>
        
        {/* Result */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#F8F9FA',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            These processes cause rupture of vulnerable atherosclerotic plaques
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
