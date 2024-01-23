from aiogram import types
from aiogram.dispatcher import Dispatcher
from config import dp

async def start_survey(message: types.Message):
    question = "Какая ваша любимая тема?"
    options = ["Наука", "Технологии", "Искусство"]

    keyboard = types.InlineKeyboardMarkup()
    for option in options:
        callback_data = f"survey_{option}"
        keyboard.add(types.InlineKeyboardButton(option, callback_data=callback_data))

    await message.reply(text=question, reply_markup=keyboard)

async def handle_survey_response(callback_query: types.CallbackQuery):
    selected_option = callback_query.data.split("_")[1]
    user_id = callback_query.from_user.id


    await callback_query.answer(f"Вы выбрали: {selected_option}")
