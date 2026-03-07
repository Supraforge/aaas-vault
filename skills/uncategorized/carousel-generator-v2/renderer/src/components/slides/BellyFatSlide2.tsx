import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Users, TrendingUp } from 'lucide-react';

export function BellyFatSlide2() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-10 right-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
      <div className="absolute bottom-10 left-10 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
    </>
  );

  const scenario = [
    { label: 'Patient A (Caucasian)', waist: '92 cm', risk: 'Standard' },
    { label: 'Patient B (Indian)', waist: '92 cm', risk: 'Significantly Higher' }
  ];

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Users size={44} color="#F8F9FA" strokeWidth={3} />
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
          Two Patients Walk Into My Clinic
        </h2>
        
        {/* Patient comparison boxes */}
        <div className="grid grid-cols-2 gap-5 mb-6">
          {scenario.map((patient, index) => (
            <div key={index} className="rounded-2xl p-6" style={{ backgroundColor: index === 0 ? 'rgba(32, 113, 120, 0.1)' : 'rgba(230, 57, 70, 0.1)' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#333333',
                lineHeight: '1.3',
                marginBottom: '12px'
              }}>
                {patient.label}
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 500,
                color: '#333333',
                lineHeight: '1.4',
                marginBottom: '8px'
              }}>
                Waist: {patient.waist}
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 500,
                color: '#333333',
                lineHeight: '1.4'
              }}>
                Weight: 75 kg | BMI: 25.9
              </p>
            </div>
          ))}
        </div>
        
        {/* Key fact box */}
        <div className="rounded-2xl p-6 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '36px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Patient B faces significantly higher risk of diabetes, heart disease, and liver problems—at the exact same measurements.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
