import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Cigarette, Wine, AlertTriangle } from 'lucide-react';

export function Slide4() {
  const backgroundElements = (
    <>
      {/* Gradient background with warning tone */}
      <div className="absolute inset-0 bg-gradient-to-tr from-[#E4F1EF] via-[#F8F9FA] to-[#F8F9FA]"></div>
      
      {/* Warning pattern */}
      <div className="absolute top-0 right-0 w-[300px] h-[300px]" style={{ opacity: 0.05 }}>
        <div className="absolute inset-0 bg-[#E63946] rounded-full"></div>
      </div>
      <div className="absolute bottom-0 left-0 w-[250px] h-[250px]" style={{ opacity: 0.05 }}>
        <div className="absolute inset-0 bg-[#E63946] rounded-full"></div>
      </div>
    </>
  );

  const risks = [
    "Coronary disease",
    "Stroke",
    "Heart failure",
    "Cardiomyopathy",
    "Atrial fibrillation",
    "Hypertensive heart disease",
    "Aneurysm"
  ];

  return (
    <SlideLayout slideNumber="04/10" backgroundElements={backgroundElements}>
      <div className="px-10">
        {/* Icon row */}
        <div className="flex justify-center gap-6 mb-6">
          <div className="relative">
            <div className="w-20 h-20 rounded-full bg-[#E63946] flex items-center justify-center">
              <Cigarette size={40} color="#F8F9FA" strokeWidth={2.5} />
            </div>
            <div className="absolute -top-1 -right-1 w-12 h-12 bg-[#E63946] rounded-full flex items-center justify-center border-3 border-[#F8F9FA]">
              <span style={{ fontSize: '24px', color: '#F8F9FA', fontWeight: 700 }}>✕</span>
            </div>
          </div>
          <div className="relative">
            <div className="w-20 h-20 rounded-full bg-[#E63946] flex items-center justify-center">
              <Wine size={40} color="#F8F9FA" strokeWidth={2.5} />
            </div>
            <div className="absolute -top-1 -right-1 w-12 h-12 bg-[#E63946] rounded-full flex items-center justify-center border-3 border-[#F8F9FA]">
              <span style={{ fontSize: '24px', color: '#F8F9FA', fontWeight: 700 }}>✕</span>
            </div>
          </div>
        </div>
        
        {/* Heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '60px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.3',
          textAlign: 'center',
          marginBottom: '20px'
        }}>
          Quit alcohol and smoking completely.
        </h2>
        
        {/* Subheading */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '34px',
          fontWeight: 500,
          color: '#333333',
          lineHeight: '1.4',
          textAlign: 'center',
          marginBottom: '30px'
        }}>
          Not 'cut back'. Not 'moderate drinking'. Complete cessation.
        </p>
        
        {/* Risk list */}
        <div className="max-w-[850px] mx-auto">
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            marginBottom: '16px'
          }}>
            Any alcohol raises risk of:
          </p>
          
          <div className="grid grid-cols-2 gap-4">
            {risks.map((risk, index) => (
              <div key={index} className="flex items-center gap-2 p-3 rounded-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
                <AlertTriangle size={24} color="#E63946" strokeWidth={2.5} />
                <span style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 400,
                  color: '#333333'
                }}>
                  {risk}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}