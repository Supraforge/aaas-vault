import argparse
import os
import requests
import sys

def load_env():
    """
    Manually loads .env file if it exists.
    """
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, _, value = line.partition('=')
                    if key and value:
                        os.environ[key.strip()] = value.strip()

def select_model(strategy="reasoning"):
    load_env()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Fallback Defaults (Safe Base)
    defaults = {
        "speed": "gemini-1.5-flash",
        "reasoning": "gemini-1.5-pro",
        "vision": "gemini-1.5-pro"
    }
    
    if not api_key:
        # Fail safe if API key is missing
        print(defaults.get(strategy, "gemini-1.5-flash"))
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            models = [m['name'].replace('models/', '') for m in data.get('models', [])]
            
            # 1. Strategy: SPEED
            if strategy == "speed":
                # Priority: 2.0 Flash -> 1.5 Flash -> Flash
                if any("gemini-2.0-flash" in m for m in models):
                     # Prefer stable 2.0 flash
                    print(next((m for m in models if "gemini-2.0-flash" in m and "preview" not in m), "gemini-2.0-flash"))
                    return
                elif "gemini-1.5-flash" in models:
                    print("gemini-1.5-flash")
                    return
            
            # 2. Strategy: REASONING / VISION
            elif strategy in ["reasoning", "vision"]:
                 # Priority: 2.5 Pro -> 2.0 Pro -> 1.5 Pro
                if any("gemini-2.5-pro" in m for m in models):
                    print("gemini-2.5-pro")
                    return
                if any("gemini-1.5-pro" in m for m in models):
                     # Find latest 1.5 pro (avoid experimental if standard exists)
                    print("gemini-1.5-pro")
                    return
            
            # If sophisticated matching failed, fall back to defaults
            print(defaults.get(strategy, "gemini-1.5-flash"))
            
        else:
            # API Error -> use default
            print(defaults.get(strategy, "gemini-1.5-flash"))
            
    except Exception:
        # Network/Code Error -> use default
        print(defaults.get(strategy, "gemini-1.5-flash"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM Router")
    parser.add_argument("--strategy", type=str, default="reasoning", choices=["speed", "reasoning", "vision"], help="Selection strategy")
    args = parser.parse_args()
    
    select_model(args.strategy)
