import requests
import time
import os

# Konfiguration (deine Daten)
API_KEY = "MZBPMPUQ8E097P2R"
BOT_TOKEN = "7745598671:AAEUi_SDwtCpYuVzaBL7EJ10huMNYas"
CHAT_ID = "2011080524"

# Trading-Signal-Logik (einfaches Beispiel mit RSI)
def fetch_data():
    url = f"https://www.alphavantage.co/query?function=RSI&symbol=XAUUSD&interval=1min&time_period=14&series_type=close&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    try:
        latest_timestamp = list(data["Technical Analysis: RSI"].keys())[0]
        rsi_value = float(data["Technical Analysis: RSI"][latest_timestamp]["RSI"])
        return rsi_value
    except Exception as e:
        print(f"Fehler beim Abrufen: {e}")
        return None

def send_signal(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(telegram_url, data=payload)

def main():
    while True:
        rsi = fetch_data()
        if rsi:
            if rsi < 30:
                send_signal("📈 RSI ist unter 30 – Kaufsignal!")
            elif rsi > 70:
                send_signal("📉 RSI ist über 70 – Verkaufssignal!")
            else:
                print(f"RSI neutral bei {rsi}")
        time.sleep(60)

if __name__ == "__main__":
    main()
