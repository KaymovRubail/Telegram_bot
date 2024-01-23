from aiogram import types
from aiogram.dispatcher import Dispatcher
from config import dp
from db_module import insert_user

async def handle_start_command(message: types.Message):
    user_data = (
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name
    )

    insert_user(user_data)

    await message.reply("Привет! Ты нажал /start")
# handlers/start.py

from aiogram import types
from aiogram.dispatcher import Dispatcher

async def start_command_handler(message: types.Message):
    await message.answer("Привет! Это ваше приветственное сообщение.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command_handler, commands=['start'])
