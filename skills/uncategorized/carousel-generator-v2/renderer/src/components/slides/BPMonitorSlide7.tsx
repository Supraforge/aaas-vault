import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingUp, Camera, LineChart } from 'lucide-react';

export function BPMonitorSlide7() {
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
            <TrendingUp size={44} color="#F8F9FA" strokeWidth={3} />
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
          Why Tracking Trends Beats Single Readings
        </h2>
        
        {/* Single reading problem */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-3xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '3px solid #E63946' }}>
          <div className="flex items-start gap-4 mb-3">
            <Camera size={38} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3'
            }}>
              A Single BP Measurement Is Almost Meaningless
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Your pressure changes minute to minute based on stress, temperature, digestion, hydration, sleep quality, pain, medications, and random biological variation.
          </p>
        </div>
        
        {/* Why trends work */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
          <div className="flex items-start gap-4 mb-3">
            <LineChart size={36} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.3'
            }}>
              Tracking Trends Reveals Your True BP
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.3'
          }}>
            Multiple measurements over days and weeks average out the random fluctuations. You get a stable picture of your cardiovascular health.
          </p>
        </div>
        
        {/* The advantage */}
        <div className="max-w-[900px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#F28C81',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Home monitoring done correctly predicts heart attack, stroke, and organ damage risk better than office measurements.
          </p>
        </div>
        
        {/* Bottom insight */}
        <div className="max-w-[880px] mx-auto mt-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            You're capturing BP across different times of day, stress levels, activities—a comprehensive view instead of a snapshot.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
