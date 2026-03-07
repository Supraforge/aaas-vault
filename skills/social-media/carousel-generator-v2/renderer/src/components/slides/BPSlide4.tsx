import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Pill, Clock } from 'lucide-react';

export function BPSlide4() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 left-20 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-40 right-10 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      
      {/* Pulse decoration */}
      <svg className="absolute top-1/2 left-0 w-full h-[200px] opacity-8 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,100 L200,100 L250,40 L300,140 L350,100 L700,100" 
          stroke="#E63946" strokeWidth="3" fill="none" opacity="0.1" />
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Reason number badge */}
        <div className="flex justify-center mb-3">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#F28C81] to-[#E63946] flex items-center justify-center shadow-lg">
            <span style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '42px',
              fontWeight: 700,
              color: '#F8F9FA'
            }}>
              3
            </span>
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '42px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          textAlign: 'center',
          marginBottom: '18px'
        }}>
          Many patients aren't on optimal doses or appropriate medications.
        </h2>
        
        {/* Example callout */}
        <div className="max-w-[900px] mx-auto rounded-3xl p-5 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)', border: '3px solid #E63946' }}>
          <div className="flex items-center gap-3 mb-4">
            <Pill size={38} color="#E63946" strokeWidth={2.5} />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '30px',
              fontWeight: 700,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Atenolol is a perfect example
            </p>
          </div>
          
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 500,
            color: '#333333',
            lineHeight: '1.4',
            marginBottom: '12px'
          }}>
            I see it prescribed frequently.
          </p>
          
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 600,
            color: '#207178',
            lineHeight: '1.4'
          }}>
            If your BP is controlled on it, I won't change it.
          </p>
        </div>
        
        {/* The problem */}
        <div className="text-center mb-4">
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4'
          }}>
            But if you're struggling to hit targets, here's what's happening:
          </p>
        </div>
        
        {/* Key info boxes */}
        <div className="max-w-[850px] mx-auto space-y-3">
          <div className="rounded-2xl p-4 flex items-start gap-3" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
            <Clock size={34} color="#207178" strokeWidth={2.5} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.4'
            }}>
              Atenolol has a <span style={{ color: '#E63946', fontWeight: 700 }}>6-9 hour half-life.</span>
            </p>
          </div>
          
          <div className="rounded-2xl p-4" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.4'
            }}>
              Once-daily dosing leaves gaps in coverage—your BP rises during "trough" periods before the next dose.
            </p>
          </div>
          
          <div className="text-center rounded-2xl p-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.4'
            }}>
              You're only protected for part of the day, not all 24 hours.
            </p>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}
