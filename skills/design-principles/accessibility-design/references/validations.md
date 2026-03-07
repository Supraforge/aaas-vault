# Accessibility Design - Validations

## Image Missing Alt Text

### **Id**
missing-alt-text
### **Severity**
error
### **Type**
regex
### **Pattern**
<img(?![^>]*alt=)[^>]*>
### **Message**
Image is missing alt attribute. Screen readers cannot describe this image.
### **Fix Action**
Add alt='description' for informative images or alt='' for decorative images
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
  - *.vue
  - *.svelte
### **Test Cases**
  #### **Should Match**
    - <img src="photo.jpg">
    - <img src="icon.png" class="icon">
    - <img src="/images/hero.webp" width="100">
  #### **Should Not Match**
    - <img src="photo.jpg" alt="Team photo">
    - <img src="decorative.png" alt="">
    - <img alt="Logo" src="logo.svg">

## Empty Alt on Linked Image

### **Id**
empty-alt-on-link-image
### **Severity**
error
### **Type**
regex
### **Pattern**
<a[^>]*href[^>]*>\s*<img[^>]*alt=""[^>]*>\s*</a>
### **Message**
Linked image has empty alt. Screen readers announce as 'link' with no context.
### **Fix Action**
Add descriptive alt text explaining the link destination
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <a href="/"><img src="logo.png" alt=""></a>
    - <a href="/products"><img alt="" src="shop.jpg" /></a>
  #### **Should Not Match**
    - <a href="/"><img src="logo.png" alt="Home"></a>
    - <img alt="" src="decorative.png">

## Focus Outline Removed Without Alternative

### **Id**
outline-none-without-alternative
### **Severity**
error
### **Type**
regex
### **Pattern**
outline:\s*(none|0)(?![^}]*outline(?:-offset)?:)
### **Message**
Focus outline removed without providing alternative focus indicator.
### **Fix Action**
Add :focus-visible styles with visible focus indicator (outline, box-shadow, or border)
### **Applies To**
  - *.css
  - *.scss
  - *.tsx
  - *.jsx
### **Test Cases**
  #### **Should Match**
    - button:focus { outline: none; }
    - *:focus { outline: 0; }
  #### **Should Not Match**
    - button:focus { outline: none; box-shadow: 0 0 0 2px blue; }
    - a:focus-visible { outline: 2px solid blue; }

## Positive Tabindex Value

### **Id**
positive-tabindex
### **Severity**
error
### **Type**
regex
### **Pattern**
tabindex="[1-9][0-9]*"|tabindex={[1-9][0-9]*}
### **Message**
Positive tabindex creates unpredictable tab order. Use only 0 or -1.
### **Fix Action**
Change to tabindex='0' (adds to tab order) or tabindex='-1' (programmatic focus only)
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
  - *.vue
### **Test Cases**
  #### **Should Match**
    - tabindex="5"
    - tabindex={10}
    - tabindex="100"
  #### **Should Not Match**
    - tabindex="0"
    - tabindex="-1"
    - tabindex={0}

## Form Input Without Associated Label

### **Id**
input-without-label
### **Severity**
error
### **Type**
regex
### **Pattern**
<input(?![^>]*(?:aria-label|aria-labelledby|id="[^"]+"))[^>]*(?:type="(?:text|email|password|search|tel|url|number)")[^>]*>
### **Message**
Form input missing accessible label. Screen readers cannot identify this field.
### **Fix Action**
Add <label for='id'> or aria-label or aria-labelledby attribute
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <input type="text" name="email">
    - <input type="password" placeholder="Password">
  #### **Should Not Match**
    - <input type="text" id="email" aria-label="Email">
    - <input type="text" id="name" aria-labelledby="name-label">

## Button Without Accessible Text

### **Id**
button-without-text
### **Severity**
error
### **Type**
regex
### **Pattern**
<button[^>]*>\s*<(?:svg|img|i|span)[^>]*(?:/>|>[^<]*</(?:svg|img|i|span)>)\s*</button>
### **Message**
Button contains only icon/image with no accessible text.
### **Fix Action**
Add aria-label, visually-hidden text, or meaningful alt text to button
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <button><svg></svg></button>
    - <button><img src="icon.png" /></button>
    - <button><i class="icon-close"></i></button>
  #### **Should Not Match**
    - <button aria-label="Close"><svg></svg></button>
    - <button><svg></svg><span class="sr-only">Close</span></button>

## Aria-hidden on Interactive Element

### **Id**
aria-hidden-on-interactive
### **Severity**
error
### **Type**
regex
### **Pattern**
aria-hidden="true"[^>]*(?:onclick|href="|tabindex="0")|(?:onclick|href="|tabindex="0")[^>]*aria-hidden="true"
### **Message**
Interactive element hidden from screen readers but visible to sighted users.
### **Fix Action**
Remove aria-hidden or make element non-interactive
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <a href="/page" aria-hidden="true">Link</a>
    - <button aria-hidden="true" onclick="handleClick()">Click</button>
    - <div tabindex="0" aria-hidden="true" onclick="go()">Go</div>
  #### **Should Not Match**
    - <svg aria-hidden="true"></svg>
    - <span aria-hidden="true">decorative</span>

## Autoplay Media Without Muted

### **Id**
autoplay-without-muted
### **Severity**
error
### **Type**
regex
### **Pattern**
<(?:video|audio)[^>]*autoplay(?![^>]*muted)[^>]*>
### **Message**
Media autoplays with sound. Interferes with screen readers and startles users.
### **Fix Action**
Add 'muted' attribute or remove 'autoplay'
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <video autoplay src="video.mp4">
    - <audio autoplay>
  #### **Should Not Match**
    - <video autoplay muted src="video.mp4">
    - <video muted autoplay playsinline>

## Missing HTML Lang Attribute

### **Id**
missing-html-lang
### **Severity**
error
### **Type**
regex
### **Pattern**
<html(?![^>]*lang=)[^>]*>
### **Message**
HTML element missing lang attribute. Screen readers cannot determine pronunciation.
### **Fix Action**
Add lang attribute to html element, e.g., <html lang='en'>
### **Applies To**
  - *.html
  - index.html
  - layout.tsx
  - layout.jsx
### **Test Cases**
  #### **Should Match**
    - <html>
    - <html class="dark">
  #### **Should Not Match**
    - <html lang="en">
    - <html lang="es" dir="ltr">

## Role Button Without Keyboard Handler

### **Id**
role-button-no-keyboard
### **Severity**
error
### **Type**
regex
### **Pattern**
role="button"(?![^>]*(?:onkeydown|onkeypress|onkeyup))[^>]*>
### **Message**
Element has button role but no keyboard event handler. Keyboard users cannot activate.
### **Fix Action**
Add onKeyDown handler for Enter and Space keys, or use native <button> element
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <div role="button" onClick={handleClick}>Click</div>
    - <span role="button" tabindex="0">Action</span>
  #### **Should Not Match**
    - <div role="button" onClick={handleClick} onKeyDown={handleKey}>Click</div>
    - <button>Click</button>

## Potentially Low Contrast Text

### **Id**
low-contrast-text
### **Severity**
warning
### **Type**
regex
### **Pattern**
text-gray-[34]00|text-slate-[34]00|color:\s*#[9abc][9abc][9abc]|color:\s*#(?:ccc|ddd|eee)
### **Message**
Text color may fail WCAG contrast requirements (4.5:1 for normal text).
### **Fix Action**
Use darker text color. Check with contrast checker tool.
### **Applies To**
  - *.tsx
  - *.jsx
  - *.css
### **Test Cases**
  #### **Should Match**
    - text-gray-400
    - text-slate-300
    - color: #aaa
    - color: #ccc
  #### **Should Not Match**
    - text-gray-600
    - text-slate-700
    - color: #333

## Click Handler Without Keyboard Alternative

### **Id**
onclick-only-handler
### **Severity**
warning
### **Type**
regex
### **Pattern**
<div[^>]*onclick(?![^>]*(?:onkeydown|onkeypress|tabindex))[^>]*>
### **Message**
Div has click handler but no keyboard accessibility. Use button or add keyboard handler.
### **Fix Action**
Replace with <button>, or add tabindex='0' and onKeyDown handler
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <div onclick="handleClick()">Click me</div>
    - <div onClick={handler} className="btn">Action</div>
  #### **Should Not Match**
    - <div onclick="go()" tabindex="0" onkeydown="key(event)">Go</div>
    - <button onclick="go()">Go</button>

## Input With Placeholder But No Label

### **Id**
placeholder-only-label
### **Severity**
warning
### **Type**
regex
### **Pattern**
<input[^>]*placeholder="[^"]+(?:"[^>]*(?!aria-label|<label)[^>]*/?>|"[^>]*>(?!</label))
### **Message**
Input uses placeholder as only label. Placeholder disappears when typing.
### **Fix Action**
Add visible <label> or aria-label. Placeholder is a hint, not a label.
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <input placeholder="Email address" type="email" />
  #### **Should Not Match**
    - <input placeholder="you@example.com" aria-label="Email" />
    - <label for="email">Email</label><input id="email" placeholder="you@example.com" />

## No Skip Link to Main Content

### **Id**
missing-skip-link
### **Severity**
warning
### **Type**
regex
### **Pattern**
<body[^>]*>(?:(?!</a[^>]*#main).)*<main
### **Message**
Page has navigation before main content but no skip link.
### **Fix Action**
Add skip link as first focusable element: <a href='#main-content' class='skip-link'>Skip to content</a>
### **Applies To**
  - *.html
  - layout.tsx
  - layout.jsx
### **Test Cases**
  #### **Should Match**
    - <body><header><nav>...</nav></header><main>
  #### **Should Not Match**
    - <body><a href="#main" class="skip">Skip</a><header>...</header><main id="main">

## Required Field Indicated By Color Only

### **Id**
color-only-required
### **Severity**
warning
### **Type**
regex
### **Pattern**
<span[^>]*(?:class="[^"]*(?:text-red|color-red)[^"]*"|style="[^"]*color:\s*red[^"]*")[^>]*>\s*\*\s*</span>
### **Message**
Required field indicator uses only color. Colorblind users may miss it.
### **Fix Action**
Add text '(required)' or aria-describedby explaining the asterisk
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <span class="text-red-500">*</span>
    - <span style="color: red">*</span>
  #### **Should Not Match**
    - <span class="text-red-500" aria-hidden="true">*</span><span class="sr-only">required</span>

## Link Without Accessible Text

### **Id**
empty-link-text
### **Severity**
error
### **Type**
regex
### **Pattern**
<a[^>]*href[^>]*>\s*</a>|<a[^>]*href[^>]*>\s*<(?:svg|img|i)[^>]*/>\s*</a>
### **Message**
Link has no accessible text. Screen readers announce only 'link'.
### **Fix Action**
Add link text, aria-label, or alt text on image inside link
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <a href="/"></a>
    - <a href="/search"><svg></svg></a>
    - <a href="/home"><i class="icon-home" /></a>
  #### **Should Not Match**
    - <a href="/">Home</a>
    - <a href="/search" aria-label="Search"><svg></svg></a>
    - <a href="/home"><img src="home.png" alt="Home" /></a>

## Form Error Not Associated With Input

### **Id**
missing-form-error-association
### **Severity**
warning
### **Type**
regex
### **Pattern**
<(?:span|div|p)[^>]*(?:class="[^"]*error[^"]*"|role="alert")[^>]*>(?:(?!aria-describedby|aria-errormessage).)*</(?:span|div|p)>
### **Message**
Error message not programmatically associated with input.
### **Fix Action**
Connect error to input using aria-describedby='error-id' on input and id='error-id' on error message
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html

## Dialog Without Accessible Label

### **Id**
dialog-no-label
### **Severity**
error
### **Type**
regex
### **Pattern**
<(?:dialog|div[^>]*role="dialog")[^>]*(?!aria-label|aria-labelledby)[^>]*>
### **Message**
Dialog/modal missing accessible label. Screen readers cannot identify it.
### **Fix Action**
Add aria-labelledby pointing to dialog title, or aria-label
### **Applies To**
  - *.tsx
  - *.jsx
  - *.html
### **Test Cases**
  #### **Should Match**
    - <dialog>
    - <div role="dialog">
  #### **Should Not Match**
    - <dialog aria-labelledby="dialog-title">
    - <div role="dialog" aria-label="Confirm deletion">