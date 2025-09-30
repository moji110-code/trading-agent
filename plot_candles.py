import pandas as pd
import mplfinance as mpf

# خواندن دیتای کندل از فایل CSV
df = pd.read_csv("data.csv", parse_dates=["date"], index_col="date")

# رسم کندل‌استیک
mpf.plot(
    df,
    type="candle",          # نوع چارت (کندل)
    style="charles",        # استایل (charles / binance / classic ...)
    volume=True,            # نمایش حجم
    title="My First Trading Chart"  # عنوان
)
