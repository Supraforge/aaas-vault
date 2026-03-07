import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingDown, AlertCircle } from 'lucide-react';

export function BPSlide5() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-10 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-20 left-40 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      
      {/* Wave decoration */}
      <svg className="absolute top-0 right-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <path d="M1080,0 Q900,200 1080,400 Q900,600 1080,800 L1080,0 Z" fill="#F28C81"/>
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="05/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Reason number badge */}
        <div className="flex justify-center mb-3">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <span style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '42px',
              fontWeight: 700,
              color: '#F8F9FA'
            }}>
              4
            </span>
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '44px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          textAlign: 'center',
          marginBottom: '18px'
        }}>
          The problem doesn't stop there.
        </h2>
        
        {/* Main issue */}
        <div className="max-w-[900px] mx-auto rounded-3xl p-5 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#333333',
            lineHeight: '1.4',
            marginBottom: '12px'
          }}>
            Primary care physicians significantly under-prescribe and underdose antihypertensives.
          </p>
          
          <div className="flex items-start gap-3">
            <AlertCircle size={34} color="#E63946" strokeWidth={2.5} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '25px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.4'
            }}>
              Multiple studies show evidence of <span style={{ color: '#E63946', fontWeight: 700 }}>"therapeutic inertia"</span>—failure to intensify treatment when BP stays elevated.
            </p>
          </div>
        </div>
        
        {/* What this means */}
        <div className="mb-3">
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            What this means:
          </p>
        </div>
        
        {/* Consequences */}
        <div className="max-w-[850px] mx-auto rounded-3xl p-5 mb-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            marginBottom: '10px'
          }}>
            Patients remain on inadequate medication regimens for extended periods despite not reaching targets.
          </p>
        </div>
        
        {/* The result */}
        <div className="max-w-[800px] mx-auto space-y-3">
          <div className="flex items-center gap-3">
            <TrendingDown size={32} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.4'
            }}>
              Your BP stays high.
            </p>
          </div>
          
          <div className="flex items-center gap-3">
            <TrendingDown size={32} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.4'
            }}>
              Your doctor doesn't adjust.
            </p>
          </div>
          
          <div className="flex items-center gap-3">
            <TrendingDown size={32} color="#E63946" strokeWidth={3} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.4'
            }}>
              Months pass. Damage accumulates.
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
