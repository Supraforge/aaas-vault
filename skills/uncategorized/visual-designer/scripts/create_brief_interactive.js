#!/usr/bin/env node
/**
 * Interactive Content Brief Generator
 *
 * Asks minimal viable questions and generates a complete content brief.
 * Each campaign starts FRESH - no hardcoded defaults from previous campaigns.
 *
 * Usage:
 *   node create_brief_interactive.js                    # Full interactive mode
 *   node create_brief_interactive.js --brand supra-forge # Load brand presets
 *   node create_brief_interactive.js --json '{"...}'    # Automation mode
 *
 * Brand configs are loaded from: context/brand_configs/[brand].json
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

// =============================================================================
// CONFIGURATION - NO HARDCODED DEFAULTS
// =============================================================================

const scriptsDir = __dirname;
const projectRoot = path.resolve(scriptsDir, '../../..');
const brandConfigDir = path.join(projectRoot, 'context/brand_configs');

// Parse command line for --brand flag
function parseBrandArg() {
    const brandIdx = process.argv.indexOf('--brand');
    if (brandIdx > -1 && process.argv[brandIdx + 1]) {
        return process.argv[brandIdx + 1];
    }
    return null;
}

// Load brand config if specified
function loadBrandConfig(brandSlug) {
    if (!brandSlug) return null;

    const configPath = path.join(brandConfigDir, `${brandSlug}.json`);
    if (!fs.existsSync(configPath)) {
        console.error(`\n❌ Brand config not found: ${configPath}`);
        console.error(`\nAvailable brands:`);
        const configs = fs.readdirSync(brandConfigDir)
            .filter(f => f.endsWith('.json') && !f.startsWith('_'))
            .map(f => `  - ${f.replace('.json', '')}`);
        console.error(configs.join('\n'));
        process.exit(1);
    }

    try {
        return JSON.parse(fs.readFileSync(configPath, 'utf8'));
    } catch (error) {
        console.error(`\n❌ Error loading brand config: ${error.message}`);
        process.exit(1);
    }
}

// List available brands
function getAvailableBrands() {
    if (!fs.existsSync(brandConfigDir)) {
        return [];
    }
    return fs.readdirSync(brandConfigDir)
        .filter(f => f.endsWith('.json') && !f.startsWith('_'))
        .map(f => {
            const config = JSON.parse(fs.readFileSync(path.join(brandConfigDir, f), 'utf8'));
            return { slug: f.replace('.json', ''), name: config.brand_name };
        });
}

// Build questions dynamically based on brand config (or without)
function buildQuestions(brandConfig) {
    const brands = getAvailableBrands();
    const brandOptions = brands.length > 0
        ? brands.map(b => b.name)
        : ['[Enter brand name]'];

    return [
        {
            id: 'campaignName',
            question: 'Campaign name (e.g., "Website Launch", "Q1 Product Update")',
            required: true,
            default: null  // NO DEFAULT - must be entered
        },
        {
            id: 'brand',
            question: 'Brand',
            required: true,
            options: brandOptions,
            default: brandConfig?.brand_name || null  // Only default if --brand was used
        },
        {
            id: 'platform',
            question: 'Platform',
            required: true,
            options: ['LinkedIn', 'Twitter', 'Instagram', 'Multi-platform'],
            default: null  // NO DEFAULT
        },
        {
            id: 'format',
            question: 'Content format',
            required: true,
            options: ['Carousel (5 slides)', 'Carousel (10 slides)', 'Single Image', 'Video', 'Text-only'],
            default: null  // NO DEFAULT
        },
        {
            id: 'pillar',
            question: 'Content pillar',
            required: true,
            options: ['Educational', 'Thought Leadership', 'Product', 'Community'],
            default: null  // NO DEFAULT
        },
        {
            id: 'targetDate',
            question: 'Target publish date (YYYY-MM-DD)',
            required: false,
            default: () => {
                const d = new Date();
                d.setDate(d.getDate() + 7);
                return d.toISOString().split('T')[0];
            }
        },
        {
            id: 'landingPage',
            question: 'Landing page URL (REQUIRED)',
            required: true,
            default: brandConfig?.landing_page || null  // Only default if --brand was used
        },
        {
            id: 'audience',
            question: 'Primary audience (who is this content for?)',
            required: true,
            default: brandConfig?.default_audience || null  // Only default if --brand was used
        },
        {
            id: 'industry',
            question: 'Industry / vertical',
            required: true,
            default: brandConfig?.industry || null
        },
        {
            id: 'painPoints',
            question: 'Pain points to address (comma-separated, or press Enter to skip)',
            required: false,
            hint: brandConfig?.pain_points
                ? `Suggestions: ${brandConfig.pain_points.slice(0, 3).join(', ')}`
                : 'What problems does your audience face?',
            default: null  // NO DEFAULT
        },
        {
            id: 'desiredAction',
            question: 'What should the audience do after seeing this?',
            required: true,
            options: ['Visit website', 'Book demo', 'Download resource', 'Engage (like/comment)', 'Follow page'],
            default: null  // NO DEFAULT
        },
        {
            id: 'hook',
            question: 'Hook idea (the scroll-stopping first line)',
            required: true,
            default: null,  // NO DEFAULT
            hint: 'Use a bold claim, surprising stat, or relatable pain point'
        },
        {
            id: 'keyMessage',
            question: 'Key message or value proposition',
            required: true,
            default: null,  // NO DEFAULT
            hint: 'What\'s the ONE thing you want them to remember?'
        },
        {
            id: 'hashtags',
            question: 'Hashtags (comma-separated, 3-5 recommended)',
            required: false,
            hint: brandConfig?.hashtags
                ? `Brand suggestions: ${brandConfig.hashtags.slice(0, 3).join(' ')}`
                : 'Include mix of industry and niche tags',
            default: null  // NO DEFAULT
        },
        {
            id: 'theme',
            question: 'Visual theme',
            required: true,
            options: ['Dark', 'Light'],
            default: null  // NO DEFAULT
        },
        {
            id: 'deviceMockup',
            question: 'Device mockup style',
            required: false,
            options: ['Mac + iPhone', 'MacBook only', 'iPhone only', 'Browser window', 'None'],
            default: null  // NO DEFAULT
        },
        {
            id: 'backgroundStyle',
            question: 'Background style',
            required: false,
            options: ['Gradient Gold', 'Gradient Blue', 'Gradient Mixed', 'Studio', 'Solid'],
            default: null  // NO DEFAULT
        },
        {
            id: 'demoLink',
            question: 'Demo booking link (optional)',
            required: false,
            default: brandConfig?.demo_booking_url || null
        }
    ];
}

// =============================================================================
// BRIEF GENERATION
// =============================================================================

function generateBrief(answers, brandConfig) {
    const today = new Date().toISOString().split('T')[0];
    const campaignSlug = answers.campaignName.toLowerCase()
        .replace(/[^a-z0-9\s]/g, '')
        .replace(/\s+/g, '-');

    // Parse format for dimensions
    const isCarousel = answers.format.toLowerCase().includes('carousel');

    // Parse hashtags - use entered or empty
    const hashtagsRaw = answers.hashtags || '';
    const hashtags = hashtagsRaw.trim()
        ? hashtagsRaw.split(',').map(h => h.trim().startsWith('#') ? h.trim() : `#${h.trim()}`).join(' ')
        : '[YOUR_HASHTAGS]';

    // Parse pain points
    const painPointsRaw = answers.painPoints || '';
    const painPoints = painPointsRaw.trim()
        ? painPointsRaw.split(',').map(p => p.trim())
        : [];

    // Generate UTM
    const utmParams = `?utm_source=${answers.platform.toLowerCase()}&utm_medium=organic&utm_campaign=${campaignSlug}&utm_content=v1`;

    // Get logo paths from brand config or use placeholders
    const logoPath = brandConfig
        ? (answers.theme === 'Dark' ? brandConfig.logo_dark : brandConfig.logo_light)
        : '[YOUR_LOGO_PATH]';

    // Build the brief
    let brief = `# Content Brief: ${answers.campaignName}

> **Generated:** ${today} | **Status:** Draft
> **Brand:** ${answers.brand}

---

## Campaign Meta

| Field | Value |
| ----- | ----- |
| **Campaign Name** | ${answers.campaignName} |
| **Platform** | ${answers.platform} |
| **Format** | ${answers.format} |
| **Content Pillar** | ${answers.pillar} |
| **Target Date** | ${answers.targetDate} |
| **Status** | Draft |

---

## Target Audience

| Field | Value |
| ----- | ----- |
| **Primary Persona** | ${answers.audience} |
| **Industry** | ${answers.industry} |

### Pain Points to Address

`;

    if (painPoints.length > 0) {
        painPoints.forEach(pp => {
            brief += `- [x] ${pp}\n`;
        });
    } else {
        brief += `- [ ] [Define pain points for this campaign]\n`;
    }

    brief += `
### Desired Action

- [${answers.desiredAction.includes('website') ? 'x' : ' '}] Visit website
- [${answers.desiredAction.includes('demo') ? 'x' : ' '}] Book demo call
- [${answers.desiredAction.includes('Download') ? 'x' : ' '}] Download resource
- [${answers.desiredAction.includes('Engage') ? 'x' : ' '}] Engage (like/comment/share)
- [${answers.desiredAction.includes('Follow') ? 'x' : ' '}] Follow company page

---

## Copy

### Hook (First 2 Lines) — CRITICAL

\`\`\`
${answers.hook}

[Second line - build curiosity or expand on the hook]
\`\`\`

### Body

\`\`\`
${answers.keyMessage}

[Expand on the key message here...]

[Add supporting point or social proof]

[Transition to CTA]
\`\`\`

### Call to Action (CTA)

\`\`\`
${answers.desiredAction.includes('website') ? `See it in action → ${answers.landingPage}` : ''}
${answers.desiredAction.includes('demo') && answers.demoLink ? `Book a demo: ${answers.demoLink}` : ''}
\`\`\`

### Hashtags

\`\`\`
${hashtags}
\`\`\`

---

## Visual Specification

### Format & Dimensions

| Field | Value |
| ----- | ----- |
| **Type** | ${answers.format} |
| **Aspect Ratio** | 1:1 |
| **Dimensions** | 1200x1200 |

### Theme & Style

| Field | Value |
| ----- | ----- |
| **Theme** | ${answers.theme} |
| **Brand** | ${answers.brand} |
| **Device Mockup** | ${answers.deviceMockup || 'None'} |
| **Background Style** | ${answers.backgroundStyle || 'Solid'} |
| **Logo Path** | ${logoPath} |

### Screenshot Requirements

| Screenshot | Section | Theme |
| ---------- | ------- | ----- |
| Screenshot 1 | Hero | ${answers.theme} |
| Screenshot 2 | Key feature section | ${answers.theme} |
| Screenshot 3 | Mobile | ${answers.theme} |

---
`;

    // Add carousel slides if applicable
    if (isCarousel) {
        brief += `
## Carousel Slides

### Slide 1: Cover

| Field | Value |
| ----- | ----- |
| **Headline** | ${answers.hook.split('\n')[0]} |
| **Visual** | ${answers.deviceMockup || 'Device'} mockup, ${answers.theme.toLowerCase()} theme, ${(answers.backgroundStyle || 'gradient').toLowerCase()} background |

### Slide 2: Problem

| Field | Value |
| ----- | ----- |
| **Key Point** | [The problem your audience faces] |
| **Visual** | Icon or abstract visualization |

### Slide 3: Solution

| Field | Value |
| ----- | ----- |
| **Key Point** | ${answers.keyMessage.split('\n')[0]} |
| **Visual** | Screenshot of key feature |

### Slide 4: Benefit

| Field | Value |
| ----- | ----- |
| **Key Point** | [Key benefit or result] |
| **Visual** | Screenshot or data visualization |

### Slide 5: CTA

| Field | Value |
| ----- | ----- |
| **Summary** | ${answers.keyMessage.split('\n')[0]} |
| **CTA** | ${answers.desiredAction} → |
| **Visual** | ${answers.brand} logo centered |

---
`;
    }

    brief += `
## Links & Tracking

| Field | Value |
| ----- | ----- |
| **Landing Page** | ${answers.landingPage} |
| **Demo Booking** | ${answers.demoLink || 'N/A'} |
| **Resource Link** | N/A |

### UTM Parameters

\`\`\`
${utmParams}
\`\`\`

**Full tracked URL:**

\`\`\`
${answers.landingPage}${utmParams}
\`\`\`

---

## Asset Generation Commands

### 1. Capture Screenshots

\`\`\`bash
node skills/visual-designer/scripts/screenshot_sections.js "${answers.landingPage}" "./assets/brand/campaigns/${campaignSlug}/screenshots" "${answers.theme.toLowerCase()}"
\`\`\`

### 2. Generate Mockups

\`\`\`bash
node skills/visual-designer/scripts/batch_from_brief.js "context/content_briefs/${today}_${campaignSlug}.md" --clean
\`\`\`

---

## Pre-Publish Checklist

- [ ] Hook is compelling (stops the scroll)
- [ ] Copy matches brand voice
- [ ] Correct logo variant for background theme
- [ ] UTM parameters added to all links
- [ ] Image dimensions correct (1200x1200)
- [ ] No AI-generated text visible in images
- [ ] Mobile preview looks good
- [ ] Hashtags are relevant
- [ ] CTA is clear and actionable
- [ ] All links tested and working

---

## Notes

\`\`\`
${today}: Brief generated via interactive tool (fresh start, no carryover)
\`\`\`
`;

    return { brief, filename: `${today}_${campaignSlug}.md` };
}

// =============================================================================
// INTERACTIVE PROMPT
// =============================================================================

async function askQuestion(rl, q) {
    return new Promise((resolve) => {
        let prompt = `\n${q.question}`;

        if (q.options) {
            prompt += '\n  Options: ' + q.options.join(' | ');
        }
        if (q.hint) {
            prompt += `\n  (${q.hint})`;
        }
        if (q.default) {
            const defaultVal = typeof q.default === 'function' ? q.default() : q.default;
            prompt += `\n  [Default: ${defaultVal}]`;
        }
        if (q.required && !q.default) {
            prompt += '\n  ⚠️  REQUIRED';
        }

        prompt += '\n> ';

        rl.question(prompt, (answer) => {
            if (!answer.trim() && q.default) {
                resolve(typeof q.default === 'function' ? q.default() : q.default);
            } else if (!answer.trim() && q.required) {
                console.log('  ⚠️  This field is required. Please provide a value.');
                resolve(askQuestion(rl, q));
            } else {
                resolve(answer.trim());
            }
        });
    });
}

async function runInteractive(brandConfig) {
    console.log('\n═══════════════════════════════════════════════════════════════');
    console.log('  INTERACTIVE CONTENT BRIEF GENERATOR');
    console.log('  ⚠️  FRESH START - No defaults from previous campaigns');
    console.log('═══════════════════════════════════════════════════════════════');

    if (brandConfig) {
        console.log(`\n🏷️  Brand presets loaded: ${brandConfig.brand_name}`);
        console.log(`   Some fields will be pre-filled from brand config.`);
    } else {
        console.log('\n📝 No brand config loaded. All fields must be entered manually.');
        console.log('   Tip: Use --brand <slug> to load presets (e.g., --brand supra-forge)\n');
    }

    const questions = buildQuestions(brandConfig);

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const answers = {};

    for (const q of questions) {
        answers[q.id] = await askQuestion(rl, q);
    }

    rl.close();

    // Generate the brief
    const { brief, filename } = generateBrief(answers, brandConfig);

    // Save to file
    const outputDir = path.join(projectRoot, 'context/content_briefs');
    const outputPath = path.join(outputDir, filename);

    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    fs.writeFileSync(outputPath, brief);

    console.log('\n═══════════════════════════════════════════════════════════════');
    console.log('  BRIEF GENERATED SUCCESSFULLY');
    console.log('═══════════════════════════════════════════════════════════════');
    console.log(`\n📄 Saved to: ${outputPath}`);
    console.log('\nNext steps:');
    console.log('1. Review and refine the brief');
    console.log(`2. Run: node skills/visual-designer/scripts/batch_from_brief.js "${outputPath}" --clean`);
    console.log('\n');
}

// =============================================================================
// JSON INPUT MODE (for automation/Claude)
// =============================================================================

function runFromJson(jsonStr, brandConfig) {
    try {
        const answers = JSON.parse(jsonStr);
        const questions = buildQuestions(brandConfig);

        // Only fill in defaults from brand config, not hardcoded values
        for (const q of questions) {
            if (!answers[q.id] && q.default && brandConfig) {
                // Only use default if it came from brand config
                answers[q.id] = typeof q.default === 'function' ? q.default() : q.default;
            }
        }

        // Validate required fields
        const missing = questions
            .filter(q => q.required && !answers[q.id])
            .map(q => q.id);

        if (missing.length > 0) {
            console.error(`\n❌ Missing required fields: ${missing.join(', ')}`);
            process.exit(1);
        }

        const { brief, filename } = generateBrief(answers, brandConfig);

        const outputDir = path.join(projectRoot, 'context/content_briefs');
        const outputPath = path.join(outputDir, filename);

        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        fs.writeFileSync(outputPath, brief);

        console.log(`Brief saved to: ${outputPath}`);
        return outputPath;
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

// =============================================================================
// MAIN
// =============================================================================

// Load brand config if --brand flag provided
const brandSlug = parseBrandArg();
const brandConfig = loadBrandConfig(brandSlug);

const jsonArg = process.argv.indexOf('--json');
if (jsonArg > -1 && process.argv[jsonArg + 1]) {
    runFromJson(process.argv[jsonArg + 1], brandConfig);
} else {
    runInteractive(brandConfig);
}
