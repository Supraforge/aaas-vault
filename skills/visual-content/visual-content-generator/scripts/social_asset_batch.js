#!/usr/bin/env node
/**
 * Social Asset Batch Generator - Generate assets for multiple platforms.
 *
 * Usage:
 *   node social_asset_batch.js <brief.md> --platforms "linkedin,twitter,instagram"
 */

const fs = require('fs');
const path = require('path');

// Skill directories
const SKILL_DIR = path.dirname(__dirname);
const PROJECT_ROOT = path.resolve(SKILL_DIR, '../..');

// Platform specifications
const PLATFORM_SPECS = {
    linkedin: {
        post: { width: 1200, height: 1200, name: 'linkedin_post' },
        story: { width: 1080, height: 1920, name: 'linkedin_story' },
        banner: { width: 1584, height: 396, name: 'linkedin_banner' }
    },
    twitter: {
        post: { width: 1200, height: 675, name: 'twitter_post' },
        header: { width: 1500, height: 500, name: 'twitter_header' }
    },
    instagram: {
        post: { width: 1080, height: 1080, name: 'instagram_post' },
        story: { width: 1080, height: 1920, name: 'instagram_story' },
        reel: { width: 1080, height: 1920, name: 'instagram_reel' }
    }
};

// Brand colors
const BRAND_COLORS = {
    enora: {
        dark: { bg: '#0F172A', text: '#F8FAFC', accent: '#d4a853' },
        light: { bg: '#F8FAFC', text: '#0F172A', accent: '#d4a853' }
    }
};

/**
 * Parse content brief for asset generation.
 */
function parseBrief(briefPath) {
    if (!fs.existsSync(briefPath)) {
        throw new Error(`Brief not found: ${briefPath}`);
    }

    const content = fs.readFileSync(briefPath, 'utf-8');

    // Extract key information
    const brief = {
        title: '',
        hook: '',
        body: '',
        cta: '',
        hashtags: []
    };

    // Extract title
    const titleMatch = content.match(/^#\s+(.+)$/m);
    if (titleMatch) brief.title = titleMatch[1];

    // Extract hook (first 2 lines after title)
    const hookMatch = content.match(/## Hook\s*\n(.+)/i);
    if (hookMatch) brief.hook = hookMatch[1];

    // Extract hashtags
    const hashtagMatch = content.match(/#\w+/g);
    if (hashtagMatch) brief.hashtags = [...new Set(hashtagMatch)];

    return brief;
}

/**
 * Generate HTML template for a social asset.
 */
function generateAssetHTML(brief, platform, format, colors) {
    const spec = PLATFORM_SPECS[platform]?.[format];
    if (!spec) return null;

    const { width, height } = spec;
    const isVertical = height > width;
    const fontSize = isVertical ? '48px' : '56px';

    return `
<!DOCTYPE html>
<html>
<head>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            width: ${width}px;
            height: ${height}px;
            background: ${colors.bg};
            color: ${colors.text};
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: ${isVertical ? '80px' : '60px'};
            text-align: center;
        }
        .headline {
            font-size: ${fontSize};
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 30px;
            color: ${colors.accent};
        }
        .subheadline {
            font-size: ${isVertical ? '32px' : '28px'};
            line-height: 1.5;
            color: ${colors.text}cc;
            max-width: 80%;
        }
        .brand {
            position: absolute;
            bottom: 40px;
            font-size: 24px;
            font-weight: 600;
            color: ${colors.accent};
        }
        .accent-line {
            width: 80px;
            height: 4px;
            background: ${colors.accent};
            margin: 30px 0;
        }
    </style>
</head>
<body>
    <div class="headline">${brief.title || 'Your Headline Here'}</div>
    <div class="accent-line"></div>
    <div class="subheadline">${brief.hook || 'Your compelling message here'}</div>
    <div class="brand">ENORA</div>
</body>
</html>
`;
}

/**
 * Generate batch of social assets.
 */
async function generateBatch(briefPath, options = {}) {
    const platforms = options.platforms || ['linkedin', 'twitter', 'instagram'];
    const theme = options.theme || 'dark';
    const brand = options.brand || 'enora';
    const outputDir = options.output || path.join(SKILL_DIR, 'data', 'generated', 'social_batch');

    // Get colors
    const colors = BRAND_COLORS[brand]?.[theme] || BRAND_COLORS.enora.dark;

    // Parse brief
    const brief = parseBrief(briefPath);

    console.log(`\nGenerating social assets for: ${brief.title || 'Untitled'}`);
    console.log(`Platforms: ${platforms.join(', ')}`);
    console.log(`Theme: ${theme}`);

    // Ensure output directory
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    const results = [];

    for (const platform of platforms) {
        const specs = PLATFORM_SPECS[platform];
        if (!specs) {
            console.log(`  Unknown platform: ${platform}, skipping`);
            continue;
        }

        console.log(`\n  ${platform}:`);

        for (const [format, spec] of Object.entries(specs)) {
            const html = generateAssetHTML(brief, platform, format, colors);
            if (!html) continue;

            const fileName = `${spec.name}_${theme}.html`;
            const filePath = path.join(outputDir, fileName);
            fs.writeFileSync(filePath, html);

            console.log(`    - ${spec.name}: ${spec.width}x${spec.height}`);
            results.push({
                platform,
                format,
                dimensions: `${spec.width}x${spec.height}`,
                file: filePath
            });
        }
    }

    console.log(`\nGenerated ${results.length} asset templates in: ${outputDir}`);
    console.log('\nTo render to images, use Puppeteer or a headless browser.');

    return {
        brief: brief.title,
        outputDir,
        assets: results
    };
}

// CLI
if (require.main === module) {
    const args = process.argv.slice(2);

    if (args.length === 0 || args.includes('--help')) {
        console.log(`
Social Asset Batch Generator

Usage:
  node social_asset_batch.js <brief.md> [options]

Options:
  --platforms   Comma-separated list (default: linkedin,twitter,instagram)
  --theme       dark|light (default: dark)
  --brand       Brand slug (default: enora)
  --output      Output directory

Example:
  node social_asset_batch.js brief.md --platforms "linkedin,twitter" --theme dark
`);
        process.exit(0);
    }

    const briefPath = args[0];
    const options = {};

    for (let i = 1; i < args.length; i++) {
        if (args[i] === '--platforms' && args[i + 1]) {
            options.platforms = args[++i].split(',').map(p => p.trim());
        } else if (args[i] === '--theme' && args[i + 1]) {
            options.theme = args[++i];
        } else if (args[i] === '--brand' && args[i + 1]) {
            options.brand = args[++i];
        } else if (args[i] === '--output' && args[i + 1]) {
            options.output = args[++i];
        }
    }

    generateBatch(briefPath, options)
        .then(result => {
            console.log('\nBatch generation complete!');
        })
        .catch(err => {
            console.error('Error:', err.message);
            process.exit(1);
        });
}

module.exports = { generateBatch, parseBrief };
