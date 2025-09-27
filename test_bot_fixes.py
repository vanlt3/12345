#!/usr/bin/env python3
"""
Test script để kiểm tra các sửa đổi bot
"""

import sys
import os
import logging
from datetime import datetime

# Add workspace to path
sys.path.insert(0, '/workspace')

def test_crypto_symbols():
    """Test crypto symbols handling"""
    print("🧪 Testing crypto symbols handling...")
    
    try:
        # Import bot functions
        from Bot-Trading_Swing import is_crypto_symbol, is_market_open, SYMBOLS
        
        # Test crypto symbols
        crypto_symbols = ["BTCUSD", "ETHUSD"]
        for symbol in crypto_symbols:
            is_crypto = is_crypto_symbol(symbol)
            is_open = is_market_open(symbol)
            print(f"  {symbol}: crypto={is_crypto}, market_open={is_open}")
            
            if not is_crypto:
                print(f"❌ {symbol} should be crypto but isn't")
                return False
            if not is_open:
                print(f"❌ {symbol} market should be open but isn't")
                return False
        
        print("✅ Crypto symbols test passed")
        return True
        
    except Exception as e:
        print(f"❌ Crypto symbols test failed: {e}")
        return False

def test_api_connection():
    """Test API connection handling"""
    print("🧪 Testing API connection handling...")
    
    try:
        from Bot-Trading_Swing import EnhancedTradingBot
        
        # Create bot instance
        bot = EnhancedTradingBot()
        
        # Test API connection (should not crash)
        api_connected = bot.check_api_connection()
        print(f"  API connection result: {api_connected}")
        
        # Test that bot doesn't crash on API failure
        print("✅ API connection test passed (no crash)")
        return True
        
    except Exception as e:
        print(f"❌ API connection test failed: {e}")
        return False

def test_active_symbols():
    """Test active symbols initialization"""
    print("🧪 Testing active symbols initialization...")
    
    try:
        from Bot-Trading_Swing import EnhancedTradingBot, is_crypto_symbol
        
        # Create bot instance
        bot = EnhancedTradingBot()
        
        # Check active symbols
        print(f"  Active symbols: {list(bot.active_symbols)}")
        
        # Check crypto symbols are in active symbols
        crypto_symbols = [s for s in bot.active_symbols if is_crypto_symbol(s)]
        print(f"  Crypto symbols in active: {crypto_symbols}")
        
        if len(crypto_symbols) == 0:
            print("❌ No crypto symbols in active symbols")
            return False
        
        print("✅ Active symbols test passed")
        return True
        
    except Exception as e:
        print(f"❌ Active symbols test failed: {e}")
        return False

def test_weekend_handling():
    """Test weekend handling"""
    print("🧪 Testing weekend handling...")
    
    try:
        from Bot-Trading_Swing import is_weekend, is_market_open
        
        # Test weekend detection
        is_weekend_now = is_weekend()
        print(f"  Is weekend: {is_weekend_now}")
        
        # Test crypto symbols on weekend
        crypto_symbols = ["BTCUSD", "ETHUSD"]
        for symbol in crypto_symbols:
            is_open = is_market_open(symbol)
            print(f"  {symbol} market open on weekend: {is_open}")
            
            if not is_open:
                print(f"❌ {symbol} should be open on weekend")
                return False
        
        print("✅ Weekend handling test passed")
        return True
        
    except Exception as e:
        print(f"❌ Weekend handling test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Running bot fix tests...")
    print("=" * 50)
    
    tests = [
        test_crypto_symbols,
        test_api_connection,
        test_active_symbols,
        test_weekend_handling
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Bot fixes are working correctly.")
    else:
        print("⚠️ Some tests failed. Please check the issues above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)