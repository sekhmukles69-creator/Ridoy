import telebot
from openai import OpenAI

# Initialize
bot = telebot.TeleBot('8863800334:AAEv_k_3v8Ka12YnCgLMLpHog1MqaTdNMAA')
client = OpenAI(api_key='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')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.text}]
    )
    bot.reply_to(message, response.choices[0].message.content)

bot.infinity_polling()
