import requests
import matplotlib.pyplot as plt

# خطوط نمونه حمایت/مقاومت
validated_lines = [108994.49, 109027.785, 109133.5, 109172.205, 109320.02, 109360.0, 109580.005]

# گرفتن قیمت واقعی بیت‌کوین از Binance
def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data["price"])

# تصمیم ساده: BUY / SELL / HOLD
def decide(price):
    if price < validated_lines[0]:
        return "BUY"
    elif price > validated_lines[-1]:
        return "SELL"
    else:
        return "HOLD"

# گرفتن قیمت و Action
current_price = get_price()
action = decide(current_price)

# رسم نمودار
plt.figure(figsize=(10,6))
plt.title(f"Price: {current_price} | Action: {action}")

# خطوط حمایت/مقاومت
for line in validated_lines:
    plt.axhline(y=line, color='green', linestyle='--')

# خط قیمت فعلی
plt.axhline(y=current_price, color='red', linestyle='-')

plt.xlabel("Time (simulated)")
plt.ylabel("Price")
plt.show()
