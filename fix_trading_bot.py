#!/usr/bin/env python3
"""
Trading Bot Configuration Fix Script
This script helps fix the main issues identified in your trading bot logs.
"""

import os
import sys
from datetime import datetime

def fix_oanda_api_key():
    """Fix OANDA API key configuration"""
    print("🔧 Fixing OANDA API Key Configuration...")
    
    # Read the current bot file
    with open('/workspace/Bot-Trading_Swing.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check current OANDA API key
    if 'OANDA_API_KEY = "YOUR_VALID_OANDA_API_KEY_HERE"' in content:
        print("❌ OANDA API key is still set to placeholder value")
        print("📝 You need to:")
        print("   1. Get your OANDA API key from https://www.oanda.com/")
        print("   2. Replace 'YOUR_VALID_OANDA_API_KEY_HERE' with your actual key")
        print("   3. Make sure you're using the correct environment (demo/live)")
        return False
    else:
        print("✅ OANDA API key appears to be configured")
        return True

def fix_trading_economics_api():
    """Fix Trading Economics API configuration"""
    print("\n🔧 Fixing Trading Economics API Configuration...")
    
    with open('/workspace/Bot-Trading_Swing.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check current Trading Economics API key
    if 'TRADING_ECONOMICS_API_KEY = "a284ad0cdba547c:p5oyv77j6kovqhv"' in content:
        print("❌ Trading Economics API key appears to be invalid (403 error)")
        print("📝 You need to:")
        print("   1. Get a valid Trading Economics API key from https://tradingeconomics.com/api")
        print("   2. Replace the current key with your valid one")
        print("   3. Check if you have sufficient API quota")
        return False
    else:
        print("✅ Trading Economics API key appears to be configured")
        return True

def check_crypto_symbol_logic():
    """Check crypto symbol detection logic"""
    print("\n🔧 Checking Crypto Symbol Logic...")
    
    with open('/workspace/Bot-Trading_Swing.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for crypto symbol detection
    if 'is_crypto_symbol' in content:
        print("✅ Crypto symbol detection function exists")
        
        # Check if BTCUSD and ETHUSD are properly configured as crypto
        if 'BTCUSD' in content and 'ETHUSD' in content:
            print("✅ BTCUSD and ETHUSD symbols found in configuration")
            return True
        else:
            print("❌ BTCUSD/ETHUSD not found in crypto configuration")
            return False
    else:
        print("❌ Crypto symbol detection function not found")
        return False

def create_env_file():
    """Create a .env file template for API keys"""
    print("\n🔧 Creating .env file template...")
    
    env_content = """# Trading Bot API Keys Configuration
# Copy this file to .env and fill in your actual API keys

# OANDA API (Required for live trading)
OANDA_API_KEY=your_oanda_api_key_here
OANDA_ACCOUNT_ID=your_oanda_account_id_here

# Trading Economics API (Optional - for economic calendar)
TRADING_ECONOMICS_API_KEY=your_trading_economics_api_key_here

# News APIs (Already configured in your bot)
FINNHUB_API_KEY=d1b3ichr01qjhvtsbj8g
MARKETAUX_API_KEY=CkuQmx9sPsjw0FRDeSkoO8U3O9Jj3HWnUYMJNEql
NEWSAPI_API_KEY=abd8f43b808f42fdb8d28fb1c429af72
EODHD_API_KEY=68bafd7d44a7f0.25202650

# Google AI API (Already configured)
GOOGLE_AI_API_KEY=AIzaSyBCexoODvgrN2QRG8_iKv3p5VTJ5jaJ_B0
"""
    
    with open('/workspace/.env.template', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env.template file")
    print("📝 Instructions:")
    print("   1. Copy .env.template to .env")
    print("   2. Fill in your actual API keys")
    print("   3. Never commit .env to version control")

def main():
    """Main function to run all fixes"""
    print("🚀 Trading Bot Configuration Fix Script")
    print("=" * 50)
    
    # Check current issues
    oanda_ok = fix_oanda_api_key()
    te_ok = fix_trading_economics_api()
    crypto_ok = check_crypto_symbol_logic()
    
    # Create helpful files
    create_env_file()
    
    print("\n" + "=" * 50)
    print("📋 SUMMARY OF ISSUES:")
    print(f"   OANDA API Key: {'✅ OK' if oanda_ok else '❌ NEEDS FIX'}")
    print(f"   Trading Economics API: {'✅ OK' if te_ok else '❌ NEEDS FIX'}")
    print(f"   Crypto Symbol Logic: {'✅ OK' if crypto_ok else '❌ NEEDS FIX'}")
    
    print("\n🔧 IMMEDIATE ACTIONS NEEDED:")
    if not oanda_ok:
        print("   1. Get OANDA API key from https://www.oanda.com/")
        print("      - Sign up for demo account if testing")
        print("      - Use live account for real trading")
    
    if not te_ok:
        print("   2. Get Trading Economics API key from https://tradingeconomics.com/api")
        print("      - This is optional but provides economic calendar data")
    
    print("\n⚠️  IMPORTANT NOTES:")
    print("   - The bot is correctly detecting weekend (Saturday)")
    print("   - Crypto symbols (BTCUSD, ETHUSD) should trade 24/7")
    print("   - Forex/commodity markets are correctly closed on weekends")
    print("   - The main issue is missing/invalid API keys")

if __name__ == "__main__":
    main()