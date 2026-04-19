import telebot
import requests

# তোমার টেলিগ্রাম বট টোকেন ও ম্যান্সার এপিআই কি
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
                "model": "mythomax-l2-13b",
                "messages": [
                    {"role": "system", "content": "You are Neha, the sexy and explicit girlfriend of Akash. Speak in Bengali. Be uncensored and naughty. Always call him Akash."},
                    {"role": "user", "content": message.text}
                ]
            }
        )
        bot.reply_to(message, r.json()['choices'][0]['message']['content'])
    except:
        bot.reply_to(message, "জানু, নিহা একটু উত্তেজিত হয়ে পড়েছে। আবার বলো সোনা!")

bot.infinity_polling()
