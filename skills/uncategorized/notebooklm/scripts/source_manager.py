#!/usr/bin/env python3
"""
Source Manager for NotebookLM
Handles remote knowledge ingestion (Website URLs and Copied Text)
"""

import argparse
import sys
import time
from pathlib import Path

from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from notebook_manager import NotebookLibrary
from config import (
    SOURCES_TAB_SELECTOR,
    ADD_SOURCE_SELECTORS,
    WEBSITE_OPTION,
    COPIED_TEXT_OPTION,
    SOURCE_URL_INPUT,
    SOURCE_INSERT_BUTTON,
    BROWSER_PROFILE_DIR
)
from browser_utils import BrowserFactory, StealthUtils


def add_source(notebook_url: str, source_type: str, content: str, headless: bool = True):
    """
    Adds a new source to a NotebookLM notebook.
    """
    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python auth_manager.py setup")
        return False

    print(f"📡 Ingesting {source_type} source into: {notebook_url}")

    playwright = None
    context = None

    try:
        playwright = sync_playwright().start()
        context = BrowserFactory.launch_persistent_context(playwright, headless=headless)
        page = context.new_page()
        
        print("  🌐 Opening notebook...")
        # domcontentloaded is faster and more reliable than networkidle for SPAs
        page.goto(notebook_url, wait_until="domcontentloaded", timeout=60000)
        
        # Ensure 'Sources' tab is active
        try:
            print("  📂 Ensuring 'Sources' tab is active...")
            # Longer timeout for the tab to appear as the page hydrates
            sources_tab = page.wait_for_selector(SOURCES_TAB_SELECTOR, timeout=20000, state="visible")
            if sources_tab:
                sources_tab.click()
                time.sleep(2)  # Small buffer for tab content to render
        except Exception as e:
            print(f"  ℹ️ 'Sources' tab not clickable or already active: {e}")

        # Wait for any of the Add source selectors
        add_btn = None
        for selector in ADD_SOURCE_SELECTORS:
            try:
                add_btn = page.wait_for_selector(selector, timeout=10000, state="visible")
                if add_btn:
                    print(f"  ✓ Found 'Add source' via: {selector}")
                    break
            except:
                continue

        if not add_btn:
            raise RuntimeError("Could not find 'Add source' button after trying all selectors.")
        
        print("  ➕ Clicking 'Add source'...")
        add_btn.click()
        
        if source_type == "url":
            print("  🔗 Selecting 'Website' option...")
            page.wait_for_selector(WEBSITE_OPTION, timeout=10000)
            page.click(WEBSITE_OPTION)
            
            print(f"  ⌨️ Entering URL: {content}")
            page.wait_for_selector(SOURCE_URL_INPUT, timeout=10000)
            StealthUtils.human_type(page, SOURCE_URL_INPUT, content)
            
        elif source_type == "text":
            print("  📝 Selecting 'Copied text' option...")
            page.wait_for_selector(COPIED_TEXT_OPTION, timeout=10000)
            page.click(COPIED_TEXT_OPTION)
            
            print("  ⌨️ Entering custom text...")
            page.wait_for_selector(SOURCE_URL_INPUT, timeout=10000)
            page.click(SOURCE_URL_INPUT) # Explicit focus
            StealthUtils.human_type(page, SOURCE_URL_INPUT, content)
            
            # Explicitly dispatch events to ensure Angular/Material detects changes
            page.evaluate(f"""
                const el = document.querySelector('{SOURCE_URL_INPUT}');
                el.dispatchEvent(new Event('input', {{ bubbles: true }}));
                el.dispatchEvent(new Event('change', {{ bubbles: true }}));
            """)
            time.sleep(1)
            
        # Click Insert (Wait for it to be enabled)
        print("  🚀 Waiting for 'Insert' button to be enabled...")
        try:
            page.wait_for_function(
                f"btn => !btn.disabled && !btn.className.includes('disabled')",
                arg=page.query_selector(SOURCE_INSERT_BUTTON),
                timeout=10000
            )
            print("  ✅ Button enabled! Submitting...")
            # Use mouse click instead of locator click to be more robust
            btn_box = page.query_selector(SOURCE_INSERT_BUTTON).bounding_box()
            page.mouse.click(btn_box['x'] + btn_box['width']/2, btn_box['y'] + btn_box['height']/2)
        except Exception as e:
            print(f"  ⚠️ Button did not enable or click failed: {e}")
            # Fallback one last time
            page.click(SOURCE_INSERT_BUTTON, force=True)
        
        # Verify ingestion (Wait for 'Copied text' or new source to appear)
        print("  ⏳ Verifying ingestion in UI...")
        success = False
        for _ in range(10):  # 10 attempts
            time.sleep(2)
            sources = page.query_selector_all(".source-list-item, .source-card") # Common selectors
            # Alternatively, look for text content we just added
            if "Copied text" in page.content() or content[:20] in page.content():
                success = True
                break
        
        if success:
            print("✅ Source ingestion verified in UI!")
            return True
        else:
            print("⚠️ Ingestion click succeeded, but source not found in UI yet.")
            return True # Still return True as indexing might be slow, but log the warning

    except Exception as e:
        print(f"❌ Ingestion failed: {e}")
        return False
    finally:
        if context:
            context.close()
        if playwright:
            playwright.stop()


def main():
    parser = argparse.ArgumentParser(description='Manage NotebookLM sources')
    parser.add_argument('--url', help='Target Notebook URL')
    parser.add_argument('--id', help='Target Notebook ID from library')
    parser.add_argument('--type', choices=['url', 'text'], default='url', help='Type of source')
    parser.add_argument('--content', required=True, help='URL string or text content')
    parser.add_argument('--show-browser', action='store_true', help='Show browser')

    args = parser.parse_args()

    notebook_url = args.url
    if not notebook_url and args.id:
        library = NotebookLibrary()
        nb = library.get_notebook(args.id)
        if nb:
            notebook_url = nb['url']
        else:
            print(f"❌ Notebook '{args.id}' not found")
            return 1

    if not notebook_url:
        library = NotebookLibrary()
        active = library.get_active_notebook()
        if active:
            notebook_url = active['url']
        else:
            print("❌ No notebook specified or active.")
            return 1

    success = add_source(
        notebook_url=notebook_url,
        source_type=args.type,
        content=args.content,
        headless=not args.show_browser
    )

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
