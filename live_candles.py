import yfinance as yf
import mplfinance as mpf
import pandas as pd

# دانلود داده
df = yf.download("BTC-USD", interval="1m", period="1d")

# اگر ستون‌ها چندلایه بودن (MultiIndex) صافشون میکنیم
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] for col in df.columns]

# انتخاب ستون‌های لازم
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# حذف NaN
df = df.dropna()

# تبدیل به float
df = df.astype(float)

print(df.head())

# رسم کندل
mpf.plot(
    df,
    type="candle",
    style="charles",
    title="BTC/USDT (Yahoo Finance)",
    ylabel="Price ($)"
)
