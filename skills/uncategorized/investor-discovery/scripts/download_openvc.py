import os
import sys

def main():
    print("=== OpenVC Database Download Helper ===")
    print("\nTo use the Investor Discovery skill, you need to download the OpenVC database:")
    print("\n1. Go to: https://openvc.app/investors")
    print("2. Log in or create a free account.")
    print("3. Click 'Download CSV' or 'Export' (top right).")
    print("4. Save the file as 'openvc_investors.csv'.")
    
    target_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resources")
    target_path = os.path.join(target_dir, "openvc_investors.csv")
    
    print(f"\nOnce downloaded, move the file to:\n{target_path}")
    
    if os.path.exists(target_path):
        print(f"\n✅ Database file already exists at {target_path}")
    else:
        print("\n❌ Database file not found yet.")

if __name__ == "__main__":
    main()
