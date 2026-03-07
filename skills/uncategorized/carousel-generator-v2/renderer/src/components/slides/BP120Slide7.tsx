import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Monitor, Clock, ClipboardList, Home } from 'lucide-react';

export function BP120Slide7() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-28 right-20 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-24 left-16 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="07/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Monitor size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Main heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          Home Monitoring Changes Everything
        </h2>
        
        {/* Key benefit */}
        <div className="max-w-[880px] mx-auto rounded-3xl p-6 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)', border: '3px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '34px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Get a home BP monitor. They cost $30-80 and give you data from your actual life.
          </p>
        </div>
        
        {/* Why home monitoring */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Office readings often run higher due to "white coat syndrome." Home readings show your true baseline.
          </p>
        </div>
        
        {/* How to measure */}
        <div className="max-w-[880px] mx-auto space-y-3">
          <div className="flex items-start gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.12)' }}>
            <Clock size={30} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Measure at the same time each day
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
            <Home size={30} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Sit quietly for 5 minutes before measuring
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-4 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.12)' }}>
            <ClipboardList size={30} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Keep a simple log to help you and your doctor make better decisions
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
