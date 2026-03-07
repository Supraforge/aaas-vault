"""
Configuration for NotebookLM Skill
Centralizes constants, selectors, and paths
"""

from pathlib import Path

# Paths
SKILL_DIR = Path(__file__).parent.parent
DATA_DIR = SKILL_DIR / "data"
PROFILES_DIR = DATA_DIR / "profiles"

# Ensure profiles directory exists
PROFILES_DIR.mkdir(parents=True, exist_ok=True)


class ProfilePaths:
    """Helper to generate paths for a specific profile"""
    def __init__(self, profile_name: str = "default"):
        self.name = profile_name.lower().replace(" ", "-")  # Sanitize
        self.root = PROFILES_DIR / self.name
        self.browser_state_dir = self.root / "browser_state"
        self.browser_profile_dir = self.browser_state_dir / "browser_profile"
        self.state_file = self.browser_state_dir / "state.json"
        self.auth_info_file = self.root / "auth_info.json"
        self.library_file = self.root / "library.json"

        # Ensure directories exist
        self.root.mkdir(parents=True, exist_ok=True)
        self.browser_state_dir.mkdir(parents=True, exist_ok=True)


# Default Profile (backward compatibility — maps to legacy flat data layout)
_default = ProfilePaths("default")
BROWSER_STATE_DIR = _default.browser_state_dir
BROWSER_PROFILE_DIR = _default.browser_profile_dir
STATE_FILE = _default.state_file
AUTH_INFO_FILE = _default.auth_info_file
LIBRARY_FILE = _default.library_file

# NotebookLM Selectors
QUERY_INPUT_SELECTORS = [
    "textarea.query-box-input",  # Primary
    'textarea[aria-label="Feld für Anfragen"]',  # Fallback German
    'textarea[aria-label="Input for queries"]',  # Fallback English
]

RESPONSE_SELECTORS = [
    ".to-user-container .message-text-content",  # Primary
    "[data-message-author='bot']",
    "[data-message-author='assistant']",
]

# Browser Configuration
BROWSER_ARGS = [
    '--disable-blink-features=AutomationControlled',  # Patches navigator.webdriver
    '--disable-dev-shm-usage',
    '--no-sandbox',
    '--no-first-run',
    '--no-default-browser-check'
]

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

# Timeouts
LOGIN_TIMEOUT_MINUTES = 10
QUERY_TIMEOUT_SECONDS = 120
PAGE_LOAD_TIMEOUT = 30000
