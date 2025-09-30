# trading-agent
# Trading Agent — Simple version

## What it is
A simple trading agent that:
- fetches 4H candles (Open/Close) and finds support/resistance lines,
- evaluates signals (bounce / breakout + volume),
- prints recommended action (BUY / SELL / HOLD) and suggested capital % (1.5%).

## Files
- `agent.py` — main logic (support/resistance detection, decision)
- `plot_candles.py` — draws candlestick chart with validated lines
- `plot_agent_live.py` — (optional) live price plotting from Yahoo
- `requirements.txt` — Python dependencies

## How to run (local)
1. Install Python 3.10+.
2. Create virtualenv (optional):
