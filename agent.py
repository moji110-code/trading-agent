import requests

def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data["price"])

def decide(price):
    if price < 60000:
        return "BUY"
    elif price > 65000:
        return "SELL"
    else:
        return "HOLD"

def run():
    price = get_price()
    action = decide(price)
    print(f"Price: {price} | Action: {action}")

if __name__ == "__main__":
    run()
