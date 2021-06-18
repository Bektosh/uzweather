import requests
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from telegram.update import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters
from settings.settings import TELEGRAM_TOKEN, owm_TOKEN
owm = OWM(owm_TOKEN)
mgr = owm.weather_manager()

updater = Updater(token=TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Assalomu alaykum')
    context.bot.sendMessage(chat_id=update.message.chat_id,\
                            text='Shaxaringiz nomini kiting. Masalan: Tashkent')

def weather(update: Update, context: CallbackContext):
    observation = mgr.weather_at_place(update.message.text)
    w = observation.weather

    wind = w.wind()['speed']
    humidity = w.humidity
    temperature = w.temperature('celsius')['temp']
    clouds = w.clouds

    update.message.reply_text(f'Shamol tezligi 💨:  {wind}\n'
                              f'Namgarchilik 💧: {humidity}\n'
                              f'Gradus 🌡: {temperature}\n'
                              f'Bulut ☁️: {clouds}\n'
    )





dispacher = updater.dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, weather))

updater.start_polling()
updater.idle()
