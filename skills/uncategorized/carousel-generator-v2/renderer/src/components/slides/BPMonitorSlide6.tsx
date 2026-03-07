import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { ListChecks, Clock, Calculator } from 'lucide-react';

export function BPMonitorSlide6() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-24 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-28 left-20 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="06/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <ListChecks size={44} color="#F8F9FA" strokeWidth={3} />
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
          The Protocol That Actually Works
        </h2>
        
        {/* Protocol steps */}
        <div className="max-w-[900px] mx-auto space-y-4">
          {/* Timing */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
            <div className="flex items-start gap-4 mb-3">
              <Clock size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3'
              }}>
                Twice Daily for 3-7 Days
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Morning before breakfast and medications. Evening before dinner. Not immediately after waking.
            </p>
          </div>
          
          {/* Two measurements */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
            <div className="flex items-start gap-4 mb-3">
              <ListChecks size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3'
              }}>
                Two Measurements Per Session
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Wait 1-2 minutes between measurements. The pause lets your arteries recover from compression.
            </p>
          </div>
          
          {/* Average everything */}
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
            <div className="flex items-start gap-4 mb-3">
              <Calculator size={36} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '32px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.3'
              }}>
                Average ALL Readings
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Don't focus on single readings. Don't throw out outliers. Average everything. This is what matters for diagnosis.
            </p>
          </div>
        </div>
        
        {/* Threshold */}
        <div className="max-w-[900px] mx-auto mt-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Home BP threshold for hypertension: 135/85 mmHg or higher (averaged)
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
