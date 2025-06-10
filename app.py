import requests
import time
import os

# Konfiguration (fest codiert)
API_KEY = "MZBPMPUQ8E097P2R"
BOT_TOKEN = "7745598671:AAEUi_SDwtCpYuVzaBL7EJ10huMNYas120"
CHAT_ID = "2011080524"

def get_gold_price():
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=XAU&to_currency=USD&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    try:
        price = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        return price
    except:
        return None

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(telegram_url, data=payload)

if __name__ == "__main__":
    last_price = 0
    while True:
        price = get_gold_price()
        if price:
            if price != last_price:
                send_telegram_message(f"📈 Aktueller Goldpreis: {price:.2f} USD")
                last_price = price
        time.sleep(60)  # alle 60 Sekunden prüfen
