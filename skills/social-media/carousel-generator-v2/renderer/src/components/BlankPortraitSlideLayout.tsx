import React from 'react';
import doctorPhoto from 'figma:asset/5e4311be9235ba207024edfb13240abe8cf20f3f.png';
import { ChevronRight } from 'lucide-react';

interface BlankPortraitSlideLayoutProps {
  children: React.ReactNode;
  backgroundElements?: React.ReactNode;
}

export function BlankPortraitSlideLayout({ children, backgroundElements }: BlankPortraitSlideLayoutProps) {
  return (
    <div className="relative w-[1080px] h-[1350px] bg-[#E4F1EF] overflow-hidden flex flex-col">
      {/* Background decorative elements */}
      {backgroundElements}
      
      {/* Main content container */}
      <div className="relative z-10 flex flex-col h-full p-8">
        {/* Main content area - no slide number */}
        <div className="flex-1 flex items-center justify-center overflow-hidden">
          <div className="w-full">
            {children}
          </div>
        </div>
        
        {/* Footer */}
        <div className="mt-4 flex-shrink-0">
          {/* Accent line separator */}
          <div className="w-full h-[2px] bg-[#F28C81] mb-4"></div>
          
          <div className="flex items-center justify-between">
            {/* Left: Profile and info */}
            <div className="flex items-center gap-3">
              <img 
                src={doctorPhoto} 
                alt="Dr Shailesh Singh"
                className="w-[60px] h-[60px] rounded-full object-cover flex-shrink-0"
              />
              <div>
                <div style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '26px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.2'
                }}>
                  Dr Shailesh Singh
                </div>
                <div style={{ 
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '22px',
                  fontWeight: 400,
                  color: '#333333',
                  lineHeight: '1.2'
                }}>
                  @dr.shailesh.singh
                </div>
              </div>
            </div>
            
            {/* Right: Arrow indicators */}
            <div className="flex gap-1 flex-shrink-0">
              <ChevronRight size={24} color="#207178" strokeWidth={3} />
              <ChevronRight size={24} color="#207178" strokeWidth={3} />
              <ChevronRight size={24} color="#207178" strokeWidth={3} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
