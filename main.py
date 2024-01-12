from aiogram import executor
from aiogram.dispatcher import Dispatcher
from config import dp
from handlers import start, survey
from db_module import create_table  # Добавьте импорт

if __name__ == "__main__":
    create_table()  # Вызовите функцию create_table перед запуском бота
    start.register_handlers(dp=dp)
    survey.register_handlers(dp=dp)
    executor.start_polling(dp, skip_updates=True)
