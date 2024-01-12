from aiogram import types, Dispatcher
from config import bot
from db_module import insert_survey_response

async def start_survey(message: types.Message):
    question = "Какая ваша любимая тема?"
    options = ["Наука", "Технологии", "Искусство"]

    keyboard = types.InlineKeyboardMarkup()
    for option in options:
        callback_data = f"survey_{option}"
        keyboard.add(types.InlineKeyboardButton(option, callback_data=callback_data))

    await bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

def handle_survey_response(callback_query: types.CallbackQuery):
    selected_option = callback_query.data.split("_")[1]
    user_id = callback_query.from_user.id

    # Здесь можно обработать ответ пользователя и записать его в базу данных
    insert_survey_response(user_id, selected_option)

    await callback_query.answer(f"Вы выбрали: {selected_option}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_survey, commands=['survey'])
    dp.register_callback_query_handler(handle_survey_response, lambda c: c.data.startswith('survey'))
