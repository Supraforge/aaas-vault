#!/usr/bin/env python3
"""
Domain Interrogator Agent
Conducts deep-dive interviews of the NotebookLM knowledge base based on domain-specific protocols.
Uses a Single Persistent Session with page reloads to maintain zero context drift.
"""

import argparse
import json
import sys
import time
import re
import shutil
import tempfile
from pathlib import Path
from datetime import datetime

from patchright.sync_api import sync_playwright

# Add base skill scripts to path
BASE_SKILL_DIR = Path(__file__).resolve().parent.parent.parent / "notebooklm" / "scripts"
sys.path.insert(0, str(BASE_SKILL_DIR))

try:
    from auth_manager import AuthManager
    from notebook_manager import NotebookLibrary
    from config import QUERY_INPUT_SELECTORS, RESPONSE_SELECTORS
    from browser_utils import BrowserFactory, StealthUtils
except ImportError as e:
    print(f"❌ Critical: Could not import base NotebookLM skill modules: {e}")
    raise e


class SessionInterrogator:
    """
    Manages a single persistent browser session for the interrogation batch.
    Uses temp user_data_dir for isolation + page reloads for context clearing.
    """
    
    def __init__(self, notebook_url: str, headless: bool = False):
        self.notebook_url = notebook_url
        self.headless = headless
        self.playwright = None
        self.context = None
        self.page = None
        self.temp_dir = None
        
    def start(self):
        """Start the browser session."""
        print("🚀 Initializing SessionInterrogator...")
        self.temp_dir = tempfile.mkdtemp()
        self.playwright = sync_playwright().start()
        
        # Launch persistent context (Headed by default for reliability)
        self.context = BrowserFactory.launch_persistent_context(
            self.playwright,
            headless=self.headless,
            user_data_dir=self.temp_dir
        )
        
        # Get/Create page
        self.page = self.context.pages[0] if self.context.pages else self.context.new_page()
        
        print(f"🌐 Navigating to Notebook: {self.notebook_url}")
        self.page.goto(self.notebook_url, wait_until="domcontentloaded")
        
        # Initial wait for load - check for input instead of URL which is flaky
        try:
            self.page.wait_for_selector(QUERY_INPUT_SELECTORS[0], timeout=60000, state="visible")
            print("✅ Session Ready (Input Found).")
        except:
            print(f"⚠️ Session Init Warning: Input not found immediately. Current URL: {self.page.url}")
            # Continue anyway, ask() will also wait

    def ask(self, question: str) -> str:
        """
        Ask a question within the existing session.
        Reloads the page FIRST to ensure clean context.
        """
        if not self.page:
            raise Exception("Session not started. Call start() first.")
            
        print(f"\n🔄 Refreshing page to clear context...")
        self.page.reload(wait_until="domcontentloaded")
        self.page.wait_for_selector(QUERY_INPUT_SELECTORS[0], timeout=60000, state="visible")
        
        # Ask logic (mirrors ask_question.py)
        print(f"💬 Asking: {question}")
        
        # Type
        input_selector = QUERY_INPUT_SELECTORS[0]
        StealthUtils.human_type(self.page, input_selector, question)
        
        # Submit
        self.page.keyboard.press("Enter")
        StealthUtils.random_delay(500, 1500)
        
        # Wait for answer
        print("⏳ Waiting for answer...")
        answer = self._wait_for_response()
        
        return answer

    def _wait_for_response(self) -> str:
        """Wait for stable response text."""
        answer = None
        stable_count = 0
        last_text = None
        deadline = time.time() + 120  # 2m timeout
        
        while time.time() < deadline:
            # Check thinking
            try:
                thinking = self.page.query_selector('div.thinking-message')
                if thinking and thinking.is_visible():
                    time.sleep(1)
                    continue
            except:
                pass
                
            # Check response
            for selector in RESPONSE_SELECTORS:
                try:
                    elements = self.page.query_selector_all(selector)
                    if elements:
                        latest = elements[-1]
                        text = latest.inner_text().strip()
                        
                        if text:
                            if text == last_text:
                                stable_count += 1
                                if stable_count >= 3:
                                    return text
                            else:
                                stable_count = 0
                                last_text = text
                except:
                    continue
            
            time.sleep(1)
            
        return None

    def close(self):
        """Cleanup resources."""
        print("🛑 Closing session...")
        if self.context:
            self.context.close()
        if self.playwright:
            self.playwright.stop()
        if self.temp_dir:
            shutil.rmtree(self.temp_dir, ignore_errors=True)
            

def load_questions(domain: str) -> list:
    """Load questions for the specified domain."""
    data_dir = Path(__file__).parent.parent / "data"
    questions_file = data_dir / "domain_questions.json"
    
    if not questions_file.exists():
        print(f"❌ Question file not found: {questions_file}")
        sys.exit(1)
        
    with open(questions_file, 'r') as f:
        data = json.load(f)
        
    return data.get(domain.lower(), [])


def create_brief_header(domain: str, notebook_name: str, company: str) -> str:
    """Create the header for the strategic brief."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""# 🧠 Strategic Intelligence Brief: {domain.title()}
**Target**: {company}
**Source**: NotebookLM ({notebook_name})
**Date**: {timestamp}
**Agent**: Domain Interrogator v2.0 (Single Session)

---

## Executive Summary
*Auto-generated based on the comprehensive interrogation below.*

---

## 🔬 Interrogation Log
"""


def interrogate(domain: str, notebook_id: str, company: str, max_questions: int = 30):
    """
    Execute the interrogation protocol using Single Session architecture.
    """
    # 1. Setup & Auth
    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Please run the base skill's auth setup.")
        sys.exit(1)

    library = NotebookLibrary()
    notebook = library.get_notebook(notebook_id)
    if not notebook:
        print(f"❌ Notebook not found: {notebook_id}")
        sys.exit(1)
    
    # Load questions
    raw_questions = load_questions(domain)
    if not raw_questions:
        print(f"❌ No questions found for domain: {domain}")
        sys.exit(1)
        
    # Format questions
    questions = []
    for q in raw_questions:
        formatted_q = q.replace("{company}", company)
        questions.append(formatted_q)

    # Limit
    if max_questions > 0:
        questions = questions[:max_questions]

    print(f"🚀 Starting {domain.title()} Interrogation of '{notebook['name']}' for {company}")
    print(f"📋 Protocol: {len(questions)} questions")
    
    # 2. Open File for Streaming Output
    output_dir = Path.home() / ".gemini/antigravity/scratch/GoodHabitz-Brand/intelligence"
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"brief_{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    output_path = output_dir / filename
    
    with open(output_path, 'w') as f:
        f.write(create_brief_header(domain, notebook['name'], company))
        
    # 3. Start Session
    session = SessionInterrogator(notebook['url'], headless=False)
    
    try:
        session.start()
        
        # 4. Interrogation Loop
        for i, question in enumerate(questions, 1):
            print(f"\n[{i}/{len(questions)}] ❓ {question}")
            
            # Retry mechanism (Session level)
            answer = None
            for attempt in range(2):
                try:
                    answer = session.ask(question)
                    if answer:
                        break
                except Exception as e:
                    print(f"  ⚠️ Error asking question: {e}")
                    # If catastrophic error, maybe restart session? For now, just retry ask
                
                print("  ⚠️ Retry...")
                time.sleep(2)
                
            if not answer:
                answer = "*ERROR: Could not retrieve answer from NotebookLM.*"
                
            # Strip junk
            clean_answer = answer.replace("EXTREMELY IMPORTANT: Is that ALL you need to know?", "").split("============================================================")[0].strip()
            
            # Stream to file
            with open(output_path, 'a') as f:
                f.write(f"\n### Q{i}: {question}\n")
                f.write(f"\n{clean_answer}\n\n")
                f.write("---\n")
                
            print("  ✅ Insight captured.")
            time.sleep(2) # Short pause between questions
            
    except Exception as e:
        print(f"❌ Session Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        session.close()

    print(f"\n✅ Interrogation Complete!")
    print(f"📄 Strategic Brief saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Domain Interrogator Agent')
    parser.add_argument('--domain', required=True, choices=['marketing', 'sales', 'learning'], help='Domain protocol to execute')
    parser.add_argument('--notebook-id', required=True, help='Target Notebook ID')
    parser.add_argument('--company', required=False, default='the company', help='Company name to inject into questions')
    parser.add_argument('--limit', type=int, default=30, help='Max questions to ask (default: 30)')
    
    args = parser.parse_args()
    
    interrogate(args.domain, args.notebook_id, args.company, args.limit)


if __name__ == "__main__":
    main()
