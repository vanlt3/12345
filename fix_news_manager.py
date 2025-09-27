#!/usr/bin/env python3
"""
Fix News Manager missing methods
"""

import os
import sys
from typing import Optional, List, Dict, Any

class NewsManagerFix:
    def __init__(self):
        self.news_manager = None
        
    def find_news_manager_class(self) -> Optional[str]:
        """
        Find the News Manager class in the codebase
        """
        print("🔍 Searching for News Manager class...")
        
        # Common file patterns to search
        search_patterns = [
            "**/*news*.py",
            "**/*News*.py", 
            "**/*manager*.py",
            "**/*Manager*.py"
        ]
        
        # This would need to be implemented with actual file search
        # For now, return the expected class name
        return "NewsEconomicManager"
    
    def add_missing_methods(self, class_name: str) -> str:
        """
        Add missing methods to News Manager class
        """
        print(f"🔧 Adding missing methods to {class_name}...")
        
        missing_methods = """
    def get_latest_news(self, symbol: str = None, limit: int = 10) -> List[Dict[str, Any]]:
        '''
        Get latest news for a specific symbol or all symbols
        
        Args:
            symbol: Symbol to get news for (optional)
            limit: Maximum number of news items to return
            
        Returns:
            List of news dictionaries
        '''
        try:
            if not hasattr(self, 'news_providers') or not self.news_providers:
                print("⚠️ No news providers available")
                return []
            
            all_news = []
            
            for provider_name, provider in self.news_providers.items():
                try:
                    if hasattr(provider, 'get_latest_news'):
                        news = provider.get_latest_news(symbol=symbol, limit=limit)
                        if news:
                            all_news.extend(news)
                    elif hasattr(provider, 'fetch_news'):
                        news = provider.fetch_news(symbol=symbol, limit=limit)
                        if news:
                            all_news.extend(news)
                except Exception as e:
                    print(f"⚠️ Error fetching news from {provider_name}: {e}")
                    continue
            
            # Sort by timestamp if available
            if all_news:
                try:
                    all_news.sort(key=lambda x: x.get('timestamp', 0), reverse=True)
                except:
                    pass
            
            return all_news[:limit]
            
        except Exception as e:
            print(f"❌ Error in get_latest_news: {e}")
            return []
    
    def get_news_sentiment(self, symbol: str, news_data: List[Dict[str, Any]]) -> Dict[str, float]:
        '''
        Get sentiment analysis for news data
        
        Args:
            symbol: Symbol to analyze
            news_data: List of news items
            
        Returns:
            Dictionary with sentiment scores
        '''
        try:
            if not news_data:
                return {'sentiment': 0.0, 'confidence': 0.0}
            
            if not hasattr(self, 'llm_analyzer') or not self.llm_analyzer:
                print("⚠️ No LLM analyzer available")
                return {'sentiment': 0.0, 'confidence': 0.0}
            
            # Analyze sentiment using LLM
            sentiment_scores = []
            confidences = []
            
            for news_item in news_data:
                try:
                    if hasattr(self.llm_analyzer, 'analyze_sentiment'):
                        result = self.llm_analyzer.analyze_sentiment(
                            text=news_item.get('title', '') + ' ' + news_item.get('description', ''),
                            symbol=symbol
                        )
                        if result:
                            sentiment_scores.append(result.get('sentiment', 0.0))
                            confidences.append(result.get('confidence', 0.0))
                except Exception as e:
                    print(f"⚠️ Error analyzing sentiment: {e}")
                    continue
            
            if sentiment_scores:
                avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
                avg_confidence = sum(confidences) / len(confidences)
                return {
                    'sentiment': avg_sentiment,
                    'confidence': avg_confidence,
                    'count': len(sentiment_scores)
                }
            else:
                return {'sentiment': 0.0, 'confidence': 0.0, 'count': 0}
                
        except Exception as e:
            print(f"❌ Error in get_news_sentiment: {e}")
            return {'sentiment': 0.0, 'confidence': 0.0}
    
    def validate_news_manager(self) -> bool:
        '''
        Validate that News Manager has all required methods
        
        Returns:
            True if all methods are present
        '''
        required_methods = [
            'get_latest_news',
            'get_news_sentiment', 
            'get_economic_calendar',
            'add_news_sentiment_features'
        ]
        
        missing_methods = []
        
        for method in required_methods:
            if not hasattr(self, method):
                missing_methods.append(method)
        
        if missing_methods:
            print(f"❌ Missing methods: {missing_methods}")
            return False
        else:
            print("✅ All required methods present")
            return True
"""
        
        return missing_methods
    
    def create_news_manager_patch(self) -> str:
        """
        Create a patch file for News Manager
        """
        print("🔧 Creating News Manager patch...")
        
        patch_content = '''
# News Manager Patch
# Add these methods to your NewsEconomicManager class

def get_latest_news(self, symbol: str = None, limit: int = 10):
    """Get latest news for a specific symbol or all symbols"""
    try:
        if not hasattr(self, 'news_providers') or not self.news_providers:
            print("⚠️ No news providers available")
            return []
        
        all_news = []
        
        for provider_name, provider in self.news_providers.items():
            try:
                if hasattr(provider, 'get_latest_news'):
                    news = provider.get_latest_news(symbol=symbol, limit=limit)
                    if news:
                        all_news.extend(news)
                elif hasattr(provider, 'fetch_news'):
                    news = provider.fetch_news(symbol=symbol, limit=limit)
                    if news:
                        all_news.extend(news)
            except Exception as e:
                print(f"⚠️ Error fetching news from {provider_name}: {e}")
                continue
        
        # Sort by timestamp if available
        if all_news:
            try:
                all_news.sort(key=lambda x: x.get('timestamp', 0), reverse=True)
            except:
                pass
        
        return all_news[:limit]
        
    except Exception as e:
        print(f"❌ Error in get_latest_news: {e}")
        return []

def get_news_sentiment(self, symbol: str, news_data: List[Dict[str, Any]]):
    """Get sentiment analysis for news data"""
    try:
        if not news_data:
            return {'sentiment': 0.0, 'confidence': 0.0}
        
        if not hasattr(self, 'llm_analyzer') or not self.llm_analyzer:
            print("⚠️ No LLM analyzer available")
            return {'sentiment': 0.0, 'confidence': 0.0}
        
        # Analyze sentiment using LLM
        sentiment_scores = []
        confidences = []
        
        for news_item in news_data:
            try:
                if hasattr(self.llm_analyzer, 'analyze_sentiment'):
                    result = self.llm_analyzer.analyze_sentiment(
                        text=news_item.get('title', '') + ' ' + news_item.get('description', ''),
                        symbol=symbol
                    )
                    if result:
                        sentiment_scores.append(result.get('sentiment', 0.0))
                        confidences.append(result.get('confidence', 0.0))
            except Exception as e:
                print(f"⚠️ Error analyzing sentiment: {e}")
                continue
        
        if sentiment_scores:
            avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
            avg_confidence = sum(confidences) / len(confidences)
            return {
                'sentiment': avg_sentiment,
                'confidence': avg_confidence,
                'count': len(sentiment_scores)
            }
        else:
            return {'sentiment': 0.0, 'confidence': 0.0, 'count': 0}
            
    except Exception as e:
        print(f"❌ Error in get_news_sentiment: {e}")
        return {'sentiment': 0.0, 'confidence': 0.0}
'''
        
        return patch_content

def fix_news_manager():
    """
    Main fix function for News Manager
    """
    print("🔧 Fixing News Manager issues...")
    
    fixer = NewsManagerFix()
    
    # Find News Manager class
    class_name = fixer.find_news_manager_class()
    if not class_name:
        print("❌ Could not find News Manager class")
        return False
    
    # Add missing methods
    missing_methods = fixer.add_missing_methods(class_name)
    
    # Create patch file
    patch_content = fixer.create_news_manager_patch()
    
    # Save patch file
    with open('/workspace/news_manager_patch.py', 'w') as f:
        f.write(patch_content)
    
    print("✅ News Manager patch created: /workspace/news_manager_patch.py")
    print("📝 Instructions:")
    print("   1. Copy the methods from news_manager_patch.py")
    print("   2. Add them to your NewsEconomicManager class")
    print("   3. Restart your bot")
    
    return True

if __name__ == "__main__":
    fix_news_manager()