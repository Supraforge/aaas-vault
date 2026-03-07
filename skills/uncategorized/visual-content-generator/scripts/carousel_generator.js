#!/usr/bin/env node
/**
 * Carousel Generator - Generate LinkedIn carousel PDFs from content briefs.
 *
 * Usage:
 *   node carousel_generator.js <brief.md> --theme dark --brand enora
 */

const fs = require('fs');
const path = require('path');

// Skill directories
const SKILL_DIR = path.dirname(__dirname);
const PROJECT_ROOT = path.resolve(SKILL_DIR, '../..');

// Default brand colors
const BRAND_COLORS = {
    enora: {
        dark: {
            background: '#0F172A',
            text: '#F8FAFC',
            accent: '#d4a853',
            secondary: '#1E293B'
        },
        light: {
            background: '#F8FAFC',
            text: '#0F172A',
            accent: '#d4a853',
            secondary: '#E2E8F0'
        }
    },
    'supra-forge': {
        dark: {
            background: '#0F172A',
            text: '#F8FAFC',
            accent: '#d4a853',
            secondary: '#1E293B'
        },
        light: {
            background: '#F8FAFC',
            text: '#0F172A',
            accent: '#d4a853',
            secondary: '#E2E8F0'
        }
    }
};

/**
 * Parse content brief markdown for carousel content.
 */
function parseBrief(briefPath) {
    if (!fs.existsSync(briefPath)) {
        throw new Error(`Brief not found: ${briefPath}`);
    }

    const content = fs.readFileSync(briefPath, 'utf-8');
    const lines = content.split('\n');

    const brief = {
        title: '',
        slides: [],
        hashtags: [],
        cta: ''
    };

    let currentSection = null;
    let slideContent = [];

    for (const line of lines) {
        // Extract title
        if (line.startsWith('# ')) {
            brief.title = line.replace('# ', '').trim();
        }

        // Look for carousel slides section
        if (line.toLowerCase().includes('carousel') || line.toLowerCase().includes('slide')) {
            currentSection = 'slides';
            continue;
        }

        // Extract slide content (numbered items or headings)
        if (currentSection === 'slides') {
            if (line.match(/^##?\s*Slide\s*\d+/i) || line.match(/^\d+\.\s+/)) {
                if (slideContent.length > 0) {
                    brief.slides.push(slideContent.join('\n').trim());
                }
                slideContent = [line.replace(/^##?\s*Slide\s*\d+:?\s*/i, '').replace(/^\d+\.\s+/, '')];
            } else if (line.trim() && !line.startsWith('#')) {
                slideContent.push(line.trim());
            }
        }

        // Extract hashtags
        if (line.includes('#') && line.match(/#\w+/g)) {
            const tags = line.match(/#\w+/g);
            brief.hashtags.push(...tags);
        }
    }

    // Add last slide if exists
    if (slideContent.length > 0) {
        brief.slides.push(slideContent.join('\n').trim());
    }

    // If no slides found, generate default structure
    if (brief.slides.length === 0) {
        brief.slides = [
            brief.title || 'Cover Slide',
            'The Problem: 40% of engineering time lost to compliance',
            'The Reality: Fragmented tools create blind spots',
            'The Solution: Continuous visibility across your toolchain',
            'The Result: 3 months → 2 days audit prep',
            'Get Your Free Risk Baseline'
        ];
    }

    return brief;
}

/**
 * Generate carousel slide HTML for rendering.
 */
function generateSlideHTML(slideContent, slideNumber, totalSlides, colors, brandName) {
    const isFirstSlide = slideNumber === 1;
    const isLastSlide = slideNumber === totalSlides;

    let slideType = 'content';
    if (isFirstSlide) slideType = 'cover';
    if (isLastSlide) slideType = 'cta';

    // Split content into headline and body
    const lines = slideContent.split('\n').filter(l => l.trim());
    const headline = lines[0] || '';
    const body = lines.slice(1).join('\n');

    return `
<!DOCTYPE html>
<html>
<head>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            width: 1080px;
            height: 1080px;
            background: ${colors.background};
            color: ${colors.text};
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: flex;
            flex-direction: column;
            padding: 80px;
        }
        .slide-number {
            position: absolute;
            top: 40px;
            right: 40px;
            font-size: 24px;
            color: ${colors.accent};
            font-weight: 600;
        }
        .headline {
            font-size: ${isFirstSlide ? '72px' : '56px'};
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 40px;
            ${isFirstSlide || isLastSlide ? `color: ${colors.accent};` : ''}
        }
        .body {
            font-size: 32px;
            line-height: 1.6;
            color: ${colors.text}cc;
            flex-grow: 1;
        }
        .brand {
            position: absolute;
            bottom: 40px;
            left: 80px;
            font-size: 24px;
            font-weight: 600;
            color: ${colors.accent};
        }
        .accent-bar {
            width: 100px;
            height: 6px;
            background: ${colors.accent};
            margin-bottom: 30px;
        }
        .cta-button {
            display: inline-block;
            background: ${colors.accent};
            color: ${colors.background};
            padding: 20px 40px;
            font-size: 28px;
            font-weight: 600;
            border-radius: 8px;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <div class="slide-number">${slideNumber}/${totalSlides}</div>

    ${!isFirstSlide ? '<div class="accent-bar"></div>' : ''}

    <div class="headline">${headline}</div>

    ${body ? `<div class="body">${body.replace(/\n/g, '<br>')}</div>` : ''}

    ${isLastSlide ? '<div class="cta-button">Link in Comments →</div>' : ''}

    <div class="brand">${brandName.toUpperCase()}</div>
</body>
</html>
`;
}

/**
 * Generate carousel (outputs HTML for each slide).
 * In production, would use Puppeteer to render to images and compile PDF.
 */
async function generateCarousel(briefPath, options = {}) {
    const theme = options.theme || 'dark';
    const brand = options.brand || 'enora';
    const outputDir = options.output || path.join(SKILL_DIR, 'data', 'generated');

    // Get colors
    const brandColors = BRAND_COLORS[brand] || BRAND_COLORS.enora;
    const colors = brandColors[theme] || brandColors.dark;

    // Parse brief
    const brief = parseBrief(briefPath);

    console.log(`\nGenerating carousel for: ${brief.title || 'Untitled'}`);
    console.log(`Slides: ${brief.slides.length}`);
    console.log(`Theme: ${theme}`);
    console.log(`Brand: ${brand}`);

    // Ensure output directory
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    // Generate HTML for each slide
    const slideFiles = [];
    for (let i = 0; i < brief.slides.length; i++) {
        const html = generateSlideHTML(
            brief.slides[i],
            i + 1,
            brief.slides.length,
            colors,
            brand
        );

        const fileName = `slide_${String(i + 1).padStart(2, '0')}.html`;
        const filePath = path.join(outputDir, fileName);
        fs.writeFileSync(filePath, html);
        slideFiles.push(filePath);
    }

    console.log(`\nGenerated ${slideFiles.length} slide HTML files in: ${outputDir}`);
    console.log('\nTo convert to images, use Puppeteer:');
    console.log('  const browser = await puppeteer.launch();');
    console.log('  const page = await browser.newPage();');
    console.log('  await page.setViewport({ width: 1080, height: 1080 });');
    console.log('  await page.goto(`file://${slidePath}`);');
    console.log('  await page.screenshot({ path: outputPath });');

    return {
        title: brief.title,
        slides: brief.slides.length,
        outputDir,
        files: slideFiles
    };
}

// CLI
if (require.main === module) {
    const args = process.argv.slice(2);

    if (args.length === 0 || args.includes('--help')) {
        console.log(`
Carousel Generator - Generate LinkedIn carousel from content brief

Usage:
  node carousel_generator.js <brief.md> [options]

Options:
  --theme     dark|light (default: dark)
  --brand     Brand slug (default: enora)
  --output    Output directory

Example:
  node carousel_generator.js content_brief.md --theme dark --brand enora
`);
        process.exit(0);
    }

    const briefPath = args[0];
    const options = {};

    for (let i = 1; i < args.length; i++) {
        if (args[i] === '--theme' && args[i + 1]) {
            options.theme = args[++i];
        } else if (args[i] === '--brand' && args[i + 1]) {
            options.brand = args[++i];
        } else if (args[i] === '--output' && args[i + 1]) {
            options.output = args[++i];
        }
    }

    generateCarousel(briefPath, options)
        .then(result => {
            console.log('\nCarousel generation complete!');
        })
        .catch(err => {
            console.error('Error:', err.message);
            process.exit(1);
        });
}

module.exports = { generateCarousel, parseBrief };
