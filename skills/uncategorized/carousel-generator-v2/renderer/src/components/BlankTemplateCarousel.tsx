import React, { useState } from 'react';
import { BlankTemplate } from './slides/BlankTemplate';
import { BlankTemplatePortrait } from './slides/BlankTemplatePortrait';
import { Download } from 'lucide-react';
import { Button } from './ui/button';

export function BlankTemplateCarousel() {
  const [currentTemplate, setCurrentTemplate] = useState<'square' | 'portrait'>('portrait');

  const downloadTemplate = async (templateId: string) => {
    const slideElement = document.getElementById(templateId);
    if (!slideElement) return;

    try {
      // Using html2canvas for screenshot
      const html2canvas = (await import('html2canvas')).default;
      const canvas = await html2canvas(slideElement, {
        width: currentTemplate === 'square' ? 1080 : 1080,
        height: currentTemplate === 'square' ? 1080 : 1350,
        scale: 2,
        backgroundColor: '#E4F1EF',
        logging: false,
        useCORS: true,
        allowTaint: false,
        removeContainer: true
      });
      
      // Convert to blob and download
      canvas.toBlob((blob) => {
        if (blob) {
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = `blank-template-${currentTemplate}.png`;
          a.click();
          URL.revokeObjectURL(url);
        }
      }, 'image/png');
    } catch (error) {
      console.error('Error downloading template:', error);
      alert(`Error downloading template: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 flex flex-col items-center justify-center p-8">
      <div className="mb-6 text-center">
        <h1 className="mb-2" style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '36px',
          fontWeight: 700,
          color: '#F8F9FA'
        }}>
          Blank Template Slides
        </h1>
        <p style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '18px',
          fontWeight: 400,
          color: '#94A3B8'
        }}>
          Download blank slides for manual content creation
        </p>
      </div>

      {/* Template selector */}
      <div className="mb-6 flex gap-3 bg-slate-700/50 p-3 rounded-lg">
        <Button
          onClick={() => setCurrentTemplate('square')}
          variant="outline"
          className={`${
            currentTemplate === 'square'
              ? 'bg-[#207178] text-white border-[#207178]'
              : 'bg-white/10 text-white border-white/20 hover:bg-white/20'
          }`}
        >
          Square (1080×1080)
        </Button>
        <Button
          onClick={() => setCurrentTemplate('portrait')}
          variant="outline"
          className={`${
            currentTemplate === 'portrait'
              ? 'bg-[#207178] text-white border-[#207178]'
              : 'bg-white/10 text-white border-white/20 hover:bg-white/20'
          }`}
        >
          Portrait (1080×1350)
        </Button>
      </div>

      {/* Template preview */}
      <div className="relative mb-6 shadow-2xl rounded-lg overflow-hidden">
        {currentTemplate === 'square' ? (
          <div id="blank-template-square">
            <BlankTemplate />
          </div>
        ) : (
          <div id="blank-template-portrait">
            <BlankTemplatePortrait />
          </div>
        )}
      </div>

      {/* Download button */}
      <Button
        onClick={() => downloadTemplate(currentTemplate === 'square' ? 'blank-template-square' : 'blank-template-portrait')}
        className="bg-gradient-to-r from-[#E63946] to-[#F28C81] hover:opacity-90"
        size="lg"
      >
        <Download className="mr-2" size={18} />
        Download {currentTemplate === 'square' ? 'Square' : 'Portrait'} Template
      </Button>

      <div className="mt-6 text-center max-w-md">
        <p style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '14px',
          fontWeight: 400,
          color: '#94A3B8',
          lineHeight: '1.5'
        }}>
          These blank templates include your brand colors, decorative elements, and footer. Download and add your content in your preferred design tool.
        </p>
      </div>
    </div>
  );
}
