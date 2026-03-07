# block.json Reference

## Complete block.json Example

```json
{
    "$schema": "https://schemas.wp.org/trunk/block.json",
    "apiVersion": 3,
    "name": "myplugin/feature-card",
    "version": "1.0.0",
    "title": "Feature Card",
    "category": "widgets",
    "icon": "star-filled",
    "description": "A card highlighting a feature with icon, title, and description.",
    "keywords": [ "feature", "card", "highlight", "service" ],
    "textdomain": "myplugin",
    "supports": {
        "html": false,
        "align": [ "wide", "full" ],
        "anchor": true,
        "color": {
            "background": true,
            "text": true,
            "gradients": true,
            "link": true
        },
        "spacing": {
            "margin": true,
            "padding": true,
            "blockGap": true
        },
        "typography": {
            "fontSize": true,
            "lineHeight": true
        },
        "__experimentalBorder": {
            "radius": true,
            "width": true,
            "color": true,
            "style": true
        }
    },
    "attributes": {
        "title": {
            "type": "string",
            "default": ""
        },
        "description": {
            "type": "string",
            "source": "html",
            "selector": ".feature-card__description"
        },
        "mediaId": {
            "type": "number"
        },
        "mediaUrl": {
            "type": "string"
        }
    },
    "example": {
        "attributes": {
            "title": "Feature Title",
            "description": "This is a description of the feature."
        }
    },
    "editorScript": "file:./index.js",
    "editorStyle": "file:./index.css",
    "style": "file:./style-index.css",
    "viewScript": "file:./view.js",
    "render": "file:./render.php"
}
```

## Key Fields

### apiVersion (Required for WP 6.9+)

```json
"apiVersion": 3
```

WordPress 6.9 enforces apiVersion 3. Lower versions trigger console warnings.

**Migration from v2 to v3:**
- Usually just change the number
- Test in iframe editor environment
- Ensure styles are included in block.json

### name (Never change after release)

```json
"name": "namespace/block-name"
```

Treat as stable API - changing breaks existing content.

### supports

Common support flags:

```json
"supports": {
    "html": false,           // Disable HTML editing mode
    "align": ["wide", "full"], // Alignment options
    "anchor": true,          // Add HTML anchor
    "className": true,       // Custom CSS class
    "color": {
        "background": true,
        "text": true,
        "link": true,
        "gradients": true
    },
    "spacing": {
        "margin": true,
        "padding": true,
        "blockGap": true
    },
    "typography": {
        "fontSize": true,
        "lineHeight": true
    }
}
```

### attributes

Attribute sources:
- No source: stored in block comment delimiter
- `source: "html"`: extracted from saved HTML
- `source: "attribute"`: extracted from HTML attribute
- `source: "text"`: extracted as text content

```json
"attributes": {
    "content": {
        "type": "string",
        "source": "html",
        "selector": "p"
    },
    "url": {
        "type": "string",
        "source": "attribute",
        "selector": "a",
        "attribute": "href"
    }
}
```

### Asset Registration

```json
"editorScript": "file:./index.js",    // Editor only
"editorStyle": "file:./index.css",    // Editor only
"script": "file:./script.js",         // Both editor and frontend
"style": "file:./style-index.css",    // Both editor and frontend
"viewScript": "file:./view.js",       // Frontend only (classic)
"viewScriptModule": "file:./view.js", // Frontend only (ESM module)
"render": "file:./render.php"         // Dynamic render callback
```
