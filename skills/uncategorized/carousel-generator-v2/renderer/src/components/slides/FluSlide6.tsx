import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Syringe, X, AlertCircle } from 'lucide-react';

export function FluSlide6() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="06/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Title */}
        <div className="text-center mb-5">
          <div className="flex justify-center mb-4">
            <div className="w-16 h-16 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center">
              <Syringe size={36} color="#F8F9FA" strokeWidth={3} />
            </div>
          </div>
          <h2 style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '48px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.2',
            marginBottom: '16px'
          }}>
            High-Dose vs Standard Flu Vaccine
          </h2>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3'
          }}>
            Does more = better?
          </p>
        </div>
        
        {/* Study finding - No benefit */}
        <div className="rounded-3xl p-5 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <div className="flex items-center justify-center gap-3 mb-3">
            <X size={40} color="#E63946" strokeWidth={4} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '36px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.2'
            }}>
              No Added Benefit
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            High-dose trivalent showed NO reduction in death or cardiopulmonary hospitalization vs standard-dose quadrivalent
          </p>
        </div>
        
        {/* More adverse effects */}
        <div className="rounded-2xl p-5 mb-4" style={{ backgroundColor: 'rgba(242, 140, 129, 0.2)' }}>
          <div className="flex items-center gap-3 mb-3">
            <AlertCircle size={32} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.2'
            }}>
              The Downside
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            High-dose vaccine reported MORE vaccine-related adverse reactions
          </p>
        </div>
        
        {/* Bottom takeaway */}
        <div className="rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            For cardiac patients: Standard-dose is just as effective with fewer side effects
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
