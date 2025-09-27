#!/usr/bin/env python3
"""
Test Runner for Trading Bot
Run this to test your bot in safe mode
"""

import sys
import os

def run_test():
    """Run the bot in test mode"""
    print("🧪 Starting Trading Bot Test Mode...")
    print("⚠️  This version will work without API keys")
    print("📊 Crypto symbols (BTCUSD, ETHUSD) should be active")
    print("🚫 Forex/commodity markets will be closed (weekend)")
    print()
    
    try:
        # Import and run the test version
        sys.path.append('/workspace')
        from Bot_Trading_Swing_Test import *
        
        print("✅ Bot test version loaded successfully")
        print("🔧 You can now test the bot functionality")
        
    except Exception as e:
        print(f"❌ Error running test version: {e}")
        print("💡 Make sure you have all required Python packages installed")

if __name__ == "__main__":
    run_test()
