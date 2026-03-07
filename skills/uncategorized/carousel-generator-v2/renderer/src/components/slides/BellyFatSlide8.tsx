import React from 'react';
import { Target, Ruler, TrendingDown, Heart } from 'lucide-react';

export function BellyFatSlide8() {
  const actions = [
    'Measure your waist circumference today',
    'Know your number: >90 cm (men) or >80 cm (women) = higher risk',
    'Aim for 3-5% weight loss for measurable benefits',
    'Small sustained changes = real metabolic improvements'
  ];

  const keyPoints = [
    { icon: '⚠️', text: 'Waist > weight on scale' },
    { icon: '🫀', text: 'Visceral fat drives disease' }
  ];

  return (
    <div className="relative w-[1080px] h-[1080px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      <div className="absolute inset-0" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.15), #F8F9FA, rgba(230, 57, 70, 0.15))' }}></div>
      
      {/* Celebratory circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 left-1/4 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}></div>
      <div className="absolute bottom-20 right-1/4 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      
      {/* Main content container */}
      <div className="relative z-10 flex flex-col h-full p-8">
        {/* Slide number - top left */}
        <div className="mb-4">
          <span style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '42px',
            fontWeight: 700,
            color: '#207178'
          }}>
            08/08
          </span>
        </div>
        
        {/* Main content area */}
        <div className="flex-1 flex items-center justify-center">
          <div className="w-full px-6">
            {/* Icon */}
            <div className="flex justify-center mb-4">
              <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
                <Target size={44} color="#F8F9FA" strokeWidth={3} />
              </div>
            </div>
            
            {/* Main title */}
            <h1 style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '52px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.2',
              marginBottom: '24px',
              textAlign: 'center'
            }}>
              The Bottom Line
            </h1>
            
            {/* Key points row */}
            <div className="grid grid-cols-2 gap-4 max-w-[800px] mx-auto mb-5">
              {keyPoints.map((point, index) => (
                <div key={index} className="rounded-2xl p-5 text-center" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)' }}>
                  <p style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '48px',
                    fontWeight: 700,
                    lineHeight: '1.1',
                    marginBottom: '8px'
                  }}>
                    {point.icon}
                  </p>
                  <p style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '24px',
                    fontWeight: 700,
                    color: '#333333',
                    lineHeight: '1.3'
                  }}>
                    {point.text}
                  </p>
                </div>
              ))}
            </div>
            
            {/* Action items */}
            <div className="max-w-[900px] mx-auto space-y-3 mb-5">
              {actions.map((action, index) => (
                <div key={index} className="flex items-start gap-3 p-4 rounded-xl" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
                  <div className="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center" style={{ backgroundColor: '#207178' }}>
                    <span style={{ 
                      fontFamily: 'Inter, sans-serif',
                      fontSize: '18px',
                      fontWeight: 700,
                      color: '#F8F9FA'
                    }}>
                      {index + 1}
                    </span>
                  </div>
                  <span style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '26px',
                    fontWeight: 600,
                    color: '#333333',
                    lineHeight: '1.3'
                  }}>
                    {action}
                  </span>
                </div>
              ))}
            </div>
            
            {/* Final statement */}
            <div className="max-w-[900px] mx-auto rounded-2xl p-5 mb-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                Your genes loaded the gun, but your lifestyle pulls the trigger.
              </p>
            </div>
            
            {/* CTA Box - No footer, integrated call to action */}
            <div className="max-w-[900px] mx-auto rounded-3xl p-6 shadow-2xl" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
              <div className="text-center">
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '34px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1.4'
                }}>
                  Start with measurement. Continue with movement. The 3-5% that changes everything is closer than you think.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
