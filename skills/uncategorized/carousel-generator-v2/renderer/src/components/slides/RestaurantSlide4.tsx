import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Home, CheckCircle2, Leaf } from 'lucide-react';

export function RestaurantSlide4() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-24 right-20 w-[200px] h-[200px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.08)' }}></div>
      <div className="absolute bottom-28 left-20 w-[260px] h-[260px] rounded-full" style={{ backgroundColor: 'rgba(242, 140, 129, 0.06)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="04/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#207178] to-[#E4F1EF] flex items-center justify-center shadow-lg">
            <Home size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '44px',
          fontWeight: 700,
          color: '#207178',
          lineHeight: '1.2',
          marginBottom: '24px',
          textAlign: 'center'
        }}>
          Why Home-Cooked Meals Work Differently
        </h2>
        
        {/* Main comparison box */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-3xl p-6" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)', border: '3px solid #207178' }}>
          <div className="flex items-start gap-4 mb-4">
            <Leaf size={38} color="#207178" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#207178',
              lineHeight: '1.3'
            }}>
              Fiber-rich meals change everything
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Whole grains, pulses, and vegetables contain fiber that slows down glucose entry into your bloodstream.
          </p>
        </div>
        
        {/* Benefits list */}
        <div className="max-w-[880px] mx-auto space-y-4">
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <CheckCircle2 size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Your insulin rises gradually instead of spiking
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <CheckCircle2 size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              You feel full with fewer calories—fiber increases satiety
            </p>
          </div>
          
          <div className="flex items-start gap-4 p-5 rounded-xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)' }}>
            <CheckCircle2 size={32} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '28px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Better blood glucose and cholesterol management
            </p>
          </div>
        </div>
        
        {/* Bottom insight */}
        <div className="max-w-[880px] mx-auto mt-5 rounded-2xl p-5" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 700,
            color: '#E63946',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            The quality of your calories matters as much as the quantity
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
