---
name: "extract-pptx-text"
description: "Extracts text from a PowerPoint (.pptx) file and prints it to the console. Useful when you need to get the text content of a presentation."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["powerpoint","pptx","text extraction","presentation","document processing"]
triggers:
  - "when I need to extract text from a PowerPoint file"
  - "when I want to get the text content of a pptx file"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "extract_pptx.py"
---

# Extract Pptx Text

## When to Use

- when I need to extract text from a PowerPoint file
- when I want to get the text content of a pptx file

## What This Does

Extracts text from a PowerPoint (.pptx) file and prints it to the console. Useful when you need to get the text content of a presentation.

## Execution

```bash
python extract_pptx.py <path>
```

### Parameters

<path>: The path to the PowerPoint (.pptx) file.

### Dependencies

- python
- python-zipfile
- python-xml.etree.ElementTree
