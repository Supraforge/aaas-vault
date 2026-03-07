import argparse
import subprocess
import os
import sys

def run_retrieval(topic, notebook_id=None):
    """
    Orchestrates intelligence retrieval by calling the base notebooklm skill.
    """
    base_skill_path = "/Users/user/.gemini/skills/notebooklm"
    run_script = os.path.join(base_skill_path, "scripts", "run.py")
    
    if not os.path.exists(run_script):
        print(f"Error: Base notebooklm skill not found at {base_skill_path}")
        sys.exit(1)

    # Construct the command for the base skill
    cmd = [
        "python3", run_script, "ask_question.py",
        "--question", f"Please provide a detailed, source-grounded summary about: {topic}. Include specific facts and source citations.",
    ]
    
    if notebook_id:
        cmd.extend(["--notebook-id", notebook_id])

    print(f"🔍 Sourcing intelligence for: {topic}...")
    
    try:
        # Execute the question command
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # In a real implementation, we would pulse for status if it's long-running,
        # but ask_question.py typically completes synchronously in this setup.
        
        print("\n--- 🧠 Grounded Intelligence Payload ---")
        print(result.stdout)
        print("------------------------------------------")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during intelligence retrieval: {e}")
        print(e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NotebookLM Intelligence Retrieval Agent")
    parser.add_argument("--topic", required=True, help="Subject to retrieve intelligence for")
    parser.add_argument("--notebook-id", help="Optional Notebook ID")
    
    args = parser.parse_args()
    run_retrieval(args.topic, args.notebook_id)
