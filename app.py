from flask import Flask, request, json
import requests
import time

app = Flask(__name__)

@app.route("/backtest", methods= )
def backtest():
    data = request.get_json()
    symbol = data.get("symbol", "QQQ")
    try:
    url = "https://query1.finance.yahoo.com/v8/finance/chart/" + symbol   
 https://query1.finance.yahoo.com/v8/finance/chart/" + symbol
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        result = r.json()
        meta = result  [0] price = meta.get("regularMarketPrice")
        bid = meta.get("bid", price)
        ask = meta.get("ask", price)
        return json.dumps({
            "symbol": symbol,
            "price": price,
            "bid": bid,
            "ask": ask,
            "timestamp": int(time.time())
        })
    except Exception as e:
        return json.dumps({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
