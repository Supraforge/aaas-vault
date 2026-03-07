import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Cigarette, Skull, AlertCircle } from 'lucide-react';

export function Slide6() {
  const backgroundElements = (
    <>
      {/* Gradient background with warning tone */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Warning circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.05)' }}></div>
      <div className="absolute bottom-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.05)' }}></div>
      
      {/* Warning stripes pattern */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="stripes" width="20" height="20" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
            <rect width="10" height="20" fill="#E63946"/>
          </pattern>
        </defs>
        <circle cx="200" cy="200" r="100" fill="url(#stripes)" />
        <circle cx="880" cy="800" r="120" fill="url(#stripes)" />
      </svg>
    </>
  );

  const timeline = [
    { age: '45', event: 'Strokes' },
    { age: '50', event: 'Heart attacks' },
    { age: '55', event: 'Death' }
  ];

  return (
    <SlideLayout slideNumber="06/10" backgroundElements={backgroundElements}>
      <div className="px-10">
        {/* Warning icon */}
        <div className="flex justify-center mb-6">
          <div className="relative">
            <div className="w-24 h-24 rounded-full bg-[#E63946] flex items-center justify-center">
              <Cigarette size={48} color="#F8F9FA" strokeWidth={2.5} />
            </div>
            <div className="absolute -top-2 -right-2">
              <Skull size={36} color="#E63946" strokeWidth={2.5} />
            </div>
          </div>
        </div>
        
        {/* Heading */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '54px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.3',
          textAlign: 'center',
          marginBottom: '30px',
          maxWidth: '900px',
          margin: '0 auto 30px'
        }}>
          Smoking causing cholesterol problems is the mildest thing it does to you.
        </h2>
        
        {/* Timeline */}
        <div className="max-w-[750px] mx-auto mb-6">
          <div className="relative">
            {/* Timeline line */}
            <div className="absolute left-1/2 top-0 bottom-0 w-1 bg-[#E63946] transform -translate-x-1/2"></div>
            
            <div className="space-y-6">
              {timeline.map((item, index) => (
                <div key={index} className="relative flex items-center justify-center">
                  <div className="bg-white border-3 border-[#E63946] rounded-xl p-4 shadow-lg flex items-center gap-4 z-10">
                    <div className="w-16 h-16 rounded-full bg-[#E63946] flex items-center justify-center flex-shrink-0">
                      <span style={{ 
                        fontFamily: 'Inter, sans-serif',
                        fontSize: '28px',
                        fontWeight: 700,
                        color: '#F8F9FA'
                      }}>
                        {item.age}
                      </span>
                    </div>
                    <div className="flex items-center gap-2">
                      <AlertCircle size={28} color="#E63946" strokeWidth={2.5} />
                      <span style={{ 
                        fontFamily: 'Inter, sans-serif',
                        fontSize: '28px',
                        fontWeight: 600,
                        color: '#333333'
                      }}>
                        {item.event}
                      </span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
        
        {/* Body text */}
        <p style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '26px',
          fontWeight: 400,
          color: '#333333',
          lineHeight: '1.4',
          textAlign: 'center',
          maxWidth: '850px',
          margin: '0 auto',
          fontStyle: 'italic'
        }}>
          Smoking doesn't just 'increase risk'—it kills you in ways that have nothing to do with your lipid panel.
        </p>
      </div>
    </SlideLayout>
  );
}