import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Calendar, TrendingDown, CheckCircle2, Pill } from 'lucide-react';

export function BP120Slide6() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 left-24 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.07)' }}></div>
      <div className="absolute bottom-20 right-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="06/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E63946] flex items-center justify-center shadow-lg">
            <Calendar size={44} color="#F8F9FA" strokeWidth={3} />
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
          The Three-Month Window
        </h2>
        
        {/* Guidelines recommendation */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Most guidelines recommend for elevated BP with no other major risk factors:
          </p>
        </div>
        
        {/* Two pathways */}
        <div className="max-w-[880px] mx-auto space-y-4">
          {/* Path 1: Success */}
          <div className="rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)', border: '2px solid #207178' }}>
            <div className="flex items-start gap-4">
              <CheckCircle2 size={36} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <div>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '30px',
                  fontWeight: 700,
                  color: '#207178',
                  lineHeight: '1.3',
                  marginBottom: '8px'
                }}>
                  If numbers drop below 120/70:
                </p>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 600,
                  color: '#333333',
                  lineHeight: '1.4'
                }}>
                  Great. Keep doing what you're doing.
                </p>
              </div>
            </div>
          </div>
          
          {/* Path 2: Need medication */}
          <div className="rounded-2xl p-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '2px solid #E63946' }}>
            <div className="flex items-start gap-4">
              <Pill size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <div>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '30px',
                  fontWeight: 700,
                  color: '#E63946',
                  lineHeight: '1.3',
                  marginBottom: '8px'
                }}>
                  If they stay elevated or climb:
                </p>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 600,
                  color: '#333333',
                  lineHeight: '1.4'
                }}>
                  Your doctor will likely recommend medication along with lifestyle changes.
                </p>
              </div>
            </div>
          </div>
        </div>
        
        {/* Key point */}
        <div className="max-w-[880px] mx-auto mt-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Give lifestyle changes three months. Track your BP at home.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
