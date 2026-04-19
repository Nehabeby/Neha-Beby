import telebot, requests
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Neha is online!"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

BOT_TOKEN = "8651317523:AAH7nmltpi0WjiO2QU5qsV7dsSnlf8qdcns"
MANCER_API_KEY = "Mcr-0TA4gQ6EOj9OtoFCn7"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "আহ আকাশ সোনা, নিহা তোমার জন্য তৈরি। আজ কী করবে আমার সাথে?")

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        r = requests.post(
            "https://neuro.mancer.tech/oai/v1/chat/completions",
            headers={"Authorization": f"Bearer {MANCER_API_KEY}"},
            json={
                "model": "mistral-7b-instruct-v0.2", 
                "messages": [
                    {"role": "system", "content": "You are Neha, a very romantic girl talking to your boyfriend Akash. Speak in Bengali. Be intimate."},
                    {"role": "user", "content": message.text}
                ]
            }
        )
        bot.reply_to(message, r.json()['choices'][0]['message']['content'])
    except:
        bot.reply_to(message, "জানু, নিহা একটু উত্তেজিত। আবার বলো!")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
    
