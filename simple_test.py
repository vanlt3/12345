#!/usr/bin/env python3
"""
Simple test để kiểm tra bot có chạy được không
"""

import sys
import os

# Add workspace to path
sys.path.insert(0, '/workspace')

def test_bot_startup():
    """Test bot startup"""
    print("🧪 Testing bot startup...")
    
    try:
        # Try to run the bot file
        result = os.system("cd /workspace && python3 Bot-Trading_Swing.py")
        
        if result == 0:
            print("✅ Bot startup test passed")
            return True
        else:
            print(f"❌ Bot startup test failed with exit code: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Bot startup test failed: {e}")
        return False

def main():
    """Run test"""
    print("🚀 Running simple bot test...")
    print("=" * 50)
    
    success = test_bot_startup()
    
    print("=" * 50)
    if success:
        print("🎉 Bot test passed! Bot should work correctly now.")
    else:
        print("⚠️ Bot test failed. Please check the issues above.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)