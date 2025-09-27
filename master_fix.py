#!/usr/bin/env python3
"""
Master Fix Script - Fix all identified issues
"""

import os
import sys
import subprocess
import time

def run_fix_script(script_path: str, description: str) -> bool:
    """
    Run a fix script and return success status
    """
    print(f"\n🔧 {description}...")
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"⚠️ {description} completed with warnings")
            print(f"   Output: {result.stdout}")
            if result.stderr:
                print(f"   Errors: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {description} timed out")
        return False
    except Exception as e:
        print(f"❌ {description} failed: {e}")
        return False

def main():
    """
    Main fix function
    """
    print("🚀 Starting comprehensive fix for Trading Bot issues...")
    print("=" * 60)
    
    # List of fixes to apply
    fixes = [
        ("/workspace/fix_cuda_issues.py", "CUDA/TensorFlow registration issues"),
        ("/workspace/fix_environment.py", "Environment variable issues"),
        ("/workspace/fix_trading_economics_api.py", "Trading Economics API issues"),
        ("/workspace/fix_gym_migration.py", "Gym to Gymnasium migration"),
        ("/workspace/fix_news_manager.py", "News Manager missing methods"),
        ("/workspace/fix_model_loading.py", "Model loading issues")
    ]
    
    success_count = 0
    total_fixes = len(fixes)
    
    for script_path, description in fixes:
        if os.path.exists(script_path):
            if run_fix_script(script_path, description):
                success_count += 1
            time.sleep(1)  # Brief pause between fixes
        else:
            print(f"❌ Fix script not found: {script_path}")
    
    print("\n" + "=" * 60)
    print(f"📊 Fix Summary: {success_count}/{total_fixes} fixes completed successfully")
    
    if success_count == total_fixes:
        print("🎉 All fixes completed successfully!")
        print("\n📝 Next Steps:")
        print("   1. Review the generated patch files")
        print("   2. Apply the patches to your bot code")
        print("   3. Restart your trading bot")
        print("   4. Monitor the logs for any remaining issues")
    else:
        print("⚠️ Some fixes had issues - please review the output above")
        print("\n📝 Manual fixes may be required for:")
        print("   - Trading Economics API key validation")
        print("   - Model file paths and permissions")
        print("   - Environment variable configuration")
    
    return success_count == total_fixes

if __name__ == "__main__":
    main()