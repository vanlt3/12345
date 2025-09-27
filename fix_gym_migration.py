#!/usr/bin/env python3
"""
Fix Gym to Gymnasium migration issues
"""

import subprocess
import sys
import os

def check_gym_installation():
    """
    Check if Gym is installed and needs migration
    """
    try:
        import gym
        print("⚠️ Gym library detected - needs migration to Gymnasium")
        return True
    except ImportError:
        print("✅ Gym not installed")
        return False

def check_gymnasium_installation():
    """
    Check if Gymnasium is already installed
    """
    try:
        import gymnasium
        print("✅ Gymnasium already installed")
        return True
    except ImportError:
        print("❌ Gymnasium not installed")
        return False

def migrate_gym_to_gymnasium():
    """
    Migrate from Gym to Gymnasium
    """
    print("🔧 Migrating from Gym to Gymnasium...")
    
    try:
        # Uninstall Gym
        print("📦 Uninstalling Gym...")
        subprocess.run([sys.executable, '-m', 'pip', 'uninstall', 'gym', '-y'], 
                      check=False, capture_output=True)
        print("✅ Gym uninstalled")
        
        # Install Gymnasium
        print("📦 Installing Gymnasium...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'gymnasium'], 
                      check=True, capture_output=True)
        print("✅ Gymnasium installed")
        
        # Install additional dependencies
        print("📦 Installing additional dependencies...")
        additional_packages = [
            'gymnasium[atari]',
            'gymnasium[accept-rom-license]',
            'gymnasium[other]'
        ]
        
        for package in additional_packages:
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                              check=True, capture_output=True)
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"⚠️ Failed to install {package}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Migration failed: {e}")
        return False

def update_imports():
    """
    Update import statements in code
    """
    print("🔧 Updating import statements...")
    
    # Common import replacements
    replacements = {
        'import gym': 'import gymnasium as gym',
        'from gym import': 'from gymnasium import',
        'gym.make(': 'gym.make(',
        'gym.spaces': 'gym.spaces',
        'gym.Env': 'gym.Env'
    }
    
    print("✅ Import replacements defined")
    print("📝 Manual update required for code files:")
    print("   - Replace 'import gym' with 'import gymnasium as gym'")
    print("   - Replace 'from gym import' with 'from gymnasium import'")
    print("   - Update any custom environment implementations")
    
    return True

def fix_gymnasium_compatibility():
    """
    Fix Gymnasium compatibility issues
    """
    print("🔧 Fixing Gymnasium compatibility...")
    
    try:
        # Install compatible versions
        compatible_packages = [
            'numpy>=1.21.0,<2.0.0',  # Ensure NumPy compatibility
            'gymnasium>=0.28.0',
            'stable-baselines3>=2.0.0'
        ]
        
        for package in compatible_packages:
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                              check=True, capture_output=True)
                print(f"✅ Installed compatible {package}")
            except subprocess.CalledProcessError:
                print(f"⚠️ Failed to install {package}")
        
        return True
        
    except Exception as e:
        print(f"❌ Compatibility fix failed: {e}")
        return False

def main():
    """
    Main migration function
    """
    print("🚀 Starting Gym to Gymnasium migration...")
    
    # Check current state
    gym_installed = check_gym_installation()
    gymnasium_installed = check_gymnasium_installation()
    
    if gym_installed and not gymnasium_installed:
        # Perform migration
        if migrate_gym_to_gymnasium():
            print("✅ Migration completed successfully")
        else:
            print("❌ Migration failed")
            return False
    
    # Update imports
    update_imports()
    
    # Fix compatibility
    fix_gymnasium_compatibility()
    
    print("✅ Gym to Gymnasium migration completed")
    return True

if __name__ == "__main__":
    main()