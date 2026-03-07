import React from 'react';
import { SlideLayout } from '../SlideLayout';
import { Search, XCircle, TrendingDown } from 'lucide-react';

export function DetoxSlide3() {
  const backgroundElements = (
    <>
      {/* Gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-[#E4F1EF] via-[#F8F9FA] to-[#E4F1EF]"></div>
      
      {/* Decorative circles */}
      <div className="absolute top-20 right-16 w-[240px] h-[240px] rounded-full" style={{ backgroundColor: 'rgba(230, 57, 70, 0.07)' }}></div>
      <div className="absolute bottom-24 left-16 w-[280px] h-[280px] rounded-full" style={{ backgroundColor: 'rgba(32, 113, 120, 0.05)' }}></div>
    </>
  );

  return (
    <SlideLayout slideNumber="03/08" backgroundElements={backgroundElements}>
      <div className="px-8">
        {/* Icon */}
        <div className="flex justify-center mb-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-[#E63946] to-[#F28C81] flex items-center justify-center shadow-lg">
            <Search size={44} color="#F8F9FA" strokeWidth={3} />
          </div>
        </div>
        
        {/* Title */}
        <h2 style={{ 
          fontFamily: 'Inter, sans-serif',
          fontSize: '46px',
          fontWeight: 700,
          color: '#E63946',
          lineHeight: '1.2',
          marginBottom: '20px',
          textAlign: 'center'
        }}>
          What Science Actually Says About Detox Products
        </h2>
        
        {/* Research findings */}
        <div className="max-w-[900px] mx-auto mb-5 rounded-3xl p-6" style={{ backgroundColor: 'rgba(230, 57, 70, 0.12)', border: '3px solid #E63946' }}>
          <div className="flex items-start gap-4 mb-4">
            <Search size={38} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '32px',
              fontWeight: 700,
              color: '#E63946',
              lineHeight: '1.3'
            }}>
              Researchers Examined Hundreds of Trials
            </p>
          </div>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '28px',
            fontWeight: 600,
            color: '#333333',
            lineHeight: '1.4'
          }}>
            Testing commercial detox supplements and weight loss products. Most studies were low quality with high bias risk.
          </p>
        </div>
        
        {/* The findings */}
        <div className="max-w-[900px] mx-auto space-y-4 mb-5">
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(242, 140, 129, 0.15)', border: '2px solid #F28C81' }}>
            <div className="flex items-start gap-4 mb-3">
              <XCircle size={36} color="#F28C81" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#F28C81',
                lineHeight: '1.3'
              }}>
                Well-Designed Studies
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              Showed little to no benefit from detox products
            </p>
          </div>
          
          <div className="p-5 rounded-2xl" style={{ backgroundColor: 'rgba(230, 57, 70, 0.15)', border: '2px solid #E63946' }}>
            <div className="flex items-start gap-4 mb-3">
              <TrendingDown size={36} color="#E63946" strokeWidth={3} className="flex-shrink-0 mt-1" />
              <p style={{ 
                fontFamily: 'Inter, sans-serif',
                fontSize: '30px',
                fontWeight: 700,
                color: '#E63946',
                lineHeight: '1.3'
              }}>
                Micronutrient & Herbal Supplements
              </p>
            </div>
            <p style={{ 
              fontFamily: 'Inter, sans-serif',
              fontSize: '26px',
              fontWeight: 600,
              color: '#333333',
              lineHeight: '1.3'
            }}>
              No evidence to recommend them. Some caused side effects.
            </p>
          </div>
        </div>
        
        {/* Bottom line */}
        <div className="max-w-[880px] mx-auto rounded-2xl p-5" style={{ backgroundColor: 'rgba(32, 113, 120, 0.12)' }}>
          <p style={{ 
            fontFamily: 'Inter, sans-serif',
            fontSize: '30px',
            fontWeight: 700,
            color: '#207178',
            lineHeight: '1.3',
            textAlign: 'center'
          }}>
            Charcoal lattes and "cleansing" juices? Aggressive marketing, not medical evidence.
          </p>
        </div>
      </div>
    </SlideLayout>
  );
}
