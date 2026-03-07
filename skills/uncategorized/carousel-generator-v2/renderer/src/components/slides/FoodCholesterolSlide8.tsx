import React from 'react';
import { Target, CheckCircle2 } from 'lucide-react';

export function FoodCholesterolSlide8() {
  const culprits = [
    { icon: '🍟', text: 'Fried foods = Trans fats + Saturated fats' },
    { icon: '🍕', text: 'Fast foods = Sat fat + Trans fat + Refined carbs' },
    { icon: '🍰', text: 'Sweet desserts = Sugar converts to triglycerides' }
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
              <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E63946] flex items-center justify-center shadow-lg">
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
            
            {/* Subtitle */}
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.4',
              textAlign: 'center',
              marginBottom: '24px'
            }}>
              Your abnormal cholesterol report is not random.
            </p>
            
            {/* The culprits */}
            <div className="max-w-[900px] mx-auto rounded-2xl p-6 mb-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '3px solid #E63946' }}>
              <div className="space-y-3">
                {culprits.map((culprit, index) => (
                  <div key={index} className="rounded-xl p-4" style={{ backgroundColor: 'rgba(255, 255, 255, 0.7)' }}>
                    <p style={{ 
                      fontFamily: 'Inter, sans-serif',
                      fontSize: '28px',
                      fontWeight: 700,
                      color: '#E63946',
                      lineHeight: '1.3',
                      textAlign: 'center'
                    }}>
                      {culprit.icon} {culprit.text}
                    </p>
                  </div>
                ))}
              </div>
            </div>
            
            {/* Knowledge statement */}
            <div className="max-w-[900px] mx-auto rounded-2xl p-5 mb-4" style={{ backgroundColor: 'rgba(32, 113, 120, 0.15)', border: '2px solid #207178' }}>
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '28px',
                fontWeight: 700,
                color: '#207178',
                lineHeight: '1.4',
                textAlign: 'center'
              }}>
                You now know which foods are doing the damage and why.
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
                  The next decision you make about what to eat is the first step toward better numbers.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
