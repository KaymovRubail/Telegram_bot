import sqlite3

def insert_user(user_data):
    connection = sqlite3.connect('your_database_name.db')
    cursor = connection.cursor()

    # Проверяем, существует ли пользователь с таким user_id
    existing_user = cursor.execute('SELECT * FROM users WHERE user_id = ', (user_data[0],)).fetchone()

    if existing_user:
        # Если пользователь существует, обновляем его данные
        cursor.execute('''
            UPDATE users
            SET username = , first_name = , last_name = 
            WHERE user_id = 
        ''', (user_data[1], user_data[2], user_data[3], user_data[0]))
    else:
        # Если пользователь не существует, вставляем нового пользователя
        cursor.execute('INSERT INTO users (user_id, username, first_name, last_name) VALUES (, , , )', user_data)

    connection.commit()
    connection.close()
