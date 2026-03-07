import React from 'react';
import { Heart, CheckCircle2 } from 'lucide-react';

export function Slide10() {
  const changes = [
    'Lose weight if obese',
    'Quit alcohol & smoking',
    'Exercise regularly'
  ];

  return (
    <div className="relative w-[1080px] h-[1080px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      {/* Vibrant gradient background */}
      <div className="absolute inset-0" style={{ background: 'linear-gradient(to bottom right, rgba(32, 113, 120, 0.2), #F8F9FA, rgba(242, 140, 129, 0.2))' }}></div>
      
      {/* Celebratory circles */}
      <div className="absolute top-10 left-10 w-[250px] h-[250px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute top-10 right-10 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      <div className="absolute bottom-20 left-1/4 w-[180px] h-[180px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.1)' }}></div>
      <div className="absolute bottom-20 right-1/4 w-[150px] h-[150px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.1)' }}></div>
      
      {/* Heart pattern background */}
      <svg className="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <path d="M200,200 L200,180 C200,140 240,140 240,180 C240,140 280,140 280,180 L280,200 L240,240 Z" fill="#F28C81"/>
        <path d="M800,300 L800,280 C800,240 840,240 840,280 C840,240 880,240 880,280 L880,300 L840,340 Z" fill="#207178"/>
        <path d="M150,700 L150,680 C150,640 190,640 190,680 C190,640 230,640 230,680 L230,700 L190,740 Z" fill="#F28C81"/>
        <path d="M850,800 L850,780 C850,740 890,740 890,780 C890,740 930,740 930,780 L930,800 L890,840 Z" fill="#207178"/>
      </svg>
      
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
            10/10
          </span>
        </div>
        
        {/* Main content area */}
        <div className="flex-1 flex items-center justify-center">
          <div className="w-full px-6">
            {/* Central heart icon */}
            <div className="flex justify-center mb-8">
              <div className="relative">
                <div className="w-40 h-40 rounded-full flex items-center justify-center shadow-2xl" style={{ background: 'linear-gradient(to bottom right, #207178, #F28C81)' }}>
                  <Heart size={80} color="#F8F9FA" strokeWidth={2.5} fill="#F8F9FA" />
                </div>
              </div>
            </div>
            
            {/* Heading */}
            <h2 style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '52px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.3',
              textAlign: 'center',
              marginBottom: '28px'
            }}>
              I see patients every day who wish they'd started earlier.
            </h2>
            
            {/* Question */}
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '36px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.4',
              textAlign: 'center',
              marginBottom: '24px'
            }}>
              Which of these 3 have you actually tried?
            </p>
            
            {/* Checklist */}
            <div className="max-w-[700px] mx-auto mb-10 space-y-4">
              {changes.map((change, index) => (
                <div key={index} className="flex items-center gap-4 p-4 rounded-xl border-2 border-[#207178] shadow-md" style={{ backgroundColor: 'rgba(255, 255, 255, 0.7)' }}>
                  <CheckCircle2 size={32} color="#F28C81" strokeWidth={2.5} />
                  <span style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '30px',
                    fontWeight: 600,
                    color: '#333333'
                  }}>
                    {change}
                  </span>
                </div>
              ))}
            </div>
            
            {/* CTA Box - No footer, integrated call to action */}
            <div className="max-w-[850px] mx-auto rounded-3xl p-10 shadow-2xl" style={{ background: 'linear-gradient(to right, #207178, #F28C81)' }}>
              <div className="text-center">
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '32px',
                  fontWeight: 600,
                  color: '#F8F9FA',
                  lineHeight: '1.4',
                  marginBottom: '14px'
                }}>
                  Take care of your heart, one fact at a time.
                </p>
                <p style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '30px',
                  fontWeight: 700,
                  color: '#F8F9FA',
                  lineHeight: '1.4'
                }}>
                  Follow @dr.shailesh.singh for science-based insights.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}