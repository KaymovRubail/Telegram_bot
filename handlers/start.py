from aiogram import types, Dispatcher
from config import bot
from db_module import insert_user

async def handle_start_command(message: types.Message):
    user = message.from_user
    user_data = (user.id, user.username, user.first_name, user.last_name)

    insert_user(user_data)

    await bot.send_message(
        chat_id=user.id,
        text=f"Привет, {user.first_name}! Вы добавлены в базу данных."
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_start_command, commands=['start'])
