# main.py

from aiogram import executor
from aiogram.dispatcher import Dispatcher
from config import dp
from handlers.start import register_handlers

if __name__ == "__main__":
    register_handlers(dp=dp)
    executor.start_polling(dp, skip_updates=True)
