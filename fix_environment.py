#!/usr/bin/env python3
"""
Fix Environment Variable issues
"""

import os
import subprocess
import sys

def fix_environment_variables():
    """
    Fix environment variable issues
    """
    print("🔧 Fixing environment variable issues...")
    
    # Fix ENV variable issue
    if 'ENV' in os.environ:
        env_value = os.environ['ENV']
        if env_value == '/root/.bashrc':
            print("⚠️ Invalid ENV value detected, removing...")
            del os.environ['ENV']
            print("✅ Invalid ENV variable removed")
    
    # Set proper environment variables
    proper_env_vars = {
        'PYTHONPATH': '/workspace',
        'PYTHONUNBUFFERED': '1',
        'TF_CPP_MIN_LOG_LEVEL': '2',
        'CUDA_VISIBLE_DEVICES': '0',
        'TF_FORCE_GPU_ALLOW_GROWTH': 'true'
    }
    
    for key, value in proper_env_vars.items():
        os.environ[key] = value
        print(f"✅ Set {key}={value}")
    
    # Fix shell environment
    try:
        # Update shell environment
        subprocess.run(['export', 'ENV=""'], shell=True, check=False)
        print("✅ Shell environment updated")
    except Exception as e:
        print(f"⚠️ Shell environment update warning: {e}")
    
    print("✅ Environment variable issues fixed")

def fix_python_environment():
    """
    Fix Python environment issues
    """
    print("🔧 Fixing Python environment...")
    
    # Ensure proper Python path
    python_path = sys.executable
    print(f"✅ Python executable: {python_path}")
    
    # Check Python version
    python_version = sys.version
    print(f"✅ Python version: {python_version}")
    
    # Set proper working directory
    os.chdir('/workspace')
    print("✅ Working directory set to /workspace")
    
    print("✅ Python environment fixed")

def fix_system_environment():
    """
    Fix system-level environment issues
    """
    print("🔧 Fixing system environment...")
    
    # Remove problematic environment variables
    problematic_vars = ['ENV']
    
    for var in problematic_vars:
        if var in os.environ:
            del os.environ[var]
            print(f"✅ Removed problematic variable: {var}")
    
    # Set system environment
    os.environ['LANG'] = 'en_US.UTF-8'
    os.environ['LC_ALL'] = 'en_US.UTF-8'
    print("✅ System environment configured")
    
    print("✅ System environment fixed")

if __name__ == "__main__":
    fix_environment_variables()
    fix_python_environment()
    fix_system_environment()