from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from decouple import config

TOKEN = config("6815811179:AAFKbcyFoNsAyydxU8Pxg5NeB39Gb3x8eOs")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
