import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Scale, Heart, Activity } from 'lucide-react';

export function Slide9() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-tr from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-16 right-16 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
      <div className="absolute bottom-24 left-12 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.05)' }}></div>
      
      {/* Heart pulse pattern */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,540 L200,540 L250,440 L300,640 L350,540 L550,540 L600,440 L650,640 L700,540 L900,540 L950,440 L1000,640 L1050,540 L1080,540" 
          stroke="#207178" strokeWidth="5" fill="none" strokeLinecap="round" strokeLinejoin="round"/>
      </svg>
    </>
  );

  return (
    <SlideLayout slideNumber="09/10" backgroundElements={backgroundElements}>
      <div className="px-10">
        {/* Heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '58px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.3',
          textAlign: 'center',
          marginBottom: '35px'
        }}>
          Yea. The cholesterol benefit is modest {"(<5% LDL reduction)"}.
        </h2>
        
        {/* Balance scale visualization */}
        <div className="max-w-[900px] mx-auto mb-6">
          <div className="relative">
            {/* Center pivot */}
            <div className="flex justify-center mb-6">
              <div className="w-24 h-24 rounded-full bg-[#207178] flex items-center justify-center">
                <Scale size={48} color="#F8F9FA" strokeWidth={2.5} />
              </div>
            </div>
            
            {/* Scale arms */}
            <div className="flex items-start justify-between gap-6">
              {/* Left side - Cholesterol numbers */}
              <div className="flex-1 rounded-xl p-6 border-3 border-[#F28C81] transform -translate-y-3" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
                <div className="text-center mb-3">
                  <Activity size={36} color="#F28C81" strokeWidth={2.5} className="mx-auto mb-2" />
                  <div style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '28px',
                    fontWeight: 700,
                    color: '#333333',
                    marginBottom: '8px'
                  }}>
                    Cholesterol Numbers
                  </div>
                  <div style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '48px',
                    fontWeight: 700,
                    color: '#F28C81'
                  }}>
                    {"<5%"}
                  </div>
                  <div style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '22px',
                    fontWeight: 400,
                    color: '#333333',
                    marginTop: '6px'
                  }}>
                    LDL reduction
                  </div>
                </div>
              </div>
              
              {/* Right side - Overall health */}
              <div className="flex-1 rounded-xl p-6 border-4 border-[#207178] shadow-lg" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.2), rgba(32, 113, 120, 0.1))' }}>
                <div className="text-center mb-3">
                  <Heart size={36} color="#207178" strokeWidth={2.5} className="mx-auto mb-2" fill="#207178" />
                  <div style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '28px',
                    fontWeight: 700,
                    color: '#333333',
                    marginBottom: '8px'
                  }}>
                    Overall Health
                  </div>
                  <div style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '56px',
                    fontWeight: 700,
                    color: '#207178'
                  }}>
                    +++
                  </div>
                  <div style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '22px',
                    fontWeight: 400,
                    color: '#333333',
                    marginTop: '6px'
                  }}>
                    Major benefits
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        {/* Body text */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '30px',
          fontWeight: 500,
          color: '#333333',
          lineHeight: '1.4',
          textAlign: 'center',
          maxWidth: '850px',
          margin: '0 auto',
          backgroundColor: 'rgba(32, 113, 120, 0.1)',
          padding: '20px',
          borderRadius: '16px',
          fontStyle: 'italic'
        }}>
          But exercise reduces overall cardiovascular risk in ways your lipid panel doesn't capture.
        </p>
      </div>
    </SlideLayout>
  );
}