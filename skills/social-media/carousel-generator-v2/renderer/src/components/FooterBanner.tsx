import React from 'react';
import doctorPhoto from 'figma:asset/5e4311be9235ba207024edfb13240abe8cf20f3f.png';
import { Download } from 'lucide-react';
import { Button } from './ui/button';

export function FooterBanner() {
  const downloadBanner = async () => {
    const bannerElement = document.getElementById('footer-banner');
    if (!bannerElement) return;

    try {
      const html2canvas = (await import('html2canvas')).default;
      const canvas = await html2canvas(bannerElement, {
        width: 2400,
        height: 480,
        scale: 2,
        backgroundColor: null, // Transparent background
        logging: false,
        useCORS: true,
        allowTaint: false,
        removeContainer: true
      });
      
      canvas.toBlob((blob) => {
        if (blob) {
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = 'dr-shailesh-footer-logo.png';
          a.click();
          URL.revokeObjectURL(url);
        }
      }, 'image/png');
    } catch (error) {
      console.error('Error downloading banner:', error);
      alert(`Error downloading banner: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 flex flex-col items-center justify-center p-8">
      <div className="mb-8 text-center">
        <h1 className="mb-2" style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '36px',
          fontWeight: 700,
          color: '#F8F9FA'
        }}>
          Footer Logo
        </h1>
        <p style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '18px',
          fontWeight: 400,
          color: '#94A3B8'
        }}>
          2400×480 px - Ultra high-resolution logo for Gamma slides footer
        </p>
      </div>

      {/* Banner preview with dark background for visibility */}
      <div className="mb-8 p-12 bg-slate-700/50 rounded-xl">
        <div id="footer-banner" className="relative">
          {/* Main logo container */}
          <div 
            className="relative overflow-hidden flex items-center"
            style={{
              width: '2400px',
              height: '480px',
              paddingLeft: '60px',
              paddingRight: '60px'
            }}
          >
            {/* Profile photo - left side */}
            <div className="flex-shrink-0">
              <img 
                src={doctorPhoto} 
                alt="Dr Shailesh Singh"
                className="rounded-full object-cover"
                style={{
                  width: '320px',
                  height: '320px',
                  border: '8px solid #FFFFFF',
                  boxShadow: '0 8px 32px rgba(32, 113, 120, 0.3)'
                }}
              />
            </div>

            {/* Text block - right side, vertically centered to match photo height */}
            <div 
              className="ml-16 flex flex-col justify-center"
              style={{
                height: '320px'
              }}
            >
              <div 
                style={{
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '96px',
                  fontWeight: 700,
                  color: '#333333',
                  lineHeight: '1.3',
                  marginBottom: '8px'
                }}
              >
                Dr Shailesh Singh
              </div>
              <div 
                style={{
                  fontFamily: 'Inter, sans-serif',
                  fontSize: '80px',
                  fontWeight: 500,
                  color: '#207178',
                  lineHeight: '1.3'
                }}
              >
                @dr.shailesh.singh
              </div>
            </div>
          </div>
        </div>
        
        {/* Size indicator */}
        <div className="mt-4 text-center">
          <p style={{
            fontFamily: 'Inter, sans-serif',
            fontSize: '12px',
            fontWeight: 400,
            color: '#64748B'
          }}>
            2400 × 480 px (2× scale for ultra high quality)
          </p>
        </div>
      </div>

      {/* Download button */}
      <Button
        onClick={downloadBanner}
        className="bg-gradient-to-r from-[#207178] to-[#F28C81] hover:opacity-90"
        size="lg"
      >
        <Download className="mr-2" size={18} />
        Download Footer Logo (PNG)
      </Button>

      {/* Info text */}
      <div className="mt-6 text-center max-w-md">
        <p style={{
          fontFamily: 'Inter, sans-serif',
          fontSize: '14px',
          fontWeight: 400,
          color: '#94A3B8',
          lineHeight: '1.5'
        }}>
          Ultra high-resolution footer logo with transparent background. Scaled up to 2400×480px to match the visual size and proportions of your Instagram slide footers when used at XL size in Gamma.
        </p>
      </div>
    </div>
  );
}
