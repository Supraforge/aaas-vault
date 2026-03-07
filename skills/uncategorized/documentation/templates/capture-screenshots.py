#!/usr/bin/env python3
"""
WordPress Documentation Screenshot Capture Script with Annotation Support

This is a template - copy to your project's docs/tools/ directory and customize.

Prerequisites:
    1. Install the mu-plugin for auto-login:
       cp ~/.claude/skills/documentation/templates/mu-auto-login.php \
          /path/to/wp-content/mu-plugins/dev-auto-login.php

    2. Install Python dependencies:
       pip install playwright pyyaml pillow
       playwright install chromium

Usage:
    python3 capture-screenshots.py

Output:
    docs/images/           - Plain screenshots
    docs/images/annotated/ - Annotated screenshots (if annotations defined)
    /tmp/screenshot-metadata-{plugin}/ - Temp JSON metadata (auto-cleaned)

Configuration:
    1. Update SITE_CONFIG with your site details
    2. Update ROLES with user IDs (no passwords needed!)
    3. Define CAPTURES with annotations for your specific plugin/theme

Image Annotator MCP Integration:
    After capture, use the generated MCP commands JSON to annotate screenshots.
    The metadata includes MCP-ready format for direct tool calls.
"""

from playwright.sync_api import sync_playwright
import time
import os
import shutil
import json
import uuid

# =============================================================================
# CONFIGURATION - Customize for your project
# =============================================================================

SITE_CONFIG = {
    "url": "http://your-site.local",  # Change to your site URL
    "plugin_page": "your-plugin-slug",  # Admin page slug
}

# User roles - use user IDs or usernames (NO passwords needed with mu-plugin!)
ROLES = {
    "admin": {
        "user_id": 1,
        "username": "admin",
    },
    "subscriber": {
        "user_id": 2,
        "username": "test_member",
    },
    "author": {
        "user_id": 3,
        "username": "test_author",
    },
}

# Output directories
OUTPUT_DIR = "docs/images"
ANNOTATED_DIR = "docs/images/annotated"
# Unique metadata dir per plugin to avoid parallel run collisions
METADATA_DIR = f"/tmp/screenshot-metadata-{SITE_CONFIG.get('plugin_page', 'default')}"

# Browser settings
VIEWPORT = {"width": 1680, "height": 1100}
HEADLESS = False  # Set True for CI/CD, False for debugging
WAIT_TIME = 2  # Seconds to wait after page load
MAX_RETRIES = 3  # Retry failed captures

# Session storage (unique per plugin)
SESSION_DIR = f"/tmp/playwright-wp-session-{SITE_CONFIG.get('plugin_page', 'default')}"

# =============================================================================
# TYPE MAPPING: Capture Script Types → Image Annotator MCP Types
# =============================================================================
# The capture script uses semantic type names, MCP uses specific tool types
TYPE_MAPPING = {
    "box": "rect",           # box → rect (rectangle highlight)
    "number": "marker",      # number → marker (numbered circle)
    "arrow": "arrow",        # arrow → arrow (direct mapping)
    "circle": "circle",      # circle → circle (direct mapping)
    "highlight": "highlight", # highlight → highlight (semi-transparent overlay)
    "callout": "callout",    # callout → callout (speech bubble)
    "label": "label",        # label → label (text with background)
    "blur": "blur",          # blur → blur (hide sensitive info)
}

# Default colors for annotation types
DEFAULT_COLORS = {
    "marker": "primary",
    "rect": "red",
    "arrow": "primary",
    "circle": "red",
    "highlight": "yellow",
    "callout": "primary",
    "label": "darkGray",
}

# =============================================================================
# CAPTURE DEFINITIONS WITH ANNOTATIONS
# =============================================================================

# Admin tab screenshots with annotations
# Each annotation includes:
#   - selector: CSS selector for the element
#   - label: Text description for the annotation
#   - type: arrow, circle, box, number, highlight
#   - position: where to place label (top, bottom, left, right, auto)
ADMIN_TABS = [
    # Example with annotations:
    # {
    #     "tab": None,
    #     "filename": "admin-overview-tab.png",
    #     "annotations": [
    #         {"selector": ".nav-tab-wrapper", "label": "Settings Tabs", "type": "box", "position": "top"},
    #         {"selector": "#general", "label": "1. General Settings", "type": "number", "number": 1},
    #         {"selector": "input[type='submit']", "label": "Save Changes", "type": "arrow", "position": "left"},
    #     ]
    # },
]

# Frontend page screenshots with annotations
FRONTEND_PAGES = [
    # Example:
    # {
    #     "url": "/members/{username}/blog/",
    #     "filename": "member-blog-tab.png",
    #     "full_page": False,
    #     "annotations": [
    #         {"selector": "#subnav a[href*='/blog/']", "label": "Blog Tab", "type": "circle"},
    #         {"selector": ".post-list", "label": "Your Published Posts", "type": "box", "position": "right"},
    #     ]
    # },
]

# Editor type variations (if plugin has multiple editors)
# Set editor_tab and editor_selector for your plugin
EDITOR_CONFIG = {
    "tab": "editor",                           # Tab ID with editor settings
    "selector": "select[name*='editor']",      # CSS selector for editor dropdown
    "form_url": "/add-new-post/",              # Frontend form URL to capture
}

EDITOR_TYPES = [
    # {"type": "editorjs", "filename": "form-editorjs.png", "annotations": [...]},
    # {"type": "medium", "filename": "form-medium.png", "annotations": [...]},
    # {"type": "classic", "filename": "form-classic.png", "annotations": [...]},
]

# Role-based captures
ROLE_CAPTURES = [
    # {"url": "/dashboard/", "roles": ["admin", "subscriber"], "filename_pattern": "dashboard-{role}.png"},
]

# =============================================================================
# ANNOTATION FUNCTIONS
# =============================================================================

def get_element_bounds(page, selector):
    """Get bounding box for an element."""
    try:
        element = page.locator(selector).first
        if element.is_visible():
            box = element.bounding_box()
            if box:
                return {
                    "x": int(box["x"]),
                    "y": int(box["y"]),
                    "width": int(box["width"]),
                    "height": int(box["height"]),
                    "center_x": int(box["x"] + box["width"] / 2),
                    "center_y": int(box["y"] + box["height"] / 2),
                }
    except Exception as e:
        print(f"    Warning: Could not get bounds for '{selector}': {e}")
    return None


def convert_to_mcp_format(ann_type, bounds, label="", position="auto", number=1):
    """
    Convert captured bounds to Image Annotator MCP annotation format.

    Each MCP annotation type expects different coordinate formats:
    - marker: {x, y, number, color, size}
    - rect: {x, y, width, height, color, strokeWidth}
    - arrow: {from: [x,y], to: [x,y], color, strokeWidth}
    - circle: {x, y, radius, color, strokeWidth}
    - highlight: {x, y, width, height, color, opacity}
    - label: {x, y, text, color, fontSize, background}
    - callout: {x, y, text, pointer, color, background}
    """
    mcp_type = TYPE_MAPPING.get(ann_type, ann_type)
    color = DEFAULT_COLORS.get(mcp_type, "red")

    # Base annotation with type
    mcp_ann = {"type": mcp_type}

    if mcp_type == "marker":
        # Numbered circle at center of element
        mcp_ann.update({
            "x": bounds["center_x"],
            "y": bounds["center_y"],
            "number": number,
            "color": color,
            "size": 24,
        })

    elif mcp_type == "rect":
        # Rectangle around element with padding
        padding = 4
        mcp_ann.update({
            "x": bounds["x"] - padding,
            "y": bounds["y"] - padding,
            "width": bounds["width"] + (padding * 2),
            "height": bounds["height"] + (padding * 2),
            "color": color,
            "strokeWidth": 3,
        })
        # Add label if provided
        if label:
            mcp_ann["_label"] = {
                "type": "label",
                "text": label,
                "color": "darkGray",
                "fontSize": 14,
                "background": "white",
                "shadow": True,
            }
            # Position label based on preference
            if position == "top":
                mcp_ann["_label"]["x"] = bounds["center_x"]
                mcp_ann["_label"]["y"] = bounds["y"] - 25
            elif position == "bottom":
                mcp_ann["_label"]["x"] = bounds["center_x"]
                mcp_ann["_label"]["y"] = bounds["y"] + bounds["height"] + 20
            elif position == "left":
                mcp_ann["_label"]["x"] = bounds["x"] - 10
                mcp_ann["_label"]["y"] = bounds["center_y"]
            else:  # right or auto
                mcp_ann["_label"]["x"] = bounds["x"] + bounds["width"] + 15
                mcp_ann["_label"]["y"] = bounds["center_y"]

    elif mcp_type == "arrow":
        # Arrow pointing to element from label position
        label_offset = 100
        if position == "left":
            from_pt = [bounds["x"] - label_offset, bounds["center_y"]]
            to_pt = [bounds["x"] - 5, bounds["center_y"]]
        elif position == "right":
            from_pt = [bounds["x"] + bounds["width"] + label_offset, bounds["center_y"]]
            to_pt = [bounds["x"] + bounds["width"] + 5, bounds["center_y"]]
        elif position == "top":
            from_pt = [bounds["center_x"], bounds["y"] - label_offset]
            to_pt = [bounds["center_x"], bounds["y"] - 5]
        elif position == "bottom":
            from_pt = [bounds["center_x"], bounds["y"] + bounds["height"] + label_offset]
            to_pt = [bounds["center_x"], bounds["y"] + bounds["height"] + 5]
        else:  # auto - default to right
            from_pt = [bounds["x"] + bounds["width"] + label_offset, bounds["center_y"]]
            to_pt = [bounds["x"] + bounds["width"] + 5, bounds["center_y"]]

        mcp_ann.update({
            "from": from_pt,
            "to": to_pt,
            "color": color,
            "strokeWidth": 2,
        })
        # Add label at arrow start
        if label:
            mcp_ann["_label"] = {
                "type": "label",
                "x": from_pt[0] + (10 if position in ["left", "auto"] else -10),
                "y": from_pt[1],
                "text": label,
                "color": "darkGray",
                "fontSize": 14,
                "background": "white",
                "shadow": True,
            }

    elif mcp_type == "circle":
        # Circle around element
        radius = max(bounds["width"], bounds["height"]) // 2 + 8
        mcp_ann.update({
            "x": bounds["center_x"],
            "y": bounds["center_y"],
            "radius": radius,
            "color": color,
            "strokeWidth": 3,
        })
        if label:
            mcp_ann["_label"] = {
                "type": "label",
                "x": bounds["center_x"] + radius + 15,
                "y": bounds["center_y"],
                "text": label,
                "color": "darkGray",
                "fontSize": 14,
                "background": "white",
                "shadow": True,
            }

    elif mcp_type == "highlight":
        # Semi-transparent highlight
        mcp_ann.update({
            "x": bounds["x"],
            "y": bounds["y"],
            "width": bounds["width"],
            "height": bounds["height"],
            "color": "yellow",
            "opacity": 0.35,
        })

    elif mcp_type == "callout":
        # Speech bubble with pointer
        pointer_dir = {"top": "bottom", "bottom": "top", "left": "right", "right": "left"}.get(position, "left")
        mcp_ann.update({
            "x": bounds["center_x"],
            "y": bounds["center_y"],
            "text": label,
            "pointer": pointer_dir,
            "color": color,
            "background": "white",
            "shadow": True,
        })

    elif mcp_type == "label":
        # Text label with background
        mcp_ann.update({
            "x": bounds["center_x"],
            "y": bounds["y"] - 20,
            "text": label,
            "color": "darkGray",
            "fontSize": 14,
            "background": "white",
            "shadow": True,
        })

    elif mcp_type == "blur":
        # Blur area
        mcp_ann.update({
            "x": bounds["x"],
            "y": bounds["y"],
            "width": bounds["width"],
            "height": bounds["height"],
            "intensity": 8,
        })

    return mcp_ann


def extract_annotations(page, annotations):
    """Extract element positions and generate MCP-ready annotations."""
    extracted = []
    mcp_annotations = []

    for i, ann in enumerate(annotations):
        selector = ann.get("selector", "")
        bounds = get_element_bounds(page, selector)

        ann_type = ann.get("type", "box")
        label = ann.get("label", "")
        position = ann.get("position", "auto")
        number = ann.get("number", i + 1)

        if bounds:
            # Original format for reference
            extracted.append({
                "index": i + 1,
                "selector": selector,
                "label": label,
                "type": ann_type,
                "position": position,
                "number": number,
                "bounds": bounds,
                "found": True,
            })

            # Convert to MCP format
            mcp_ann = convert_to_mcp_format(ann_type, bounds, label, position, number)
            mcp_annotations.append(mcp_ann)

            # If there's a separate label, add it too
            if "_label" in mcp_ann:
                mcp_annotations.append(mcp_ann.pop("_label"))
        else:
            extracted.append({
                "index": i + 1,
                "selector": selector,
                "label": label,
                "type": ann_type,
                "position": position,
                "number": number,
                "bounds": None,
                "found": False,
            })
            print(f"    Warning: Element not found: {selector}")

    return extracted, mcp_annotations


def save_metadata(filename, metadata, mcp_annotations):
    """Save annotation metadata and MCP-ready commands as JSON."""
    os.makedirs(METADATA_DIR, exist_ok=True)

    # Save original metadata
    json_filename = os.path.splitext(filename)[0] + ".json"
    json_path = os.path.join(METADATA_DIR, json_filename)
    with open(json_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"    Metadata: {json_path}")

    # Save MCP-ready command (can be used directly with Image Annotator MCP)
    if mcp_annotations:
        mcp_filename = os.path.splitext(filename)[0] + "_mcp.json"
        mcp_path = os.path.join(METADATA_DIR, mcp_filename)

        mcp_command = {
            "tool": "annotate_screenshot",
            "input_path": metadata["filepath"],
            "output_path": os.path.join(ANNOTATED_DIR, filename),
            "theme": "documentation",
            "annotations": mcp_annotations,
        }

        with open(mcp_path, 'w') as f:
            json.dump(mcp_command, f, indent=2)
        print(f"    MCP Command: {mcp_path}")

    return json_path


def generate_mcp_batch_file(all_captures):
    """Generate a batch file with all MCP annotation commands."""
    batch_path = os.path.join(METADATA_DIR, "_batch_annotate.json")

    batch = {
        "description": "Batch annotation commands for Image Annotator MCP",
        "output_dir": ANNOTATED_DIR,
        "commands": all_captures,
    }

    with open(batch_path, 'w') as f:
        json.dump(batch, f, indent=2)

    print(f"\n  Batch file: {batch_path}")
    return batch_path


# =============================================================================
# CAPTURE FUNCTIONS
# =============================================================================

# Global tracking for batch processing
ALL_MCP_COMMANDS = []
CAPTURE_RESULTS = {"success": [], "failed": [], "skipped": []}


def setup_directories():
    """Create output directories and clear session."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(ANNOTATED_DIR, exist_ok=True)
    os.makedirs(METADATA_DIR, exist_ok=True)
    if os.path.exists(SESSION_DIR):
        shutil.rmtree(SESSION_DIR)
    os.makedirs(SESSION_DIR, exist_ok=True)

    # Reset tracking
    ALL_MCP_COMMANDS.clear()
    CAPTURE_RESULTS["success"].clear()
    CAPTURE_RESULTS["failed"].clear()
    CAPTURE_RESULTS["skipped"].clear()


def login_as(page, role="admin"):
    """Login to WordPress using mu-plugin auto-login."""
    role_config = ROLES.get(role, ROLES["admin"])
    user_id = role_config.get('user_id', 1)

    print(f"  Switching to {role} (user ID: {user_id})...")

    try:
        page.goto(f"{SITE_CONFIG['url']}/wp-admin/?dev_login={user_id}")
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        title = page.title()
        if "Dashboard" in title or "Profile" in title or "Log In" not in title:
            print(f"    Logged in successfully as {role}")
            return True
        else:
            print(f"    Login failed for {role}! Make sure mu-plugin is installed.")
            return False
    except Exception as e:
        print(f"    Login error for {role}: {e}")
        return False


def switch_user(page, role):
    """Switch to a different user role."""
    return login_as(page, role)


def click_plugin_tab(page, tab_id, wait_time=WAIT_TIME):
    """Click a plugin admin tab by its ID."""
    if tab_id is None:
        return True

    selector = f".nav-tab-wrapper li#{tab_id} a.nav-tab"
    try:
        tab = page.locator(selector)
        if tab.is_visible():
            tab.click()
            time.sleep(wait_time)
            # Verify tab is now active
            if "nav-tab-active" in (tab.get_attribute("class") or ""):
                return True
            # Fallback: check if click worked by re-checking visibility
            return True
        else:
            print(f"    Warning: Tab '{tab_id}' not visible")
            return False
    except Exception as e:
        print(f"    Warning: Could not click tab '{tab_id}': {e}")
    return False


def capture_screenshot_with_retry(page, filename, full_page=False, annotations=None, max_retries=MAX_RETRIES):
    """Capture screenshot with automatic retry on failure."""
    for attempt in range(max_retries):
        try:
            return capture_screenshot(page, filename, full_page, annotations)
        except Exception as e:
            print(f"    Attempt {attempt + 1}/{max_retries} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
                try:
                    page.reload()
                    page.wait_for_load_state('networkidle')
                except Exception:
                    pass
            else:
                print(f"    FAILED after {max_retries} attempts: {filename}")
                CAPTURE_RESULTS["failed"].append(filename)
                return None
    return None


def capture_screenshot(page, filename, full_page=False, annotations=None):
    """Capture screenshot and extract annotation metadata."""
    filepath = os.path.join(OUTPUT_DIR, filename)
    page.screenshot(path=filepath, full_page=full_page)
    print(f"    Saved: {filepath}")

    # Extract and save annotation metadata
    metadata = {
        "filename": filename,
        "filepath": os.path.abspath(filepath),
        "viewport": VIEWPORT,
        "full_page": full_page,
        "url": page.url,
        "title": page.title(),
        "annotations": [],
    }

    mcp_annotations = []

    if annotations:
        extracted, mcp_annotations = extract_annotations(page, annotations)
        metadata["annotations"] = extracted
        save_metadata(filename, metadata, mcp_annotations)

        # Track for batch processing
        if mcp_annotations:
            ALL_MCP_COMMANDS.append({
                "input_path": os.path.abspath(filepath),
                "output_path": os.path.join(os.path.abspath(ANNOTATED_DIR), filename),
                "annotations": mcp_annotations,
            })

    CAPTURE_RESULTS["success"].append(filename)
    return filepath


def navigate_and_capture(page, url, filename, full_page=False, wait_time=WAIT_TIME, annotations=None):
    """Navigate to URL and capture screenshot with annotations."""
    current_role = getattr(navigate_and_capture, 'current_role', 'admin')
    username = ROLES.get(current_role, {}).get('username', '')
    url = url.replace('{username}', username)

    print(f"  Capturing: {filename}")

    try:
        page.goto(f"{SITE_CONFIG['url']}{url}")
        page.wait_for_load_state('networkidle')
        time.sleep(wait_time)
        return capture_screenshot_with_retry(page, filename, full_page, annotations)
    except Exception as e:
        print(f"    Navigation failed: {e}")
        CAPTURE_RESULTS["failed"].append(filename)
        return None


def set_editor_type(page, editor_type, editor_tab="editor", editor_selector="select[name*='editor']"):
    """
    Change editor type in plugin settings.

    Args:
        page: Playwright page object
        editor_type: Value to select (e.g., "editorjs", "medium", "classic")
        editor_tab: Tab ID containing editor settings (default: "editor")
        editor_selector: CSS selector for editor dropdown (default: generic selector)
    """
    print(f"  Setting editor to: {editor_type}")
    page.goto(f"{SITE_CONFIG['url']}/wp-admin/admin.php?page={SITE_CONFIG['plugin_page']}")
    page.wait_for_load_state('networkidle')
    time.sleep(1)

    if editor_tab:
        click_plugin_tab(page, editor_tab)

    try:
        page.select_option(editor_selector, editor_type)
        time.sleep(0.5)
        page.locator("input[type='submit']").click()
        page.wait_for_load_state('networkidle')
        time.sleep(1)
        print(f"    Editor set to: {editor_type}")
        return True
    except Exception as e:
        print(f"    Warning: Could not set editor type: {e}")
        return False


# =============================================================================
# MAIN CAPTURE WORKFLOW
# =============================================================================

def capture_admin_tabs(page):
    """Capture admin tab screenshots with annotations."""
    if not ADMIN_TABS:
        return

    print("\n=== Admin Tab Screenshots ===\n")

    try:
        page.goto(f"{SITE_CONFIG['url']}/wp-admin/admin.php?page={SITE_CONFIG['plugin_page']}")
        page.wait_for_load_state('networkidle')
        time.sleep(WAIT_TIME)
    except Exception as e:
        print(f"  ERROR: Could not load admin page: {e}")
        return

    for capture in ADMIN_TABS:
        filename = capture['filename']
        tab_id = capture.get('tab')

        print(f"  Capturing: {filename}")

        # Verify tab click succeeded before capturing
        if tab_id is not None:
            if not click_plugin_tab(page, tab_id):
                print(f"    SKIPPED: Tab '{tab_id}' click failed for {filename}")
                CAPTURE_RESULTS["skipped"].append(filename)
                continue

        capture_screenshot_with_retry(
            page,
            filename,
            capture.get('full_page', False),
            capture.get('annotations', [])
        )


def capture_frontend_pages(page):
    """Capture frontend screenshots with annotations."""
    if not FRONTEND_PAGES:
        return

    print("\n=== Frontend Screenshots ===\n")
    for capture in FRONTEND_PAGES:
        navigate_and_capture(
            page,
            capture['url'],
            capture['filename'],
            capture.get('full_page', False),
            WAIT_TIME,
            capture.get('annotations', [])
        )


def capture_editor_variations(page):
    """Capture editor type screenshots with annotations."""
    if not EDITOR_TYPES:
        return

    print("\n=== Editor Type Screenshots ===\n")

    # Get editor config (use defaults if not defined)
    editor_tab = EDITOR_CONFIG.get("tab", "editor")
    editor_selector = EDITOR_CONFIG.get("selector", "select[name*='editor']")
    form_url = EDITOR_CONFIG.get("form_url", "/add-new-post/")

    for editor in EDITOR_TYPES:
        print(f"\n--- {editor['type']} editor ---")
        set_editor_type(page, editor['type'], editor_tab, editor_selector)
        navigate_and_capture(
            page,
            form_url,
            editor['filename'],
            full_page=True,
            annotations=editor.get('annotations', [])
        )


def capture_role_comparisons(page):
    """Capture role-based screenshots."""
    if not ROLE_CAPTURES:
        return

    print("\n=== Role Comparison Screenshots ===\n")
    for capture in ROLE_CAPTURES:
        for role in capture['roles']:
            print(f"\n--- As {role} ---")
            if switch_user(page, role):
                navigate_and_capture.current_role = role
                filename = capture['filename_pattern'].format(role=role)
                navigate_and_capture(
                    page,
                    capture['url'],
                    filename,
                    capture.get('full_page', False),
                    annotations=capture.get('annotations', [])
                )


def cleanup_metadata():
    """Remove temporary metadata files after annotation is complete."""
    if os.path.exists(METADATA_DIR):
        shutil.rmtree(METADATA_DIR)
        print(f"  Cleaned up: {METADATA_DIR}/")


def print_capture_summary():
    """Print summary of capture results."""
    print("\n" + "="*60)
    print("CAPTURE RESULTS")
    print("="*60)

    success = len(CAPTURE_RESULTS["success"])
    failed = len(CAPTURE_RESULTS["failed"])
    skipped = len(CAPTURE_RESULTS["skipped"])
    total = success + failed + skipped

    print(f"\n  Total:   {total}")
    print(f"  Success: {success}")
    if failed:
        print(f"  Failed:  {failed}")
        for f in CAPTURE_RESULTS["failed"]:
            print(f"           - {f}")
    if skipped:
        print(f"  Skipped: {skipped}")
        for f in CAPTURE_RESULTS["skipped"]:
            print(f"           - {f}")


def print_annotation_summary():
    """Print summary of captured annotations for Claude/MCP processing."""
    print("\n" + "="*60)
    print("ANNOTATION SUMMARY")
    print("="*60)

    if not ALL_MCP_COMMANDS:
        print("\nNo annotations to process.")
        return

    # Generate batch file for MCP processing
    generate_mcp_batch_file(ALL_MCP_COMMANDS)

    print(f"\nFound {len(ALL_MCP_COMMANDS)} screenshots with annotations.")
    print(f"\nMetadata (temp): {METADATA_DIR}/")
    print(f"Annotated output: {ANNOTATED_DIR}/")

    print("\n" + "-"*60)
    print("NEXT STEP: Annotate using Image Annotator MCP")
    print("-"*60)
    print(f"""
Option 1 - Batch annotation (recommended):
  Load {METADATA_DIR}/_batch_annotate.json and process all at once.

Option 2 - Individual annotation:
  For each *_mcp.json file in {METADATA_DIR}/, use:
  annotate_screenshot(input_path, output_path, annotations)

After annotation is complete:
  Run cleanup_metadata() or delete {METADATA_DIR}/
""")


def main():
    """Main capture workflow."""
    setup_directories()

    print("\n" + "="*60)
    print("WordPress Documentation Screenshot Capture")
    print("="*60)
    print(f"\nSite: {SITE_CONFIG['url']}")
    print(f"Plugin: {SITE_CONFIG['plugin_page']}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Annotated: {ANNOTATED_DIR}")
    print(f"Metadata: {METADATA_DIR}")
    print("\nUsing mu-plugin auto-login (no passwords needed)")
    print("="*60)

    try:
        with sync_playwright() as p:
            context = p.chromium.launch_persistent_context(
                SESSION_DIR,
                headless=HEADLESS,
                viewport=VIEWPORT
            )
            page = context.pages[0] if context.pages else context.new_page()

            print("\n=== Logging in ===\n")
            if not login_as(page, "admin"):
                print("\n  FATAL: Login failed. Aborting capture.")
                context.close()
                return 1

            navigate_and_capture.current_role = "admin"

            # Run capture sequences
            capture_admin_tabs(page)
            capture_frontend_pages(page)
            capture_editor_variations(page)
            capture_role_comparisons(page)

            context.close()

    except Exception as e:
        print(f"\n  FATAL ERROR: {e}")
        return 1

    # Print summaries
    print_capture_summary()
    print_annotation_summary()

    print("\n" + "="*60)
    print("Screenshot capture complete!")
    print("="*60)
    print(f"\nPlain screenshots: {OUTPUT_DIR}/")
    print(f"Annotated (after MCP processing): {ANNOTATED_DIR}/")
    print(f"\nMetadata location: {METADATA_DIR}/")
    print("  (Temporary - will be cleaned up after annotation)")

    # Return exit code based on results
    if CAPTURE_RESULTS["failed"]:
        return 1
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
