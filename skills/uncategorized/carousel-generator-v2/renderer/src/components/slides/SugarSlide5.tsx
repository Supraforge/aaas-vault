import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { AlertOctagon, Flame } from 'lucide-react';

export function SugarSlide5() {
  const backgroundElements = (
    <>
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      <div className="absolute top-10 left-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.08)' }}></div>
      <div className="absolute bottom-10 right-10 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-[300px] h-[300px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.04)' }}></div>
    </>
  );

  const examples = [
    'Morning cereal',
    'Lunch sandwich on white bread',
    'Afternoon biscuits',
    'Evening white rice'
  ];

  const effects = [
    'Disrupts your normal metabolism',
    'Increases fat production in your body',
    'Promotes fat deposits in and around organs'
  ];

  return (
    <SlideLayout slideNumber="05/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <AlertOctagon size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '48px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          Frequent Sugar Intake = All-Day Insulin Elevation
        </h2>
        
        {/* Examples */}
        <div className="rounded-2xl p-5 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center',
            marginBottom: '12px'
          }}>
            Typical Day:
          </p>
          <div className="grid grid-cols-2 gap-3">
            {examples.map((example, index) => (
              <div key={index} className="p-3 rounded-lg" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '22px',
                  fontWeight: 600,
                  color: '#333333',
                  lineHeight: '1.3',
                  textAlign: 'center'
                }}>
                  {example}
                </p>
              </div>
            ))}
          </div>
        </div>
        
        {/* Effects */}
        <div className="rounded-2xl p-5 mb-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.4',
            textAlign: 'center',
            marginBottom: '12px'
          }}>
            Constant Elevation Does 3 Things:
          </p>
          <div className="space-y-2">
            {effects.map((effect, index) => (
              <div key={index} className="p-3 rounded-lg" style={{ backgroundColor: 'rgba(255, 255, 255, 0.6)' }}>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '22px',
                  fontWeight: 600,
                  color: '#333333',
                  lineHeight: '1.3',
                  textAlign: 'center'
                }}>
                  {index + 1}. {effect}
                </p>
              </div>
            ))}
          </div>
        </div>
        
        {/* Bottom box */}
        <div className="rounded-2xl p-5 shadow-lg" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '26px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            Your triglycerides go up. Over 10% daily calories from fructose pushes them even higher.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
