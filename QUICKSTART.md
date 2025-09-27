# Quickstart Guide - Enhanced Trading Bot

## 🚀 Quick Start

### 1. Local Setup
```bash
# Set environment variables
export ENV=paper
export FINNHUB_API_KEY=your_finnhub_key
export ALPHAVANTAGE_API_KEY=your_alpha_vantage_key

# Run with default settings
python Bot-Trading_Swing.py --symbols EURUSD,BTCUSD,XAUUSD --timeframe 5m --enable-monitor --agent ensemble --dry-run
```

### 2. Colab Setup
```python
# Set environment variables
%env ENV=paper
%env FINNHUB_API_KEY=your_finnhub_key
%env ALPHAVANTAGE_API_KEY=your_alpha_vantage_key

# Run the bot
!python Bot-Trading_Swing.py --symbols EURUSD,BTCUSD,XAUUSD --timeframe 5m --enable-monitor --agent ensemble --dry-run
```

### 3. Self-Test
```bash
python Bot-Trading_Swing.py --self-test
```

## 🔧 Configuration Examples

### Conservative Settings
```bash
python Bot-Trading_Swing.py \
  --env paper \
  --symbols EURUSD,GBPUSD \
  --timeframe 1h \
  --risk-per-trade 0.5 \
  --max-daily-dd 2.0 \
  --max-weekly-dd 4.0 \
  --max-open-trades 3 \
  --agent rule \
  --enable-monitor \
  --dry-run
```

### Aggressive Settings
```bash
python Bot-Trading_Swing.py \
  --env paper \
  --symbols EURUSD,BTCUSD,XAUUSD,GBPUSD,USDJPY \
  --timeframe 5m \
  --risk-per-trade 1.5 \
  --max-daily-dd 3.0 \
  --max-weekly-dd 6.0 \
  --max-open-trades 8 \
  --agent ensemble \
  --enable-monitor \
  --enable-news \
  --enable-trailing
```

### Production Settings
```bash
python Bot-Trading_Swing.py \
  --env prod \
  --symbols EURUSD,GBPUSD \
  --timeframe 1h \
  --risk-per-trade 1.0 \
  --max-daily-dd 2.5 \
  --max-weekly-dd 5.0 \
  --max-open-trades 5 \
  --agent ensemble \
  --enable-monitor \
  --enable-news
```

## 📊 Monitoring Commands

### Check Logs
```bash
# View real-time logs
tail -f ./bot_runtime/logs/trading_bot.log

# Filter by channel
grep "Signal" ./bot_runtime/logs/trading_bot.log
grep "Risk" ./bot_runtime/logs/trading_bot.log
grep "Monitor" ./bot_runtime/logs/trading_bot.log
```

### Monitor Performance
```bash
# Check decision history
grep "Decision:" ./bot_runtime/logs/trading_bot.log | tail -20

# Check circuit breaker events
grep "circuit breaker" ./bot_runtime/logs/trading_bot.log

# Check price aggregator performance
grep "PriceAggregator" ./bot_runtime/logs/trading_bot.log | tail -10
```

## 🛠️ Troubleshooting

### Common Issues

1. **API Key Missing**
   ```bash
   # Check if API keys are set
   echo $FINNHUB_API_KEY
   echo $ALPHAVANTAGE_API_KEY
   ```

2. **Permission Issues (Colab)**
   ```python
   # Mount Google Drive
   from google.colab import drive
   drive.mount('/content/drive')
   ```

3. **Import Errors**
   ```bash
   # Install missing packages
   pip install aiohttp requests numpy pandas
   ```

4. **Self-Test Failures**
   ```bash
   # Run individual tests
   python Bot-Trading_Swing.py --self-test
   # Check specific test results in output
   ```

### Debug Mode
```bash
# Enable verbose logging
python Bot-Trading_Swing.py --symbols EURUSD --timeframe 5m --dry-run --enable-monitor 2>&1 | tee debug.log
```

## 📈 Performance Tuning

### For Low-Spec Machines
```bash
# Reduce monitoring frequency
python Bot-Trading_Swing.py \
  --symbols EURUSD \
  --timeframe 1h \
  --monitor-interval 5 \
  --disable-news \
  --agent rule
```

### For High-Performance
```bash
# Enable all features
python Bot-Trading_Swing.py \
  --symbols EURUSD,BTCUSD,XAUUSD,GBPUSD,USDJPY \
  --timeframe 5m \
  --monitor-interval 1 \
  --enable-monitor \
  --enable-news \
  --enable-trailing \
  --agent ensemble
```

## 🔒 Security Notes

- API keys are read from environment variables only
- No secrets are logged or stored in files
- All sensitive data is redacted in logs
- Use `--dry-run` for testing without real trades

## 📞 Support

For issues or questions:
1. Check the logs in `./bot_runtime/logs/`
2. Run self-tests: `python Bot-Trading_Swing.py --self-test`
3. Review the UPGRADE_SUMMARY.md for detailed feature documentation