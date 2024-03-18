import telebot
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = telebot.TeleBot('7074598864:AAEPefl4FCMY3f4oTsYPGOnZF_d2oBncYc8')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть', web_app=WebAppInfo(url='https://github.com/')))
executor.start_polling(dp)