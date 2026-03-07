# WordPress Gutenberg Blocks - Complete Reference

Complete reference for ALL WordPress core Gutenberg blocks with attributes and supports for creating landing pages and styled content.

## Block Syntax

All blocks use HTML comments with JSON attributes:
```html
<!-- wp:blockname {"attribute":"value"} -->
<html-content>
<!-- /wp:blockname -->
```

---

# LAYOUT BLOCKS

## Cover Block (`core/cover`)
Full-width sections with background colors/images. Perfect for hero sections.

**Attributes:**
- `url` (string): Background image URL
- `useFeaturedImage` (boolean, default: false)
- `id` (number): Media ID
- `alt` (string): Alt text
- `hasParallax` (boolean, default: false): Fixed background
- `isRepeated` (boolean, default: false): Repeat background
- `dimRatio` (number, default: 100): Overlay opacity 0-100
- `overlayColor` (string): Color preset slug
- `customOverlayColor` (string): Hex color
- `backgroundType` (string, default: "image"): "image" or "video"
- `focalPoint` (object): {x: 0.5, y: 0.5}
- `minHeight` (number)
- `minHeightUnit` (string): "px", "vh", "%"
- `gradient` (string): Gradient preset
- `customGradient` (string): CSS gradient
- `contentPosition` (string): "top left", "center center", etc.
- `isDark` (boolean, default: true): Dark mode text

**Supports:** anchor, align, shadow, padding, margin, blockGap, border (color, radius, style, width), color (heading, text), typography, layout, duotone filter

```html
<!-- wp:cover {"overlayColor":"black","minHeight":500,"minHeightUnit":"px","isDark":false,"style":{"spacing":{"padding":{"top":"80px","bottom":"80px"}}}} -->
<div class="wp-block-cover is-light" style="min-height:500px;padding-top:80px;padding-bottom:80px">
  <span aria-hidden="true" class="wp-block-cover__background has-black-background-color has-background-dim-100 has-background-dim"></span>
  <div class="wp-block-cover__inner-container">
    <!-- Inner content -->
  </div>
</div>
<!-- /wp:cover -->
```

---

## Group Block (`core/group`)
Container for grouping blocks with backgrounds and spacing.

**Attributes:**
- `tagName` (string, default: "div"): HTML tag
- `templateLock` (string|boolean): "all", "insert", "contentOnly", false

**Supports:** align (wide, full), anchor, ariaLabel, background (backgroundImage, backgroundSize), color (gradients, heading, button, link), shadow, padding, margin, blockGap, minHeight, border, position (sticky), typography, layout

```html
<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px"}}},"backgroundColor":"white","layout":{"type":"constrained"}} -->
<div class="wp-block-group has-white-background-color has-background" style="padding-top:60px;padding-bottom:60px">
  <!-- Inner content -->
</div>
<!-- /wp:group -->
```

**Layout Types:**
- `{"type":"constrained"}` - Centered with max-width
- `{"type":"flex","flexWrap":"nowrap"}` - Horizontal flex
- `{"type":"flex","orientation":"vertical"}` - Vertical flex
- `{"type":"default"}` - Flow layout

---

## Columns Block (`core/columns`)
Multi-column layouts.

**Attributes:**
- `verticalAlignment` (string): "top", "center", "bottom"
- `isStackedOnMobile` (boolean, default: true)
- `templateLock` (string|boolean)

**Supports:** anchor, align (wide, full), color (gradients, link, heading, button), blockGap (horizontal, vertical), margin, padding, border, typography, shadow

```html
<!-- wp:columns {"style":{"spacing":{"blockGap":{"left":"30px"}}}} -->
<div class="wp-block-columns">
  <!-- wp:column -->
  <div class="wp-block-column">Content</div>
  <!-- /wp:column -->
</div>
<!-- /wp:columns -->
```

---

## Column Block (`core/column`)
Single column within columns.

**Attributes:**
- `verticalAlignment` (string): "top", "center", "bottom"
- `width` (string): "33.33%", "50%", "66.66%", etc.
- `templateLock` (string|boolean)

**Supports:** anchor, color (gradients, heading, button, link), shadow, blockGap, padding, border, typography, layout

```html
<!-- wp:column {"width":"50%","style":{"spacing":{"padding":{"top":"30px","bottom":"30px","left":"30px","right":"30px"}},"border":{"radius":"8px"}},"backgroundColor":"white"} -->
<div class="wp-block-column has-white-background-color has-background" style="border-radius:8px;padding:30px">
  Content
</div>
<!-- /wp:column -->
```

---

## Media & Text Block (`core/media-text`)
Side-by-side media and content.

**Attributes:**
- `align` (string, default: "none")
- `mediaAlt` (string): Alt text
- `mediaPosition` (string, default: "left"): "left" or "right"
- `mediaId` (number)
- `mediaUrl` (string)
- `mediaType` (string): "image" or "video"
- `mediaWidth` (number, default: 50): Percentage
- `mediaSizeSlug` (string)
- `isStackedOnMobile` (boolean, default: true)
- `verticalAlignment` (string): "top", "center", "bottom"
- `imageFill` (boolean)
- `focalPoint` (object)
- `useFeaturedImage` (boolean, default: false)

**Supports:** anchor, align (wide, full), border, color (gradients, heading, link), margin, padding, typography

```html
<!-- wp:media-text {"mediaPosition":"right","mediaWidth":40,"verticalAlignment":"center"} -->
<div class="wp-block-media-text alignwide has-media-on-the-right is-stacked-on-mobile is-vertically-aligned-center" style="grid-template-columns:auto 40%">
  <div class="wp-block-media-text__content">
    <!-- Text content -->
  </div>
  <figure class="wp-block-media-text__media">
    <img src="image.jpg" alt=""/>
  </figure>
</div>
<!-- /wp:media-text -->
```

---

# TEXT BLOCKS

## Heading Block (`core/heading`)

**Attributes:**
- `textAlign` (string): "left", "center", "right"
- `content` (rich-text)
- `level` (number, default: 2): 1-6
- `placeholder` (string)

**Supports:** align (wide, full), anchor, className, splitting, border, color (gradients, link), margin, padding, typography (fontSize, lineHeight, fontFamily, fontWeight, fontStyle, textTransform, textDecoration, letterSpacing, fitText)

```html
<!-- wp:heading {"textAlign":"center","level":1,"style":{"typography":{"fontSize":"48px"}},"textColor":"white"} -->
<h1 class="wp-block-heading has-text-align-center has-white-color has-text-color" style="font-size:48px">Heading</h1>
<!-- /wp:heading -->
```

---

## Paragraph Block (`core/paragraph`)

**Attributes:**
- `align` (string): "left", "center", "right"
- `content` (rich-text)
- `dropCap` (boolean, default: false)
- `placeholder` (string)
- `direction` (string): "ltr", "rtl"

**Supports:** anchor, border, color (gradients, link), margin, padding, typography (fontSize, lineHeight, fontFamily, textDecoration, fontStyle, fontWeight, letterSpacing, textTransform, fitText)

```html
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"20px"}},"textColor":"white"} -->
<p class="has-text-align-center has-white-color has-text-color" style="font-size:20px">Paragraph text</p>
<!-- /wp:paragraph -->
```

---

## List Block (`core/list`)

**Attributes:**
- `ordered` (boolean, default: false)
- `values` (string): HTML content
- `type` (string): List type (1, a, A, i, I)
- `start` (number): Starting number
- `reversed` (boolean)
- `placeholder` (string)

**Supports:** anchor, border, typography, color (gradients, link), margin, padding

```html
<!-- wp:list {"ordered":false,"style":{"typography":{"fontSize":"16px"}}} -->
<ul class="wp-block-list" style="font-size:16px">
  <!-- wp:list-item -->
  <li>Item 1</li>
  <!-- /wp:list-item -->
  <!-- wp:list-item -->
  <li>Item 2</li>
  <!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
```

---

## Quote Block (`core/quote`)

**Attributes:**
- `value` (string): Quote HTML
- `citation` (rich-text): Attribution
- `textAlign` (string)

**Styles:** default, plain

**Supports:** anchor, align (left, right, wide, full), background, border, minHeight, typography, color (gradients, heading, link), padding, margin, blockGap

```html
<!-- wp:quote {"className":"is-style-default"} -->
<blockquote class="wp-block-quote is-style-default">
  <!-- wp:paragraph -->
  <p>Quote text here</p>
  <!-- /wp:paragraph -->
  <cite>— Author Name</cite>
</blockquote>
<!-- /wp:quote -->
```

---

## Pullquote Block (`core/pullquote`)
Highlighted quote with visual emphasis.

**Attributes:**
- `value` (rich-text)
- `citation` (rich-text)
- `textAlign` (string)

**Supports:** anchor, align (left, right, wide, full), background, color (gradients, link), minHeight, margin, padding, typography, border

```html
<!-- wp:pullquote {"textAlign":"center"} -->
<figure class="wp-block-pullquote has-text-align-center">
  <blockquote>
    <p>Important quote text</p>
    <cite>Source</cite>
  </blockquote>
</figure>
<!-- /wp:pullquote -->
```

---

## Code Block (`core/code`)

**Attributes:**
- `content` (rich-text): Code content

**Supports:** align (wide), anchor, typography, margin, padding, border (radius, color, width, style), color (text, background, gradients)

```html
<!-- wp:code {"backgroundColor":"black","textColor":"white"} -->
<pre class="wp-block-code has-black-background-color has-white-color has-text-color has-background"><code>const hello = "world";</code></pre>
<!-- /wp:code -->
```

---

## Preformatted Block (`core/preformatted`)
Monospace text preserving spacing.

**Supports:** anchor, color (gradients, link), spacing (margin, padding), typography

---

## Verse Block (`core/verse`)
Poetry and verse with preserved formatting.

**Supports:** anchor, color (gradients, link, background, text), typography, spacing (margin, padding), border

---

## Details Block (`core/details`)
Collapsible content (accordion).

**Attributes:**
- `showContent` (boolean, default: false): Open by default
- `summary` (rich-text): Toggle text
- `name` (string): Group name for exclusive open
- `placeholder` (string)

**Supports:** align (wide, full), anchor, color (gradients, link), border, margin, padding, blockGap, typography, layout

```html
<!-- wp:details -->
<details class="wp-block-details">
  <summary>Click to expand</summary>
  <!-- wp:paragraph -->
  <p>Hidden content here</p>
  <!-- /wp:paragraph -->
</details>
<!-- /wp:details -->
```

---

# INTERACTIVE BLOCKS

## Buttons Block (`core/buttons`)
Container for multiple buttons.

**Supports:** anchor, align (wide, full), color (gradients), blockGap (horizontal, vertical), padding, margin, typography, border, layout (flex)

```html
<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"30px"}}}} -->
<div class="wp-block-buttons" style="margin-top:30px">
  <!-- Button blocks here -->
</div>
<!-- /wp:buttons -->
```

---

## Button Block (`core/button`)

**Attributes:**
- `tagName` (string, default: "a"): "a" or "button"
- `type` (string, default: "button")
- `textAlign` (string)
- `url` (string): Link URL
- `title` (string): Link title
- `text` (rich-text): Button text
- `linkTarget` (string): "_blank" for new tab
- `rel` (string): Link rel attribute
- `placeholder` (string)
- `backgroundColor` (string): Color preset
- `textColor` (string): Color preset
- `gradient` (string): Gradient preset
- `width` (number): 25, 50, 75, 100 (percentage)

**Styles:** fill (default), outline

**Supports:** anchor, color (gradients), typography, shadow, padding (horizontal, vertical), border

```html
<!-- wp:button {"backgroundColor":"vivid-cyan-blue","textColor":"white","style":{"typography":{"fontSize":"18px"},"border":{"radius":"50px"}}} -->
<div class="wp-block-button has-custom-font-size" style="font-size:18px">
  <a class="wp-block-button__link has-vivid-cyan-blue-background-color has-white-color has-text-color has-background wp-element-button" href="https://example.com" style="border-radius:50px">Button Text</a>
</div>
<!-- /wp:button -->

<!-- Outline style -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline">
  <a class="wp-block-button__link wp-element-button" href="#">Outline Button</a>
</div>
<!-- /wp:button -->

<!-- Full width -->
<!-- wp:button {"width":100} -->
```

---

## Table Block (`core/table`)

**Attributes:**
- `hasFixedLayout` (boolean, default: true)
- `caption` (rich-text)
- `head` (array): Header rows
- `body` (array): Body rows
- `foot` (array): Footer rows

**Styles:** regular (default), stripes

**Supports:** anchor, align, color (gradients), margin, padding, typography, border

```html
<!-- wp:table {"hasFixedLayout":true,"className":"is-style-stripes"} -->
<figure class="wp-block-table is-style-stripes">
  <table class="has-fixed-layout">
    <thead>
      <tr><th>Header 1</th><th>Header 2</th></tr>
    </thead>
    <tbody>
      <tr><td>Cell 1</td><td>Cell 2</td></tr>
    </tbody>
  </table>
</figure>
<!-- /wp:table -->
```

---

## Search Block (`core/search`)

**Attributes:**
- `label` (string)
- `showLabel` (boolean, default: true)
- `placeholder` (string)
- `width` (number)
- `widthUnit` (string)
- `buttonText` (string)
- `buttonPosition` (string, default: "button-outside"): "button-outside", "button-inside", "no-button"
- `buttonUseIcon` (boolean, default: false)
- `isSearchFieldHidden` (boolean, default: false)

**Supports:** align (left, center, right), color (gradients), typography, border, margin

```html
<!-- wp:search {"label":"Search","buttonText":"Search","buttonPosition":"button-inside"} /-->
```

---

# MEDIA BLOCKS

## Image Block (`core/image`)

**Attributes:**
- `url` (string): Image URL
- `alt` (string): Alt text
- `caption` (rich-text)
- `lightbox` (object): {enabled: boolean}
- `title` (string)
- `href` (string): Link URL
- `rel` (string)
- `linkClass` (string)
- `id` (number): Media ID
- `width` (string)
- `height` (string)
- `aspectRatio` (string): "16/9", "4/3", "1/1", etc.
- `scale` (string): "cover", "contain"
- `sizeSlug` (string): "thumbnail", "medium", "large", "full"
- `linkDestination` (string): "none", "media", "attachment", "custom"
- `linkTarget` (string)

**Styles:** default, rounded

**Supports:** align (left, center, right, wide, full), anchor, filter (duotone), margin, border (color, radius, width), shadow

```html
<!-- wp:image {"align":"center","sizeSlug":"large","linkDestination":"none","className":"is-style-rounded"} -->
<figure class="wp-block-image aligncenter size-large is-style-rounded">
  <img src="image.jpg" alt="Description"/>
  <figcaption class="wp-element-caption">Caption text</figcaption>
</figure>
<!-- /wp:image -->
```

---

## Gallery Block (`core/gallery`)

**Attributes:**
- `images` (array): Image data
- `ids` (array): Media IDs
- `columns` (number, 1-8)
- `caption` (rich-text)
- `imageCrop` (boolean, default: true)
- `randomOrder` (boolean, default: false)
- `fixedHeight` (boolean, default: true)
- `linkTarget` (string)
- `linkTo` (string): "none", "media", "attachment"
- `sizeSlug` (string, default: "large")
- `allowResize` (boolean, default: false)
- `aspectRatio` (string, default: "auto")

**Supports:** anchor, align, border (radius, color, width, style), blockGap (horizontal, vertical), margin, padding, color (background, gradients), layout (flex)

```html
<!-- wp:gallery {"columns":3,"linkTo":"none","sizeSlug":"large"} -->
<figure class="wp-block-gallery has-nested-images columns-3">
  <!-- wp:image blocks here -->
</figure>
<!-- /wp:gallery -->
```

---

## Video Block (`core/video`)

**Attributes:**
- `autoplay` (boolean)
- `caption` (rich-text)
- `controls` (boolean, default: true)
- `id` (number)
- `loop` (boolean)
- `muted` (boolean)
- `poster` (string): Preview image URL
- `preload` (string, default: "metadata"): "auto", "metadata", "none"
- `src` (string): Video URL
- `playsInline` (boolean)
- `tracks` (array): Caption tracks

**Supports:** anchor, align, margin, padding

```html
<!-- wp:video {"id":123} -->
<figure class="wp-block-video">
  <video controls src="video.mp4" poster="poster.jpg"></video>
  <figcaption class="wp-element-caption">Caption</figcaption>
</figure>
<!-- /wp:video -->
```

---

## Audio Block (`core/audio`)

**Attributes:**
- `src` (string)
- `caption` (rich-text)
- `id` (number)
- `autoplay` (boolean)
- `loop` (boolean)
- `preload` (string): "auto", "metadata", "none"

**Supports:** anchor, align, margin, padding

```html
<!-- wp:audio {"id":456} -->
<figure class="wp-block-audio">
  <audio controls src="audio.mp3"></audio>
</figure>
<!-- /wp:audio -->
```

---

## File Block (`core/file`)

**Attributes:**
- `id` (number)
- `href` (string): File URL
- `fileName` (rich-text)
- `textLinkHref` (string)
- `textLinkTarget` (string)
- `showDownloadButton` (boolean, default: true)
- `downloadButtonText` (rich-text)
- `displayPreview` (boolean)
- `previewHeight` (number, default: 600)

**Supports:** anchor, align, margin, padding, color (gradients, link), border

```html
<!-- wp:file {"id":789,"href":"document.pdf"} -->
<div class="wp-block-file">
  <a href="document.pdf">Document Name</a>
  <a href="document.pdf" class="wp-block-file__button wp-element-button" download>Download</a>
</div>
<!-- /wp:file -->
```

---

## Embed Block (`core/embed`)
Embed content from external sources.

**Attributes:**
- `url` (string): URL to embed
- `caption` (rich-text)
- `type` (string): Provider type
- `providerNameSlug` (string): youtube, twitter, vimeo, etc.
- `allowResponsive` (boolean, default: true)
- `responsive` (boolean, default: false)

**Supports:** align, margin

```html
<!-- wp:embed {"url":"https://youtube.com/watch?v=xxx","type":"video","providerNameSlug":"youtube"} -->
<figure class="wp-block-embed is-type-video is-provider-youtube">
  <div class="wp-block-embed__wrapper">
    https://youtube.com/watch?v=xxx
  </div>
</figure>
<!-- /wp:embed -->
```

---

# DESIGN BLOCKS

## Separator Block (`core/separator`)

**Attributes:**
- `opacity` (string, default: "alpha-channel")
- `tagName` (string, default: "hr"): "hr" or "div"

**Styles:** default, wide, dots

**Supports:** anchor, align (center, wide, full), color (gradients, background), margin

```html
<!-- wp:separator {"className":"is-style-wide"} -->
<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide"/>
<!-- /wp:separator -->

<!-- Colored separator -->
<!-- wp:separator {"backgroundColor":"vivid-cyan-blue","className":"is-style-wide"} -->
<hr class="wp-block-separator has-vivid-cyan-blue-background-color has-background is-style-wide"/>
<!-- /wp:separator -->
```

---

## Spacer Block (`core/spacer`)

**Attributes:**
- `height` (string, default: "100px")
- `width` (string)

**Supports:** anchor, margin

```html
<!-- wp:spacer {"height":"50px"} -->
<div style="height:50px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->
```

---

# WIDGET BLOCKS

## Social Icons Block (`core/social-links`)

**Attributes:**
- `iconColor` (string)
- `customIconColor` (string)
- `iconBackgroundColor` (string)
- `customIconBackgroundColor` (string)
- `openInNewTab` (boolean, default: false)
- `showLabels` (boolean, default: false)
- `size` (string)

**Styles:** default, logos-only, pill-shape

**Supports:** align (left, center, right), anchor, layout (flex), color (background, gradients), blockGap, margin, padding, border

```html
<!-- wp:social-links {"iconColor":"white","iconBackgroundColor":"vivid-cyan-blue","className":"is-style-default"} -->
<ul class="wp-block-social-links has-icon-color has-icon-background-color is-style-default">
  <!-- wp:social-link {"url":"https://twitter.com/example","service":"twitter"} /-->
  <!-- wp:social-link {"url":"https://facebook.com/example","service":"facebook"} /-->
</ul>
<!-- /wp:social-links -->
```

---

## Latest Posts Block (`core/latest-posts`)

**Attributes:**
- `categories` (array)
- `selectedAuthor` (number)
- `postsToShow` (number, default: 5)
- `displayPostContent` (boolean, default: false)
- `displayPostContentRadio` (string, default: "excerpt"): "excerpt" or "full_post"
- `excerptLength` (number, default: 55)
- `displayAuthor` (boolean, default: false)
- `displayPostDate` (boolean, default: false)
- `postLayout` (string, default: "list"): "list" or "grid"
- `columns` (number, default: 3)
- `order` (string, default: "desc")
- `orderBy` (string, default: "date")
- `displayFeaturedImage` (boolean, default: false)
- `featuredImageAlign` (string): "left", "center", "right"
- `featuredImageSizeSlug` (string, default: "thumbnail")
- `addLinkToFeaturedImage` (boolean, default: false)

**Supports:** align, color (gradients, link), margin, padding, typography, border

```html
<!-- wp:latest-posts {"postsToShow":3,"displayPostDate":true,"displayFeaturedImage":true,"postLayout":"grid","columns":3} /-->
```

---

## Custom HTML Block (`core/html`)

**Attributes:**
- `content` (string): Raw HTML

```html
<!-- wp:html -->
<div class="custom-element">Custom HTML content</div>
<!-- /wp:html -->
```

---

## Shortcode Block (`core/shortcode`)

**Attributes:**
- `text` (string): Shortcode text

```html
<!-- wp:shortcode -->
[contact-form-7 id="123"]
<!-- /wp:shortcode -->
```

---

# COLOR PRESETS

Available color slugs for `backgroundColor`, `textColor`, `overlayColor`:

| Slug | Color | Hex |
|------|-------|-----|
| `black` | Black | #000000 |
| `white` | White | #ffffff |
| `vivid-cyan-blue` | Blue | #0693e3 |
| `vivid-green-cyan` | Green | #00d084 |
| `vivid-red` | Red | #cf2e2e |
| `luminous-vivid-orange` | Orange | #ff6900 |
| `luminous-vivid-amber` | Yellow | #fcb900 |
| `pale-pink` | Pink | #f78da7 |
| `pale-cyan-blue` | Light Blue | #8ed1fc |
| `cyan-bluish-gray` | Gray | #abb8c3 |
| `vivid-purple` | Purple | #9b51e0 |

---

# GRADIENT PRESETS

| Slug | Description |
|------|-------------|
| `vivid-cyan-blue-to-vivid-purple` | Blue to Purple |
| `light-green-cyan-to-vivid-green-cyan` | Light to Dark Green |
| `luminous-vivid-amber-to-luminous-vivid-orange` | Yellow to Orange |
| `luminous-vivid-orange-to-vivid-red` | Orange to Red |
| `very-light-gray-to-cyan-bluish-gray` | Light to Dark Gray |
| `cool-to-warm-spectrum` | Rainbow spectrum |
| `blush-light-purple` | Pink to Purple |
| `blush-bordeaux` | Pink to Dark Red |
| `luminous-dusk` | Orange to Purple |
| `pale-ocean` | Blue to Cyan |
| `electric-grass` | Green to Yellow |
| `midnight` | Dark Blue to Black |

---

# LANDING PAGE PATTERNS

## Hero Section
```html
<!-- wp:cover {"overlayColor":"black","minHeight":500,"minHeightUnit":"px","style":{"spacing":{"padding":{"top":"80px","bottom":"80px"}}}} -->
<div class="wp-block-cover" style="min-height:500px;padding-top:80px;padding-bottom:80px">
  <span aria-hidden="true" class="wp-block-cover__background has-black-background-color has-background-dim-100 has-background-dim"></span>
  <div class="wp-block-cover__inner-container">
    <!-- wp:heading {"textAlign":"center","level":1,"textColor":"white"} -->
    <h1 class="wp-block-heading has-text-align-center has-white-color has-text-color">Hero Headline</h1>
    <!-- /wp:heading -->
    <!-- wp:paragraph {"align":"center","textColor":"white"} -->
    <p class="has-text-align-center has-white-color has-text-color">Subheadline text</p>
    <!-- /wp:paragraph -->
    <!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
    <div class="wp-block-buttons">
      <!-- wp:button {"backgroundColor":"vivid-cyan-blue"} -->
      <div class="wp-block-button"><a class="wp-block-button__link has-vivid-cyan-blue-background-color has-background wp-element-button" href="#">Primary CTA</a></div>
      <!-- /wp:button -->
    </div>
    <!-- /wp:buttons -->
  </div>
</div>
<!-- /wp:cover -->
```

## Feature Cards Section
```html
<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px"}}},"backgroundColor":"pale-cyan-blue","layout":{"type":"constrained"}} -->
<div class="wp-block-group has-pale-cyan-blue-background-color has-background" style="padding-top:60px;padding-bottom:60px">
  <!-- wp:heading {"textAlign":"center"} -->
  <h2 class="wp-block-heading has-text-align-center">Features</h2>
  <!-- /wp:heading -->
  <!-- wp:columns {"style":{"spacing":{"blockGap":{"left":"30px"}}}} -->
  <div class="wp-block-columns">
    <!-- wp:column {"style":{"spacing":{"padding":{"top":"30px","bottom":"30px","left":"30px","right":"30px"}},"border":{"radius":"8px"}},"backgroundColor":"white"} -->
    <div class="wp-block-column has-white-background-color has-background" style="border-radius:8px;padding:30px">
      <!-- wp:heading {"level":3} --><h3>Feature 1</h3><!-- /wp:heading -->
      <!-- wp:paragraph --><p>Description</p><!-- /wp:paragraph -->
    </div>
    <!-- /wp:column -->
    <!-- Repeat columns -->
  </div>
  <!-- /wp:columns -->
</div>
<!-- /wp:group -->
```

## Comparison Cards
```html
<!-- wp:columns -->
<div class="wp-block-columns">
  <!-- wp:column {"style":{"spacing":{"padding":"30px"},"border":{"radius":"8px"}},"backgroundColor":"vivid-red","textColor":"white"} -->
  <div class="wp-block-column has-white-color has-vivid-red-background-color has-text-color has-background" style="border-radius:8px;padding:30px">
    <!-- wp:heading {"level":3,"textColor":"white"} --><h3 class="has-white-color has-text-color">Problem</h3><!-- /wp:heading -->
    <!-- wp:list --><ul><li>Pain point 1</li><li>Pain point 2</li></ul><!-- /wp:list -->
  </div>
  <!-- /wp:column -->
  <!-- wp:column {"style":{"spacing":{"padding":"30px"},"border":{"radius":"8px"}},"backgroundColor":"vivid-green-cyan","textColor":"white"} -->
  <div class="wp-block-column has-white-color has-vivid-green-cyan-background-color has-text-color has-background" style="border-radius:8px;padding:30px">
    <!-- wp:heading {"level":3,"textColor":"white"} --><h3 class="has-white-color has-text-color">Solution</h3><!-- /wp:heading -->
    <!-- wp:paragraph --><p>Solution description</p><!-- /wp:paragraph -->
  </div>
  <!-- /wp:column -->
</div>
<!-- /wp:columns -->
```

## CTA Section
```html
<!-- wp:cover {"overlayColor":"vivid-cyan-blue","minHeight":300,"style":{"spacing":{"padding":{"top":"60px","bottom":"60px"}}}} -->
<div class="wp-block-cover" style="padding-top:60px;padding-bottom:60px;min-height:300px">
  <span aria-hidden="true" class="wp-block-cover__background has-vivid-cyan-blue-background-color has-background-dim-100 has-background-dim"></span>
  <div class="wp-block-cover__inner-container">
    <!-- wp:heading {"textAlign":"center","textColor":"white"} -->
    <h2 class="has-text-align-center has-white-color has-text-color">Call to Action</h2>
    <!-- /wp:heading -->
    <!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
    <div class="wp-block-buttons">
      <!-- wp:button {"backgroundColor":"white","textColor":"vivid-cyan-blue"} -->
      <div class="wp-block-button"><a class="wp-block-button__link has-vivid-cyan-blue-color has-white-background-color has-text-color has-background wp-element-button" href="#">Get Started</a></div>
      <!-- /wp:button -->
    </div>
    <!-- /wp:buttons -->
  </div>
</div>
<!-- /wp:cover -->
```

## FAQ with Details
```html
<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px"}}},"backgroundColor":"white","layout":{"type":"constrained"}} -->
<div class="wp-block-group has-white-background-color has-background" style="padding-top:60px;padding-bottom:60px">
  <!-- wp:heading {"textAlign":"center"} -->
  <h2 class="has-text-align-center">FAQ</h2>
  <!-- /wp:heading -->
  <!-- wp:details -->
  <details class="wp-block-details">
    <summary>Question 1?</summary>
    <!-- wp:paragraph --><p>Answer to question 1.</p><!-- /wp:paragraph -->
  </details>
  <!-- /wp:details -->
  <!-- wp:details -->
  <details class="wp-block-details">
    <summary>Question 2?</summary>
    <!-- wp:paragraph --><p>Answer to question 2.</p><!-- /wp:paragraph -->
  </details>
  <!-- /wp:details -->
</div>
<!-- /wp:group -->
```

---

# TIPS

1. **Use Cover blocks** for full-width colored/image sections
2. **Use Group blocks** with `layout: constrained` for centered content
3. **Always add padding** via `style.spacing.padding`
4. **Use Columns** for feature grids (3-4 columns work best)
5. **Add border-radius** (`8px`-`12px`) for modern card look
6. **Use contrasting colors** for CTA buttons
7. **Consistent spacing**: 60px section padding, 30px element gaps
8. **Mobile-first**: Columns stack automatically on mobile (`isStackedOnMobile: true`)
9. **Color contrast**: Use white text on dark backgrounds, dark on light
10. **Use presets**: Color slugs are more reliable than custom hex values
