import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Activity, Droplets, Filter } from 'lucide-react';

export function DetoxSlide2() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-24 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.06)' }}></div>
      <div className="absolute bottom-32 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="02/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Activity size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          The Real Detox Machines
        </h2>
        
        {/* Liver */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-3xl p-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '3px solid #207178' }}>
          <div className="flex items-start gap-4 mb-4">
            <Activity size={40} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '36px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.3'
            }}>
              Your Liver: 24/7 Chemical Plant
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Processes everything you consume. Transforms harmful substances into water-soluble compounds through Phase I oxidation and Phase II conjugation.
          </p>
        </div>
        
        {/* Kidneys */}
        <div className="max-w-[900px] mx-auto mb-6 rounded-3xl p-6" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '3px solid #F28C81' }}>
          <div className="flex items-start gap-4 mb-4">
            <Filter size={40} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '36px',
              fontWeight: 700,
              color: '#F28C81',
              lineHeight: '1.3'
            }}>
              Your Kidneys: Precision Filters
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Clean 200 liters of blood daily. Remove waste while keeping essential minerals exactly where they need to be. Millions of tiny units in perfect coordination.
          </p>
        </div>
        
        {/* The verdict */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            No juice can do this. No tea. No supplement.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
