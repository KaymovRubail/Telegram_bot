from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from decouple import config

TOKEN = config("TOKEN")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
