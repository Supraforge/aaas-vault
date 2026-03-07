#!/usr/bin/env node
/**
 * Batch Asset Generator from Content Brief
 *
 * Reads a content brief markdown file and generates all specified visual assets.
 * Each campaign starts FRESH - will warn if output folder already exists.
 *
 * Usage:
 *   node batch_from_brief.js <brief.md>              # Warns if folder exists
 *   node batch_from_brief.js <brief.md> --dry-run   # Preview what would be generated
 *   node batch_from_brief.js <brief.md> --clean     # Delete existing folder first
 *   node batch_from_brief.js <brief.md> --overwrite # Overwrite existing files
 *
 * The brief must contain a "## Visual Specification" section with:
 * - Format & Dimensions table
 * - Theme & Style table
 * - Screenshot Requirements table (if applicable)
 *
 * Outputs are saved to: assets/brand/campaigns/<campaign-name>/
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Parse command line arguments
const briefPath = process.argv[2];
const dryRun = process.argv.includes('--dry-run');
const cleanFirst = process.argv.includes('--clean');
const overwrite = process.argv.includes('--overwrite');

if (!briefPath || briefPath.startsWith('--')) {
    console.error('Usage: node batch_from_brief.js <path_to_brief.md> [options]');
    console.error('\nOptions:');
    console.error('  --dry-run    Preview what would be generated without executing');
    console.error('  --clean      Delete existing campaign folder before generating');
    console.error('  --overwrite  Proceed even if folder exists (overwrites files)');
    console.error('\nExample: node batch_from_brief.js context/content_briefs/2025-02-15_website-launch.md --clean');
    process.exit(1);
}

// Helper to delete folder recursively
function deleteFolderRecursive(folderPath) {
    if (fs.existsSync(folderPath)) {
        fs.readdirSync(folderPath).forEach((file) => {
            const curPath = path.join(folderPath, file);
            if (fs.lstatSync(curPath).isDirectory()) {
                deleteFolderRecursive(curPath);
            } else {
                fs.unlinkSync(curPath);
            }
        });
        fs.rmdirSync(folderPath);
    }
}

// Check if folder exists and has files
function checkExistingFolder(folderPath) {
    if (!fs.existsSync(folderPath)) return { exists: false, fileCount: 0 };

    const files = fs.readdirSync(folderPath);
    const pngFiles = files.filter(f => f.endsWith('.png'));
    return { exists: true, fileCount: files.length, pngCount: pngFiles.length };
}

// Get the directory of this script for relative paths to other scripts
const scriptsDir = __dirname;
const projectRoot = path.resolve(scriptsDir, '../../..');

// =============================================================================
// MARKDOWN PARSING UTILITIES
// =============================================================================

function parseMarkdownTable(content, sectionName) {
    // Find the section
    const sectionRegex = new RegExp(`### ${sectionName}[\\s\\S]*?\\|[\\s\\S]*?(?=###|##|$)`, 'i');
    const sectionMatch = content.match(sectionRegex);

    if (!sectionMatch) return {};

    const section = sectionMatch[0];
    const lines = section.split('\n').filter(line => line.trim().startsWith('|'));

    if (lines.length < 3) return {};

    const result = {};
    // Skip header and separator rows
    for (let i = 2; i < lines.length; i++) {
        const cells = lines[i].split('|').map(c => c.trim()).filter(c => c);
        if (cells.length >= 2) {
            const key = cells[0].replace(/\*\*/g, '').trim();
            const value = cells[1].trim();
            result[key] = value;
        }
    }

    return result;
}

function parseCarouselSlides(content) {
    const slides = [];
    const slideRegex = /### Slide (\d+):?\s*([^\n]*)\n([\s\S]*?)(?=### Slide|\n---|\n##|$)/gi;

    let match;
    while ((match = slideRegex.exec(content)) !== null) {
        const slideNum = parseInt(match[1]);
        const slideTitle = match[2].trim();
        const slideContent = match[3];

        const tableData = {};
        const tableLines = slideContent.split('\n').filter(line => line.trim().startsWith('|'));

        for (let i = 2; i < tableLines.length; i++) {
            const cells = tableLines[i].split('|').map(c => c.trim()).filter(c => c);
            if (cells.length >= 2) {
                const key = cells[0].replace(/\*\*/g, '').trim();
                const value = cells[1].trim();
                tableData[key] = value;
            }
        }

        slides.push({
            number: slideNum,
            title: slideTitle,
            ...tableData
        });
    }

    return slides;
}

function extractCampaignName(content) {
    // Try to get from Campaign Meta table
    const metaTable = parseMarkdownTable(content, 'Campaign Meta') ||
                      parseMarkdownTable(content.replace('## Campaign Meta', '### Campaign Meta'), 'Campaign Meta');

    // Look for Campaign Name in the table
    for (const [key, value] of Object.entries(metaTable)) {
        if (key.toLowerCase().includes('campaign name')) {
            // Convert to kebab-case
            return value.toLowerCase()
                .replace(/[^a-z0-9\s]/g, '')
                .replace(/\s+/g, '-')
                .substring(0, 50);
        }
    }

    // Fallback: extract from title
    const titleMatch = content.match(/^# Content Brief:\s*(.+)$/m);
    if (titleMatch) {
        return titleMatch[1].toLowerCase()
            .replace(/[^a-z0-9\s]/g, '')
            .replace(/\s+/g, '-')
            .substring(0, 50);
    }

    return 'campaign-' + Date.now();
}

function extractScreenshotRequirements(content) {
    const screenshots = [];
    const sectionMatch = content.match(/### Screenshot Requirements[\s\S]*?(?=###|---|\n##|$)/i);

    if (!sectionMatch) return screenshots;

    const lines = sectionMatch[0].split('\n').filter(line => line.trim().startsWith('|'));

    // Skip header and separator
    for (let i = 2; i < lines.length; i++) {
        const cells = lines[i].split('|').map(c => c.trim()).filter(c => c);
        if (cells.length >= 3) {
            screenshots.push({
                name: cells[0],
                section: cells[1],
                theme: cells[2].toLowerCase()
            });
        }
    }

    return screenshots;
}

function extractLinks(content) {
    const links = {};
    const linksSection = content.match(/## Links & Tracking[\s\S]*?(?=##|$)/i);

    if (linksSection) {
        const tableData = parseMarkdownTable(linksSection[0].replace('## Links', '### Links'), 'Links');
        Object.assign(links, tableData);

        // Also look in the main table format
        const lines = linksSection[0].split('\n').filter(line => line.trim().startsWith('|'));
        for (let i = 2; i < lines.length; i++) {
            const cells = lines[i].split('|').map(c => c.trim()).filter(c => c);
            if (cells.length >= 2) {
                const key = cells[0].replace(/\*\*/g, '').trim();
                const value = cells[1].trim();
                links[key] = value;
            }
        }
    }

    return links;
}

// =============================================================================
// ASSET GENERATION
// =============================================================================

function runCommand(cmd, description) {
    console.log(`\n📦 ${description}`);
    console.log(`   Command: ${cmd}`);

    if (dryRun) {
        console.log('   [DRY RUN - Not executed]');
        return true;
    }

    try {
        execSync(cmd, {
            cwd: projectRoot,
            stdio: 'inherit'
        });
        console.log('   ✅ Success');
        return true;
    } catch (error) {
        console.error(`   ❌ Failed: ${error.message}`);
        return false;
    }
}

async function generateAssets(briefPath) {
    console.log('═══════════════════════════════════════════════════════════════');
    console.log('  BATCH ASSET GENERATOR FROM CONTENT BRIEF');
    console.log('═══════════════════════════════════════════════════════════════');
    console.log(`\nReading brief: ${briefPath}`);

    if (!fs.existsSync(briefPath)) {
        console.error(`\n❌ Brief file not found: ${briefPath}`);
        process.exit(1);
    }

    const content = fs.readFileSync(briefPath, 'utf8');

    // Parse brief
    const campaignName = extractCampaignName(content);
    const formatAndDimensions = parseMarkdownTable(content, 'Format & Dimensions');
    const themeAndStyle = parseMarkdownTable(content, 'Theme & Style');
    const screenshotReqs = extractScreenshotRequirements(content);
    const carouselSlides = parseCarouselSlides(content);
    const links = extractLinks(content);

    console.log('\n📋 BRIEF SUMMARY');
    console.log('─────────────────────────────────────────────────────────────────');
    console.log(`Campaign: ${campaignName}`);
    console.log(`Format: ${formatAndDimensions['Type'] || 'Unknown'}`);
    console.log(`Dimensions: ${formatAndDimensions['Dimensions'] || '1200x1200'}`);
    console.log(`Theme: ${themeAndStyle['Theme'] || 'dark'}`);
    console.log(`Device Mockup: ${themeAndStyle['Device Mockup'] || 'None'}`);
    console.log(`Screenshots needed: ${screenshotReqs.length}`);
    console.log(`Carousel slides: ${carouselSlides.length}`);
    console.log(`Landing page: ${links['Landing Page'] || 'N/A'}`);

    // Setup output directory
    const outputDir = path.join(projectRoot, 'assets/brand/campaigns', campaignName);
    const screenshotsDir = path.join(outputDir, 'screenshots');

    console.log(`\n📁 Output directory: ${outputDir}`);

    // Check if folder already exists with assets
    const folderStatus = checkExistingFolder(outputDir);

    if (folderStatus.exists && folderStatus.fileCount > 0) {
        console.log(`\n⚠️  Campaign folder already exists with ${folderStatus.fileCount} files (${folderStatus.pngCount} images)`);

        if (cleanFirst) {
            console.log('🧹 --clean flag: Deleting existing folder...');
            if (!dryRun) {
                deleteFolderRecursive(outputDir);
                console.log('   Folder deleted.');
            } else {
                console.log('   [DRY RUN - Would delete folder]');
            }
        } else if (overwrite) {
            console.log('📝 --overwrite flag: Will overwrite existing files.');
        } else {
            console.log('\n❌ Refusing to overwrite existing campaign assets.');
            console.log('   To proceed, use one of these options:');
            console.log('     --clean     Delete existing folder and start fresh');
            console.log('     --overwrite Proceed and overwrite existing files');
            console.log('     --dry-run   Preview what would be generated\n');
            process.exit(1);
        }
    }

    if (!dryRun) {
        fs.mkdirSync(outputDir, { recursive: true });
        fs.mkdirSync(screenshotsDir, { recursive: true });
    }

    const results = {
        screenshots: [],
        mockups: [],
        branded: [],
        errors: []
    };

    // ==========================================================================
    // STEP 1: Capture Screenshots (if website URL provided)
    // ==========================================================================

    const websiteUrl = links['Landing Page'];
    const theme = (themeAndStyle['Theme'] || 'dark').toLowerCase();

    if (websiteUrl && websiteUrl.startsWith('http')) {
        console.log('\n\n🖥️  STEP 1: CAPTURING WEBSITE SCREENSHOTS');
        console.log('─────────────────────────────────────────────────────────────────');

        const screenshotScript = path.join(scriptsDir, 'screenshot_sections.js');

        if (fs.existsSync(screenshotScript)) {
            const cmd = `node "${screenshotScript}" "${websiteUrl}" "${screenshotsDir}" "${theme}"`;
            if (runCommand(cmd, `Capturing ${theme} theme screenshots`)) {
                results.screenshots.push(`${theme} theme screenshots`);
            } else {
                results.errors.push('Screenshot capture failed');
            }
        } else {
            console.log('   ⚠️  Screenshot script not found, skipping...');
        }
    }

    // ==========================================================================
    // STEP 2: Generate Mockups
    // ==========================================================================

    console.log('\n\n🎨 STEP 2: GENERATING MOCKUPS');
    console.log('─────────────────────────────────────────────────────────────────');

    const deviceMockup = (themeAndStyle['Device Mockup'] || '').toLowerCase();
    const backgroundStyle = (themeAndStyle['Background Style'] || '').toLowerCase();

    // Desktop screenshot paths
    const heroScreenshot = path.join(screenshotsDir, `hero_${theme}.png`);
    const mobileScreenshot = path.join(screenshotsDir, `mobile_${theme}.png`);
    const stepScreenshot = path.join(screenshotsDir, `step_section_${theme}.png`);

    // Mac + iPhone Combined Mockup
    if (deviceMockup.includes('mac') && deviceMockup.includes('iphone')) {
        const mockupScript = path.join(scriptsDir, 'create_mac_iphone_mockup.js');
        const outputPath = path.join(outputDir, 'mockup_mac_iphone.png');

        if (fs.existsSync(mockupScript)) {
            const cmd = `node "${mockupScript}" "${heroScreenshot}" "${mobileScreenshot}" "${outputPath}" "${theme}"`;
            if (runCommand(cmd, 'Creating Mac + iPhone combined mockup')) {
                results.mockups.push('Mac + iPhone mockup');
            }
        }
    }

    // Browser Mockup
    if (deviceMockup.includes('browser')) {
        const mockupScript = path.join(scriptsDir, 'create_browser_mockup.js');
        const outputPath = path.join(outputDir, 'mockup_browser.png');

        if (fs.existsSync(mockupScript)) {
            const cmd = `node "${mockupScript}" "${heroScreenshot}" "${outputPath}" "${theme}"`;
            if (runCommand(cmd, 'Creating browser window mockup')) {
                results.mockups.push('Browser mockup');
            }
        }
    }

    // Gradient Background Mockup
    if (backgroundStyle.includes('gradient')) {
        const mockupScript = path.join(scriptsDir, 'create_gradient_mockup.js');
        const gradientType = backgroundStyle.includes('gold') ? 'gold' :
                            backgroundStyle.includes('blue') ? 'blue' : 'mixed';
        const outputPath = path.join(outputDir, `mockup_gradient_${gradientType}.png`);

        if (fs.existsSync(mockupScript)) {
            const cmd = `node "${mockupScript}" "${heroScreenshot}" "${outputPath}" "${gradientType}"`;
            if (runCommand(cmd, `Creating ${gradientType} gradient mockup`)) {
                results.mockups.push(`Gradient ${gradientType} mockup`);
            }
        }
    }

    // ==========================================================================
    // STEP 3: Generate Carousel Slides (if applicable)
    // ==========================================================================

    if (carouselSlides.length > 0) {
        console.log('\n\n📊 STEP 3: GENERATING CAROUSEL SLIDES');
        console.log('─────────────────────────────────────────────────────────────────');

        for (const slide of carouselSlides) {
            console.log(`\n   Slide ${slide.number}: ${slide.title || slide['Key Point'] || slide['Headline'] || 'Untitled'}`);

            const slideVisual = (slide['Visual'] || '').toLowerCase();
            const slideOutputBase = path.join(outputDir, `slide_${String(slide.number).padStart(2, '0')}`);

            // Determine which mockup style to use based on visual description
            if (slideVisual.includes('mac') && slideVisual.includes('iphone')) {
                // Use Mac + iPhone mockup
                const mockupScript = path.join(scriptsDir, 'create_mac_iphone_mockup.js');
                const outputPath = `${slideOutputBase}_mac_iphone.png`;

                if (fs.existsSync(mockupScript) && !dryRun && fs.existsSync(heroScreenshot)) {
                    const cmd = `node "${mockupScript}" "${heroScreenshot}" "${mobileScreenshot}" "${outputPath}" "${theme}"`;
                    runCommand(cmd, `Slide ${slide.number}: Mac + iPhone mockup`);
                }
            } else if (slideVisual.includes('screenshot') || slideVisual.includes('step')) {
                // Use gradient mockup with step section screenshot
                const mockupScript = path.join(scriptsDir, 'create_gradient_mockup.js');
                const inputScreenshot = slideVisual.includes('step') ? stepScreenshot : heroScreenshot;
                const outputPath = `${slideOutputBase}_gradient.png`;

                if (fs.existsSync(mockupScript)) {
                    const cmd = `node "${mockupScript}" "${inputScreenshot}" "${outputPath}" "gold"`;
                    runCommand(cmd, `Slide ${slide.number}: Gradient screenshot mockup`);
                }
            } else if (slideVisual.includes('logo') || slideVisual.includes('cta')) {
                // CTA slide - generate with AI or use template
                console.log(`   📝 Note: Slide ${slide.number} is a CTA/Logo slide - use AI generation or brand template`);
            } else {
                console.log(`   ⚠️  Visual type not recognized: "${slide['Visual'] || 'none specified'}"`);
            }
        }
    }

    // ==========================================================================
    // STEP 4: Add Logo Branding
    // ==========================================================================

    console.log('\n\n🏷️  STEP 4: ADDING LOGO BRANDING');
    console.log('─────────────────────────────────────────────────────────────────');

    // Try to get logo path from brief first (Logo Path field), then fall back to brand detection
    const logoPathFromBrief = themeAndStyle['Logo Path'];
    let logoPath;
    let logoFile;

    if (logoPathFromBrief && !logoPathFromBrief.includes('[')) {
        // Use explicit logo path from brief
        logoPath = path.join(projectRoot, logoPathFromBrief);
        logoFile = path.basename(logoPathFromBrief);
    } else {
        // Fall back to brand detection
        const brand = (themeAndStyle['Brand'] || '').toUpperCase();
        const logoVariant = theme === 'dark' ? 'dark' : '';

        if (!brand || brand.includes('[')) {
            console.log('   ⚠️  No brand specified in brief. Skipping logo branding.');
            console.log('   Add "Brand" field to Theme & Style section, or use --brand flag when creating brief.');
            results.errors.push('No brand specified - logo branding skipped');
            logoPath = null;
        } else {
            logoFile = brand.includes('ENORA')
                ? `enora-logo${logoVariant ? '-' + logoVariant : ''}.svg`
                : `supra-forge-logo${logoVariant ? '-' + logoVariant : ''}.svg`;
            logoPath = path.join(projectRoot, 'website/assets', logoFile);
        }
    }

    const compositeScript = path.join(scriptsDir, 'composite_logo.js');

    if (logoPath && fs.existsSync(compositeScript)) {
        if (!fs.existsSync(logoPath)) {
            console.log(`\n   ❌ Logo file not found: ${logoPath}`);
            console.log(`   Expected: ${logoFile}`);
            console.log(`   Check that the logo exists or update the brief's Logo Path field.`);
            results.errors.push(`Logo not found: ${logoFile}`);
        } else {
            // Find all generated mockups and add logo
            if (!dryRun && fs.existsSync(outputDir)) {
                const files = fs.readdirSync(outputDir).filter(f => f.endsWith('.png') && !f.includes('_branded'));

                for (const file of files) {
                    const inputPath = path.join(outputDir, file);
                    const outputPath = path.join(outputDir, file.replace('.png', '_branded.png'));

                    const cmd = `node "${compositeScript}" "${inputPath}" "${logoPath}" "${outputPath}" "bottom-left" "0.16"`;
                    if (runCommand(cmd, `Branding: ${file}`)) {
                        results.branded.push(file.replace('.png', '_branded.png'));
                    }
                }
            } else if (dryRun) {
                console.log('   [DRY RUN - Would brand all generated mockups]');
            }
        }
    }

    // ==========================================================================
    // SUMMARY
    // ==========================================================================

    console.log('\n\n═══════════════════════════════════════════════════════════════');
    console.log('  GENERATION COMPLETE');
    console.log('═══════════════════════════════════════════════════════════════');
    console.log(`\n📁 Output directory: ${outputDir}`);
    console.log(`\n✅ Screenshots captured: ${results.screenshots.length}`);
    console.log(`✅ Mockups generated: ${results.mockups.length}`);
    console.log(`✅ Branded assets: ${results.branded.length}`);

    if (results.errors.length > 0) {
        console.log(`\n❌ Errors: ${results.errors.length}`);
        results.errors.forEach(e => console.log(`   - ${e}`));
    }

    // List generated files
    if (!dryRun && fs.existsSync(outputDir)) {
        console.log('\n📄 Generated files:');
        const allFiles = fs.readdirSync(outputDir);
        allFiles.filter(f => f.endsWith('.png')).forEach(f => console.log(`   - ${f}`));
    }

    console.log('\n');
}

// Run
generateAssets(briefPath);
