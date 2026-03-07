import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { TrendingDown, ArrowDown, Activity, Dumbbell } from 'lucide-react';

export function Slide8() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-bl from-[#F8F9FA] via-[#E4F1EF] to-[#F8F9FA]"></div>
      
      {/* Decorative arrows and shapes */}
      <div className="absolute top-10 left-10 opacity-5">
        <TrendingDown size={120} color="#207178" strokeWidth={3} />
      </div>
      <div className="absolute bottom-20 right-20 opacity-5">
        <TrendingDown size={100} color="#F28C81" strokeWidth={3} />
      </div>
      
      {/* Decorative shapes */}
      <div className="absolute top-1/3 right-10 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
      <div className="absolute bottom-1/4 left-16 w-[120px] h-[120px]" style={{ backgroundColor: 'rgba(242, 140, 129, 0.05)', borderRadius: '40% 60% 60% 40% / 40% 40% 60% 60%' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="08/10" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* First section - Aerobic alone */}
        <div className="mb-6">
          <div className="flex items-center justify-center gap-3 mb-4">
            <div className="w-16 h-16 rounded-full bg-[#F28C81] flex items-center justify-center">
              <Activity size={32} color="#F8F9FA" strokeWidth={2.5} />
            </div>
            <h3 style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '44px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.2'
            }}>
              Aerobic exercise alone:
            </h3>
          </div>
          
          <div className="grid grid-cols-3 gap-4 max-w-[950px] mx-auto">
            <div className="rounded-2xl p-5 border-2 border-[#F28C81]" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
              <ArrowDown size={24} color="#F28C81" strokeWidth={3} className="mx-auto mb-2" />
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '22px',
                fontWeight: 600,
                color: '#333333',
                textAlign: 'center',
                lineHeight: '1.3'
              }}>
                Triglycerides
              </div>
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#F28C81',
                textAlign: 'center'
              }}>
                ↓ 10-20%
              </div>
            </div>
            
            <div className="rounded-2xl p-6 border-2 border-[#F28C81]" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
              <ArrowDown size={32} color="#F28C81" strokeWidth={3} className="mx-auto mb-3" />
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '22px',
                fontWeight: 600,
                color: '#333333',
                textAlign: 'center',
                lineHeight: '1.3'
              }}>
                LDL drops
              </div>
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#F28C81',
                textAlign: 'center'
              }}>
                5-10 mg/dL
              </div>
            </div>
            
            <div className="rounded-xl p-4 border-2 border-[#207178]" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
              <div className="transform rotate-180 mx-auto mb-2">
                <ArrowDown size={24} color="#207178" strokeWidth={3} />
              </div>
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '22px',
                fontWeight: 600,
                color: '#333333',
                textAlign: 'center',
                lineHeight: '1.3'
              }}>
                HDL increases
              </div>
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#207178',
                textAlign: 'center'
              }}>
                2-5%
              </div>
            </div>
          </div>
        </div>
        
        {/* Divider */}
        <div className="flex items-center gap-3 my-5 max-w-[700px] mx-auto">
          <div className="flex-1 h-1 bg-[#207178]"></div>
          <span style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 700,
            color: '#207178'
          }}>
            VS
          </span>
          <div className="flex-1 h-1 bg-[#207178]"></div>
        </div>
        
        {/* Second section - Combined */}
        <div>
          <div className="flex items-center justify-center gap-3 mb-4">
            <div className="w-16 h-16 rounded-full bg-gradient-to-br from-[#F28C81] to-[#207178] flex items-center justify-center">
              <Dumbbell size={32} color="#F8F9FA" strokeWidth={2.5} />
            </div>
            <h3 style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '42px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.2'
            }}>
              Combined cardio + strength:
            </h3>
          </div>
          
          <div className="grid grid-cols-2 gap-4 max-w-[650px] mx-auto">
            <div className="rounded-xl p-5 border-3 border-[#207178]" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.1), rgba(242, 140, 129, 0.1))' }}>
              <ArrowDown size={32} color="#207178" strokeWidth={3} className="mx-auto mb-2" />
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 600,
                color: '#333333',
                textAlign: 'center',
                lineHeight: '1.3'
              }}>
                LDL drops
              </div>
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '36px',
                fontWeight: 700,
                color: '#207178',
                textAlign: 'center'
              }}>
                7-12 mg/dL
              </div>
            </div>
            
            <div className="rounded-xl p-5 border-3 border-[#207178]" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.1), rgba(242, 140, 129, 0.1))' }}>
              <ArrowDown size={32} color="#207178" strokeWidth={3} className="mx-auto mb-2" />
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '24px',
                fontWeight: 600,
                color: '#333333',
                textAlign: 'center',
                lineHeight: '1.3'
              }}>
                Triglycerides
              </div>
              <div style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '36px',
                fontWeight: 700,
                color: '#207178',
                textAlign: 'center'
              }}>
                ↓ 15-25%
              </div>
            </div>
          </div>
        </div>
      </div>
    </SlideLayout>
  );
}