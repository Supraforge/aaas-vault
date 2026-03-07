import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Stethoscope, Syringe, Pill, XCircle } from 'lucide-react';

export function DetoxSlide7() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.07)' }}></div>
      <div className="absolute bottom-28 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="07/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Stethoscope size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          When Medical Detoxification Actually Exists
        </h2>
        
        {/* Real medical detox */}
        <div className="max-w-[900px] mx-auto space-y-4 mb-5">
          {/* Dialysis */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)' }}>
            <Stethoscope size={32} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Dialysis
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Replaces kidney function when organs fail
              </p>
            </div>
          </div>
          
          {/* Chelation */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <Syringe size={32} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Chelation Therapy
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                Intravenous medications for certain poisonings
              </p>
            </div>
          </div>
          
          {/* Prescription */}
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)' }}>
            <Pill size={32} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <div>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3',
                marginBottom: '6px'
              }}>
                Prescription Drugs
              </p>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 600,
                color: '#333333',
                lineHeight: '1.3'
              }}>
                For diagnosed liver disease under medical oversight
              </p>
            </div>
          </div>
        </div>
        
        {/* What they require */}
        <div className="max-w-[900px] mx-auto rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            These address actual organ failure or toxic overload. They require medical oversight, specialized equipment, prescription medications.
          </p>
        </div>
        
        {/* The truth */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
          <div className="flex items-center justify-center gap-3">
            <XCircle size={36} color="#F28C81" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '30px',
              fontWeight: 700,
              color: '#F28C81',
              lineHeight: '1.3'
            }}>
              They have nothing in common with juice cleanses.
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
