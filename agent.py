import requests
from datetime import datetime

BOT_TOKEN = "8574299465:AAFjJHLh4rCBE-rTKSISHq1iqW4cMnNxaHw"
CHAT_ID = "-5079341429"
NEWS_API_KEY = "9ea8cdac0aa042cabf3132a727ff110f"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=12.37&longitude=-1.52&current_weather=true"
    r = requests.get(url).json()
    return f"🌤️ Météo : {r['current_weather']['temperature']}°C"

def get_news():
    url = f"https://newsapi.org/v2/everything?q=actualité&language=fr&pageSize=3&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    r = requests.get(url).json()

    if "articles" not in r or len(r["articles"]) == 0:
        return "📰 Pas d’actualités disponibles pour le moment."

    news_text = "📰 Actualités du jour :\n\n"
    for i, a in enumerate(r["articles"], 1):
        title = a["title"]
        source = a["source"]["name"]
        desc = a["description"] or "Pas de résumé disponible."
        link = a["url"]

        news_text += f"{i}. 🗞️ {title}\n📍 {source}\n📝 {desc}\n🔗 {link}\n\n"

    return news_text

def main():
    now = datetime.now().strftime("%H:%M")
    message = f"☀️ Bonjour !\n🕒 {now}\n{get_weather()}\n\n{get_news()}\nBonne journée 💪"
    send_message(message)

main()
