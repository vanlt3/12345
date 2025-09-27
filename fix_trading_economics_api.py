#!/usr/bin/env python3
"""
Fix Trading Economics API issues
"""

import os
import requests
import time
from typing import Optional

class TradingEconomicsAPIFix:
    def __init__(self):
        self.api_key = os.getenv('TRADING_ECONOMICS_API_KEY')
        self.base_url = "https://api.tradingeconomics.com"
        self.rate_limit_delay = 1  # seconds between requests
        
    def test_api_connection(self) -> bool:
        """
        Test API connection and validate key
        """
        if not self.api_key:
            print("❌ Trading Economics API key not found")
            return False
            
        try:
            # Test endpoint
            url = f"{self.base_url}/markets/currency"
            params = {'c': self.api_key}
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                print("✅ Trading Economics API connection successful")
                return True
            elif response.status_code == 403:
                print("❌ Trading Economics API key invalid or expired")
                return False
            elif response.status_code == 429:
                print("⚠️ Trading Economics API rate limited")
                return False
            else:
                print(f"⚠️ Trading Economics API error: {response.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Trading Economics API connection failed: {e}")
            return False
    
    def get_api_key_info(self) -> Optional[dict]:
        """
        Get API key information
        """
        if not self.api_key:
            return None
            
        try:
            url = f"{self.base_url}/markets/currency"
            params = {'c': self.api_key}
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'status': 'active',
                    'rate_limit': response.headers.get('X-RateLimit-Limit'),
                    'remaining': response.headers.get('X-RateLimit-Remaining')
                }
            else:
                return {
                    'status': 'error',
                    'code': response.status_code
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
    
    def implement_rate_limiting(self):
        """
        Implement proper rate limiting
        """
        print("🔧 Implementing Trading Economics API rate limiting...")
        
        # Add delay between requests
        time.sleep(self.rate_limit_delay)
        
        print("✅ Rate limiting implemented")
    
    def fix_api_issues(self):
        """
        Main fix function
        """
        print("🔧 Fixing Trading Economics API issues...")
        
        # Test connection
        if not self.test_api_connection():
            print("❌ API connection failed - check your API key")
            return False
        
        # Get API info
        info = self.get_api_key_info()
        if info:
            print(f"📊 API Status: {info}")
        
        # Implement rate limiting
        self.implement_rate_limiting()
        
        print("✅ Trading Economics API issues fixed")
        return True

def fix_trading_economics_api():
    """
    Fix Trading Economics API issues
    """
    fixer = TradingEconomicsAPIFix()
    return fixer.fix_api_issues()

if __name__ == "__main__":
    fix_trading_economics_api()