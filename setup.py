#!/usr/bin/env python3
"""
Setup script for Python Games Collection
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main setup function"""
    print("🎮 Python Games Collection - Setup Script")
    print("=" * 50)
    
    # Check if virtual environment exists
    if not os.path.exists("venv"):
        print("❌ Virtual environment not found!")
        print("Please create a virtual environment first:")
        print("python -m venv venv")
        return False
    
    # Install dependencies
    if not run_command("venv\\Scripts\\pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    print("\n🎉 Setup completed successfully!")
    print("\nTo start playing:")
    print("1. Activate virtual environment: venv\\Scripts\\activate")
    print("2. Run the game: python main.py")
    print("\nHave fun gaming! 🎮")
    
    return True

if __name__ == "__main__":
    main()
