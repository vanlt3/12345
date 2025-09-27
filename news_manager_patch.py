
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
