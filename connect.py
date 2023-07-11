import mysql.connector

# Установка соединения с базой данных
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Функция для добавления товара в базу данных
def add_product():
    # Получение данных от пользователя
    name = input("Введите наименование товара: ")
    quantity = int(input("Введите количество товара: "))

    # Выполнение SQL-запроса для добавления товара
    cursor = connection.cursor()
    query = "INSERT INTO Товары (Наименование, Количество, Доступность) VALUES (%s, %s, true)"
    values = (name, quantity)
    cursor.execute(query, values)
    connection.commit()

    print("Товар успешно добавлен!")

# Вызов функции для добавления товара
add_product()

# Закрытие соединения с базой данных
connection.close()
