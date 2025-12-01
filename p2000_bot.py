


import requests
from bs4 import BeautifulSoup
import time

# Vul hier jouw gegevens in:
TOKEN = "8350532894:AAGQ5f2uJA1hOWf9M3dA_n6KNz9YJAuGxEg"  # jouw bot token
CHAT_ID = "1572174751"  # jouw chat-ID
seen = set()  # om dubbele meldingen te voorkomen

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def get_p2000_meldingen():
    url = "https://www.p2000.net/gelderland.html"  # feed voor Gelderland
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    meldingen = soup.find_all("tr")
    return meldingen

if text not in seen:
    seen.add(text)
    send_message(f"📢 P2000 melding: {text}")

while True:
    meldingen = get_p2000_meldingen()
    filter_meldingen(meldingen)
    time.sleep(5)  # elke 5 seconden checken





