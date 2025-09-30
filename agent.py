import requests
import csv

# گرفتن کندل‌ها
def get_candles(symbol="BTCUSDT", interval="4h", limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    data = requests.get(url).json()
    return data

# پیدا کردن خطوط حمایت/مقاومت
def find_support_resistance(candles):
    lines = []
    closes = [float(c[4]) for c in candles]
    opens = [float(c[1]) for c in candles]
    prices = closes + opens

    for price in prices:
        touches = sum(1 for c in candles if abs(float(c[1])-price)<0.5 or abs(float(c[4])-price)<0.5)
        if touches >= 2:
            lines.append(price)
    return list(sorted(set(lines)))

# ذخیره خطوط در CSV
def save_lines_csv(lines, filename="lines_for_tradingview.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Price"])
        for line in lines:
            writer.writerow([line])
    print(f"{filename} created with {len(lines)} lines!")

# اجرا
def run():
    candles = get_candles()
    lines = find_support_resistance(candles)
    save_lines_csv(lines)

if __name__ == "__main__":
    run()
