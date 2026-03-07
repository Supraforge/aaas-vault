import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Layers, AlertTriangle } from 'lucide-react';

export function BellyFatSlide3() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-20 left-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-20 right-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  const fatTypes = [
    { 
      name: 'Subcutaneous Fat',
      location: 'Under your skin',
      visibility: 'You can pinch it',
      danger: 'Relatively harmless'
    },
    { 
      name: 'Visceral Fat',
      location: 'Around your organs',
      visibility: 'You cannot see or pinch it',
      danger: 'This is the dangerous one'
    }
  ];

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Layers size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '28px',
          textAlign: 'center'
        }}>
          The Belly Fat You Cannot See
        </h2>
        
        {/* Two types of fat */}
        <div className="space-y-5 mb-6">
          {fatTypes.map((fat, index) => (
            <div key={index} className="rounded-2xl p-6" style={{ backgroundColor: index === 0 ? 'rgba(32, 113, 120, 0.1)' : 'rgba(230, 57, 70, 0.15)', border: index === 1 ? '3px solid #E63946' : 'none' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: index === 0 ? '#207178' : '#E63946',
                lineHeight: '1.3',
                marginBottom: '12px'
              }}>
                {fat.name}
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 500,
                color: '#333333',
                lineHeight: '1.4',
                marginBottom: '6px'
              }}>
                Location: {fat.location}
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 500,
                color: '#333333',
                lineHeight: '1.4',
                marginBottom: '6px'
              }}>
                Visibility: {fat.visibility}
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '26px',
                fontWeight: 600,
                color: index === 0 ? '#333333' : '#E63946',
                lineHeight: '1.4'
              }}>
                Risk: {fat.danger}
              </p>
            </div>
          ))}
        </div>
        
        {/* Key message */}
        <div className="rounded-2xl p-5 text-center" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4'
          }}>
            If you are Asian, your body packs more fat into internal spaces—even when you do not look overweight.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
