# db_module.py

import sqlite3

def create_table():
    connection = sqlite3.connect('your_database_name.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT
        )
    ''')

    connection.commit()
    connection.close()

def insert_user(user_data):
    connection = sqlite3.connect('your_database_name.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO users (user_id, username, first_name, last_name) VALUES (?, ?, ?, ?)', user_data)

    connection.commit()
    connection.close()

def record_survey_response(user_id, selected_option):
    connection = sqlite3.connect('your_database_name.db')
    cursor = connection.cursor()

    # Здесь реализуйте логику записи ответа на опрос в базу данных
    # cursor.execute('INSERT INTO survey_responses (user_id, selected_option) VALUES (?, ?)', (user_id, selected_option))

    connection.commit()
    connection.close()
