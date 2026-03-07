#!/usr/bin/env python3
"""
WordPress Plugin Structure Discovery Script

Run this FIRST to discover a plugin's admin tabs, settings, and structure.
It outputs a capture script configuration tailored to your specific plugin.

Usage:
    python3 discover-plugin.py --url http://your-site.local --page your-plugin-slug

Prerequisites:
    1. Install mu-plugin for auto-login (see mu-auto-login.php)
    2. pip install playwright && playwright install chromium
"""

from playwright.sync_api import sync_playwright
import argparse
import json
import os
import time

def discover_admin_tabs(page):
    """Discover all admin tabs in the plugin settings page."""
    tabs = []

    # Common tab wrapper selectors (ordered by specificity)
    tab_selectors = [
        ".nav-tab-wrapper ul li a.nav-tab",        # Wbcom style (ul > li > a)
        ".nav-tab-wrapper li a.nav-tab",           # Wbcom style (li > a)
        ".nav-tab-wrapper a.nav-tab",              # Standard WP style
        ".wp-tab-bar li a",                        # WP tab bar
        ".settings-tabs li a",                     # Generic settings tabs
        "[role='tablist'] [role='tab']",           # ARIA tabs
        ".nav-tab",                                # Fallback - any nav-tab
    ]

    for selector in tab_selectors:
        try:
            elements = page.locator(selector).all()
            print(f"    Trying: {selector} → {len(elements)} matches")

            if elements:
                for el in elements:
                    tab_id = None
                    tab_name = el.text_content().strip()

                    # Try to get tab ID from parent li
                    try:
                        parent = el.locator("xpath=..")
                        parent_id = parent.get_attribute("id")
                        if parent_id:
                            tab_id = parent_id
                    except:
                        pass

                    # Try href parameter
                    if not tab_id:
                        href = el.get_attribute("href") or ""
                        if "tab=" in href:
                            tab_id = href.split("tab=")[-1].split("&")[0]
                        elif "#" in href:
                            tab_id = href.split("#")[-1]

                    # Try element's own ID
                    if not tab_id:
                        tab_id = el.get_attribute("id")

                    if tab_name and tab_id:
                        # Avoid duplicates
                        if not any(t["id"] == tab_id for t in tabs):
                            tabs.append({
                                "id": tab_id,
                                "name": tab_name,
                                "selector": selector,
                            })

                if tabs:
                    print(f"    ✓ Found {len(tabs)} tabs using: {selector}")
                    break
        except Exception as e:
            print(f"    Error with {selector}: {e}")
            continue

    return tabs


def discover_form_elements(page):
    """Discover form elements on the current page."""
    elements = {
        "dropdowns": [],
        "checkboxes": [],
        "text_inputs": [],
        "textareas": [],
        "buttons": [],
    }

    # Dropdowns
    try:
        selects = page.locator("select").all()
        for sel in selects:
            sel_id = sel.get_attribute("id") or ""
            sel_name = sel.get_attribute("name") or ""
            options = []
            try:
                opts = sel.locator("option").all()
                for opt in opts:
                    val = opt.get_attribute("value")
                    text = opt.text_content().strip()
                    if val:
                        options.append({"value": val, "text": text})
            except:
                pass

            if sel_id or sel_name:
                elements["dropdowns"].append({
                    "id": sel_id,
                    "name": sel_name,
                    "options": options[:10],  # Limit to 10
                })
    except:
        pass

    # Checkboxes
    try:
        checks = page.locator("input[type='checkbox']").all()
        for chk in checks[:20]:  # Limit
            chk_id = chk.get_attribute("id") or ""
            chk_name = chk.get_attribute("name") or ""
            if chk_id or chk_name:
                elements["checkboxes"].append({
                    "id": chk_id,
                    "name": chk_name,
                })
    except:
        pass

    # Submit buttons
    try:
        btns = page.locator("input[type='submit'], button[type='submit']").all()
        for btn in btns[:5]:
            btn_val = btn.get_attribute("value") or btn.text_content() or ""
            btn_id = btn.get_attribute("id") or ""
            elements["buttons"].append({
                "id": btn_id,
                "text": btn_val.strip(),
            })
    except:
        pass

    return elements


def discover_plugin_structure(url, admin_page, user_id=1):
    """Discover the complete plugin admin structure."""

    print(f"\n{'='*60}")
    print("PLUGIN STRUCTURE DISCOVERY")
    print(f"{'='*60}")
    print(f"\nSite: {url}")
    print(f"Admin Page: {admin_page}")

    structure = {
        "site_url": url,
        "admin_page": admin_page,
        "tabs": [],
        "tab_details": {},
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1680, "height": 1100})
        page = context.new_page()

        # Login
        print(f"\n--- Logging in as user {user_id} ---")
        page.goto(f"{url}/wp-admin/?dev_login={user_id}")
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        if "Dashboard" not in page.title() and "Log In" in page.title():
            print("ERROR: Login failed. Check mu-plugin installation.")
            browser.close()
            return None

        print("Logged in successfully!")

        # Navigate to plugin page
        print(f"\n--- Loading plugin page ---")
        page.goto(f"{url}/wp-admin/admin.php?page={admin_page}")
        page.wait_for_load_state('networkidle')
        time.sleep(2)

        # Check if page loaded
        if "page=" not in page.url:
            print(f"ERROR: Plugin page not found. Check slug: {admin_page}")
            browser.close()
            return None

        # Discover tabs
        print(f"\n--- Discovering tabs ---")
        tabs = discover_admin_tabs(page)
        structure["tabs"] = tabs

        if tabs:
            print(f"Found {len(tabs)} tabs:")
            for tab in tabs:
                print(f"  - {tab['id']}: {tab['name']}")
        else:
            print("No tabs found (single-page settings)")

        # Discover elements on each tab
        print(f"\n--- Analyzing each tab ---")

        if tabs:
            for tab in tabs:
                print(f"\n  Tab: {tab['name']} ({tab['id']})")

                # Click tab
                try:
                    tab_selector = f".nav-tab-wrapper li#{tab['id']} a.nav-tab"
                    page.locator(tab_selector).click()
                    time.sleep(1)
                except:
                    try:
                        page.goto(f"{url}/wp-admin/admin.php?page={admin_page}&tab={tab['id']}")
                        page.wait_for_load_state('networkidle')
                        time.sleep(1)
                    except:
                        print(f"    Could not load tab: {tab['id']}")
                        continue

                # Discover form elements
                elements = discover_form_elements(page)
                structure["tab_details"][tab["id"]] = elements

                # Summary
                print(f"    Dropdowns: {len(elements['dropdowns'])}")
                print(f"    Checkboxes: {len(elements['checkboxes'])}")

                # Check for editor dropdown
                for dd in elements["dropdowns"]:
                    if "editor" in dd["id"].lower() or "editor" in dd["name"].lower():
                        print(f"    >> EDITOR FOUND: #{dd['id']} ({len(dd['options'])} options)")
                        for opt in dd["options"]:
                            print(f"       - {opt['value']}: {opt['text']}")
        else:
            # Single page - discover all elements
            elements = discover_form_elements(page)
            structure["tab_details"]["main"] = elements
            print(f"  Dropdowns: {len(elements['dropdowns'])}")
            print(f"  Checkboxes: {len(elements['checkboxes'])}")

        browser.close()

    return structure


def generate_capture_config(structure):
    """Generate capture script configuration from discovered structure."""

    config = {
        "SITE_CONFIG": {
            "url": structure["site_url"],
            "plugin_slug": structure["admin_page"],
        },
        "ADMIN_TABS": [],
        "EDITOR_CONFIG": None,
    }

    # Generate tab captures
    for tab in structure["tabs"]:
        tab_config = {
            "id": tab["id"],
            "name": tab["name"],
            "file": f"admin-{tab['id'].replace('_', '-')}-tab.png",
        }
        config["ADMIN_TABS"].append(tab_config)

    # Find editor config
    for tab_id, elements in structure["tab_details"].items():
        for dd in elements.get("dropdowns", []):
            if "editor" in dd["id"].lower() or "editor" in dd["name"].lower():
                config["EDITOR_CONFIG"] = {
                    "tab": tab_id,
                    "selector": f"#{dd['id']}" if dd["id"] else f"[name='{dd['name']}']",
                    "options": [opt["value"] for opt in dd["options"] if opt["value"]],
                }
                break

    return config


def print_capture_script(config, plugin_path):
    """Print a ready-to-use capture script."""

    tabs_code = "ADMIN_TABS = [\n"
    for tab in config["ADMIN_TABS"]:
        tabs_code += f'    {{"id": "{tab["id"]}", "name": "{tab["name"]}", "file": "{tab["file"]}"}},\n'
    tabs_code += "]"

    editor_code = "EDITOR_CONFIG = None  # No editor dropdown found"
    editor_types = ""

    if config["EDITOR_CONFIG"]:
        ec = config["EDITOR_CONFIG"]
        editor_code = f'''EDITOR_CONFIG = {{
    "tab": "{ec['tab']}",
    "selector": "{ec['selector']}",
    "form_url": "/add-new-post/",  # Update if different
}}'''

        if ec["options"]:
            editor_types = "\nEDITOR_TYPES = [\n"
            for opt in ec["options"]:
                editor_types += f'    {{"type": "{opt}", "filename": "frontend-form-{opt}.png"}},\n'
            editor_types += "]"

    script = f'''#!/usr/bin/env python3
"""
Screenshot Capture Script for {config["SITE_CONFIG"]["plugin_slug"]}
Auto-generated by discover-plugin.py

Usage: python3 capture-screenshots.py
"""

from playwright.sync_api import sync_playwright
import time
import os
import json

# =============================================================================
# CONFIGURATION
# =============================================================================

SITE_CONFIG = {{
    "url": "{config["SITE_CONFIG"]["url"]}",
    "plugin_slug": "{config["SITE_CONFIG"]["plugin_slug"]}",
    "plugin_path": "{plugin_path}",
}}

ADMIN_USER_ID = 1
IMAGES_DIR = f"{{SITE_CONFIG['plugin_path']}}/docs/images"
METADATA_DIR = f"/tmp/screenshot-metadata-{{SITE_CONFIG['plugin_slug']}}"
SESSION_DIR = "/tmp/playwright-wp-session"
VIEWPORT = {{"width": 1680, "height": 1100}}

# =============================================================================
# ADMIN TABS
# =============================================================================

{tabs_code}

# =============================================================================
# EDITOR CONFIGURATION
# =============================================================================

{editor_code}
{editor_types}

# =============================================================================
# FRONTEND PAGES (add your pages here)
# =============================================================================

FRONTEND_PAGES = [
    # {{"url": "/dashboard/", "file": "frontend-dashboard.png", "full_page": True}},
]

# =============================================================================
# CAPTURE FUNCTIONS
# =============================================================================

def ensure_dirs():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    os.makedirs(METADATA_DIR, exist_ok=True)
    if os.path.exists(SESSION_DIR):
        import shutil
        shutil.rmtree(SESSION_DIR)
    os.makedirs(SESSION_DIR, exist_ok=True)


def click_tab(page, tab_id, wait=2):
    """Click a plugin admin tab."""
    selector = f".nav-tab-wrapper li#{{tab_id}} a.nav-tab"
    try:
        tab = page.locator(selector)
        if tab.is_visible():
            tab.click()
            time.sleep(wait)
            return True
    except:
        pass
    return False


def capture(page, filename, full_page=False):
    """Capture screenshot."""
    filepath = os.path.join(IMAGES_DIR, filename)
    page.screenshot(path=filepath, full_page=full_page)
    print(f"  Saved: {{filepath}}")
    return filepath


def main():
    ensure_dirs()
    url = SITE_CONFIG["url"]
    slug = SITE_CONFIG["plugin_slug"]

    print(f"\\n=== Capturing {{slug}} Screenshots ===\\n")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            SESSION_DIR, headless=False, viewport=VIEWPORT
        )
        page = context.pages[0] if context.pages else context.new_page()

        # Login
        print("Logging in...")
        page.goto(f"{{url}}/wp-admin/?dev_login={{ADMIN_USER_ID}}")
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        # Admin tabs
        print("\\n--- Admin Screenshots ---\\n")
        page.goto(f"{{url}}/wp-admin/admin.php?page={{slug}}")
        page.wait_for_load_state('networkidle')
        time.sleep(2)

        for tab in ADMIN_TABS:
            print(f"  Tab: {{tab['name']}}")
            if click_tab(page, tab["id"]):
                capture(page, tab["file"])
            else:
                print(f"    SKIP: Tab {{tab['id']}} not found")

        # Editor variations
        if EDITOR_CONFIG and 'EDITOR_TYPES' in dir():
            print("\\n--- Editor Screenshots ---\\n")
            for editor in EDITOR_TYPES:
                print(f"  Editor: {{editor['type']}}")
                page.goto(f"{{url}}/wp-admin/admin.php?page={{slug}}")
                page.wait_for_load_state('networkidle')
                click_tab(page, EDITOR_CONFIG["tab"])
                try:
                    page.select_option(EDITOR_CONFIG["selector"], editor["type"])
                    page.locator("input[type='submit']").click()
                    page.wait_for_load_state('networkidle')
                    page.goto(f"{{url}}{{EDITOR_CONFIG['form_url']}}")
                    page.wait_for_load_state('networkidle')
                    time.sleep(2)
                    capture(page, editor["filename"], full_page=True)
                except Exception as e:
                    print(f"    Error: {{e}}")

        # Frontend pages
        if FRONTEND_PAGES:
            print("\\n--- Frontend Screenshots ---\\n")
            for pg in FRONTEND_PAGES:
                print(f"  Page: {{pg['url']}}")
                page.goto(f"{{url}}{{pg['url']}}")
                page.wait_for_load_state('networkidle')
                time.sleep(2)
                capture(page, pg["file"], pg.get("full_page", False))

        context.close()

    print(f"\\n=== Done! Screenshots in {{IMAGES_DIR}} ===\\n")


if __name__ == "__main__":
    main()
'''

    return script


def main():
    parser = argparse.ArgumentParser(description="Discover WordPress plugin structure")
    parser.add_argument("--url", required=True, help="WordPress site URL (e.g., http://site.local)")
    parser.add_argument("--page", required=True, help="Plugin admin page slug")
    parser.add_argument("--user", type=int, default=1, help="User ID for login (default: 1)")
    parser.add_argument("--plugin-path", help="Path to plugin directory")
    parser.add_argument("--output", help="Output capture script path")

    args = parser.parse_args()

    # Discover structure
    structure = discover_plugin_structure(args.url, args.page, args.user)

    if not structure:
        print("\nDiscovery failed!")
        return 1

    # Generate config
    config = generate_capture_config(structure)

    # Print summary
    print(f"\n{'='*60}")
    print("DISCOVERY COMPLETE")
    print(f"{'='*60}")
    print(f"\nTabs found: {len(config['ADMIN_TABS'])}")
    print(f"Editor config: {'Yes' if config['EDITOR_CONFIG'] else 'No'}")

    # Generate script
    plugin_path = args.plugin_path or f"/path/to/your/{args.page}"
    script = print_capture_script(config, plugin_path)

    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(script)
        print(f"\nCapture script saved to: {args.output}")
    else:
        print(f"\n{'='*60}")
        print("GENERATED CAPTURE SCRIPT")
        print(f"{'='*60}")
        print(script)

    # Save structure as JSON for reference
    json_path = f"/tmp/{args.page}-structure.json"
    with open(json_path, 'w') as f:
        json.dump(structure, f, indent=2)
    print(f"\nStructure JSON saved to: {json_path}")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
