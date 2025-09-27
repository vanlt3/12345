
def get_enhanced_signal_fixed(self, symbol: str, data: pd.DataFrame, regime: int) -> Tuple[str, float]:
    """
    Fixed version of get_enhanced_signal with better error handling
    """
    try:
        # Check if models exist
        trending_model = getattr(self, f'trending_model_{symbol}', None)
        ranging_model = getattr(self, f'ranging_model_{symbol}', None)
        
        if not trending_model and not ranging_model:
            print(f"⚠️ No models available for {symbol}, using fallback")
            return self._get_fallback_signal(symbol, data)
        
        # Determine which model to use based on regime
        if regime == 1 and trending_model:
            model = trending_model
            model_type = "trending"
        elif regime == -1 and ranging_model:
            model = ranging_model
            model_type = "ranging"
        elif trending_model:
            model = trending_model
            model_type = "trending"
        elif ranging_model:
            model = ranging_model
            model_type = "ranging"
        else:
            return self._get_fallback_signal(symbol, data)
        
        # Get prediction
        try:
            prediction = model.predict(data.tail(1))[0]
            confidence = getattr(model, 'confidence_', 0.5)
            
            # Convert prediction to signal
            if prediction == 1:
                signal = "BUY"
            elif prediction == 2:
                signal = "SELL"
            else:
                signal = "HOLD"
            
            return signal, confidence
            
        except Exception as e:
            print(f"⚠️ Model prediction failed for {symbol}: {e}")
            return self._get_fallback_signal(symbol, data)
            
    except Exception as e:
        print(f"❌ Error in get_enhanced_signal for {symbol}: {e}")
        return "HOLD", 0.5

def _get_fallback_signal(self, symbol: str, data: pd.DataFrame) -> Tuple[str, float]:
    """
    Get fallback signal when models are not available
    """
    try:
        # Simple technical analysis fallback
        if len(data) < 20:
            return "HOLD", 0.5
        
        # Calculate simple moving averages
        sma_20 = data['close'].rolling(20).mean().iloc[-1]
        sma_50 = data['close'].rolling(50).mean().iloc[-1]
        current_price = data['close'].iloc[-1]
        
        # Simple signal logic
        if current_price > sma_20 > sma_50:
            return "BUY", 0.6
        elif current_price < sma_20 < sma_50:
            return "SELL", 0.6
        else:
            return "HOLD", 0.5
            
    except Exception as e:
        print(f"❌ Fallback signal failed for {symbol}: {e}")
        return "HOLD", 0.5
