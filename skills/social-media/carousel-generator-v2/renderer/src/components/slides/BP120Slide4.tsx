import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingUp, BarChart3 } from 'lucide-react';

export function BP120Slide4() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-28 left-20 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.07)' }}></div>
      <div className="absolute bottom-24 right-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.07)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <BarChart3 size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Main heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '44px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          Why 120/80 became "normal" in everyone's mind
        </h2>
        
        {/* Old thinking */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            For decades, doctors used 140/90 as the cutoff for hypertension. Anything below that seemed fine.
          </p>
        </div>
        
        {/* Research changed everything */}
        <div className="max-w-[880px] mx-auto rounded-3xl p-6 mb-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)', border: '3px solid #207178' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '34px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center',
            marginBottom: '16px'
          }}>
            But research over the past 20 years changed everything.
          </p>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Cardiovascular risk doesn't flip on like a switch at 140/90. It's a slope. Your risk starts increasing gradually from levels as low as 90/75.
          </p>
        </div>
        
        {/* Bottom insight */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '32px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            A reading of 120/80 puts you at higher risk than someone at 110/70.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
