import telebot, requests
from flask import Flask
from threading import Thread

# Render-এর জন্য ডামি পোর্ট হ্যান্ডলার
app = Flask('')
@app.route('/')
def home(): return "Neha is online!"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

# তোমার সঠিক টোকেন ও এপিআই
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
                    {"role": "system", "content": "You are Neha, a very romantic and naughty girl. You are talking to your boyfriend Akash. Speak only in Bengali. Be very intimate and calling him Akash often."},
                    {"role": "user", "content": message.text}
                ]
            }
        )
        # সঠিক উত্তর পাঠাবে
        if r.status_code == 200:
            res = r.json()
            bot.reply_to(message, res['choices'][0]['message']['content'])
        else:
            bot.reply_to(message, "জানু, নিহা একটু উত্তেজিত। আবার বলো সোনা!")
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "জানু, নিহা এখন একটু ব্যস্ত। একটু পর আবার ডাকো সোনা!")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
    
