# Block Debugging Guide

## "Invalid block content" Error

**Symptoms:**
- Block shows "This block contains unexpected or invalid content"
- Block recovery dialog appears after editing

**Common Causes:**

1. **Changed save() output without deprecation**
   ```jsx
   // Old save (in production)
   save() { return <div className="old-class">...</div> }

   // New save (causes invalid block)
   save() { return <div className="new-class">...</div> }
   ```

   **Fix:** Add deprecation entry
   ```jsx
   const deprecated = [{
       attributes: { /* old attributes */ },
       save() { return <div className="old-class">...</div> }
   }];
   ```

2. **Whitespace differences**
   - Extra spaces in JSX
   - Different line breaks

   **Fix:** Ensure save() produces identical output

3. **Attribute serialization mismatch**
   - Attribute type changed
   - Source selector changed

## Block Attributes Not Saving

**Symptoms:**
- Values don't persist after save
- Inspector controls show blank

**Common Causes:**

1. **Missing source definition for HTML attributes**
   ```json
   // Wrong - expects value in comment delimiter
   "content": { "type": "string" }

   // Right - extracts from HTML
   "content": {
       "type": "string",
       "source": "html",
       "selector": ".my-content"
   }
   ```

2. **Type mismatch**
   ```json
   // Wrong - mediaId should be number
   "mediaId": { "type": "string" }

   // Right
   "mediaId": { "type": "number" }
   ```

3. **Selector doesn't match save() output**
   ```json
   "title": {
       "source": "html",
       "selector": ".title"  // Must match exact class in save()
   }
   ```

## Block Not Appearing in Inserter

**Symptoms:**
- Block not in block library
- Can't search for block

**Common Causes:**

1. **PHP registration failed**
   - Check PHP error logs
   - Verify file paths in `register_block_type()`

2. **Wrong category**
   ```json
   "category": "nonexistent"  // Must be valid category
   ```

3. **Build not run**
   - Run `npm run build`
   - Check build/ directory exists

4. **JavaScript error**
   - Check browser console for errors
   - Verify imports are correct

## Styles Not Applying

**Symptoms:**
- Editor looks different from frontend
- Styles missing in one or both

**Common Causes:**

1. **Missing asset in block.json**
   ```json
   "editorStyle": "file:./index.css",   // Editor only
   "style": "file:./style-index.css"     // Both
   ```

2. **Wrong file path**
   - Check file exists in build directory
   - Verify path is relative to block.json

3. **CSS specificity issues**
   - Use block wrapper class for specificity
   - `.wp-block-namespace-blockname .my-element {}`

## Debug Tools

```javascript
// Log block attributes
console.log('Block attributes:', attributes);

// Log block props
const blockProps = useBlockProps();
console.log('Block props:', blockProps);

// Check registered blocks
wp.blocks.getBlockTypes().map(b => b.name);

// Get specific block type
wp.blocks.getBlockType('namespace/block-name');
```

## Console Warnings

### "apiVersion should be 3"
- Update block.json: `"apiVersion": 3`

### "Block has a save function but no render callback"
- Normal for static blocks, can ignore

### "Encountered two children with same key"
- Check InnerBlocks template for duplicate keys
