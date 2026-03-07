import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Heart, Scale, Utensils, Dumbbell, Droplets, Apple } from 'lucide-react';

export function BP120Slide5() {
  const factors = [
    {
      icon: Scale,
      title: 'Your weight',
      description: 'Losing just 5 kg drops systolic pressure by 4.4 points on average.'
    },
    {
      icon: Utensils,
      title: 'What you eat',
      description: 'Mediterranean and DASH diets consistently lower BP.'
    },
    {
      icon: Droplets,
      title: 'Salt intake',
      description: 'Cut from 9-12g daily to 5g per day (about one teaspoon).'
    },
    {
      icon: Dumbbell,
      title: 'How much you move',
      description: '150 min moderate exercise weekly + strength training 2-3x/week.'
    },
    {
      icon: Apple,
      title: 'Potassium',
      description: '3,500-5,000 mg daily through bananas, potatoes, spinach, beans.'
    }
  ];

  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-16 w-[220px] h-[220px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.08)' }}></div>
      <div className="absolute bottom-28 left-20 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="05/08" backgroundElements={backgroundElements}>
      <div className="px-6">
        {/* Icon */}
        <div className="flex justify-center mb-4">
          <div className="w-18 h-18 rounded-full bg-gradient-to-br from-[#207178] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Heart size={40} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '42px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          5 Factors You Can Control
        </h2>
        
        {/* Factors grid */}
        <div className="max-w-[920px] mx-auto space-y-3">
          {factors.map((factor, index) => {
            const Icon = factor.icon;
            return (
              <div key={index} className="flex items-start gap-4 p-4 rounded-xl" style={{ backgroundColor: index % 2 === 0 ? 'rgba(32, 113, 120, 0.1)' : 'rgba(242, 140, 129, 0.12)' }}>
                <div className="flex-shrink-0 w-12 h-12 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center">
                  <Icon size={26} color="#F8F9FA" strokeWidth={3} />
                </div>
                <div className="flex-1">
                  <p style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '28px',
                    fontWeight: 700,
                    color: '#207178',
                    lineHeight: '1.3',
                    marginBottom: '4px'
                  }}>
                    {factor.title}
                  </p>
                  <p style={{ 
                    fontFamily: 'Inter, sans-serif',
                    fontSize: '24px',
                    fontWeight: 600,
                    color: '#333333',
                    lineHeight: '1.3'
                  }}>
                    {factor.description}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
        
        {/* Bottom note */}
        <div className="max-w-[880px] mx-auto mt-5 rounded-2xl p-4" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.4',
            textAlign: 'center'
          }}>
            It's not about perfection—it's about shifting the balance.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}