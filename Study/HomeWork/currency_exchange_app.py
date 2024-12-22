import sqlite3


# Класс пользователя
class User:
    def __init__(self, rub: int, usd: int, eur: int) -> None:
        self.rub = rub
        self.usd = usd
        self.eur = eur


# Класс для взаимодействия с БД
class DBManager:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name  # Указываем имя БД для подключения

    # Подключаемся к БД
    def connect(self):
        return sqlite3.connect(self.db_name)

    # Создание пользователя
    def create_user(self, user: User) -> bool:
        # Подключаемся к БД для создания пользователя
        with self.connect() as db:
            cur = db.cursor()

            # Параметры для запроса получаем из объекта User переданного в аргументы метода
            data_user = (user.rub, user.usd, user.eur)

            cur.execute("""
                        INSERT INTO users_balance(Balance_RUB, Balance_USD, Balance_EUR)
                        VALUES (?, ?, ?);
                        """, data_user)

            db.commit()
            print("Пользователь успешно добавлен.")
            return True

    def exchange(self, target_currency: str, new_amount: float, source_currency: str, amount: float) -> str:
        # Подключаемся к БД
        with self.connect() as db:
            cur = db.cursor()

            # Запрашиваем данные пользователя
            cur.execute("""
                        SELECT *
                        FROM users_balance
                        WHERE UserID = 1;
                        """)

            user_data = list(cur.fetchone())  # получаем данные пользователя в список
            user_data[int(source_currency)] -= new_amount  # изменяем количество исходной валюты
            user_data[int(target_currency)] += amount  # изменяем количество новой валюты

            # При отсутствии нужной суммы, радуем пользователя
            if user_data[int(source_currency)] < 0:
                return 'Недостаточно средств в выбранной валюте.'

            # Загоняем обновленные данные в кортеж для использования параметризированного запроса
            update_params = (user_data[1], user_data[2], user_data[3], 1)

            cur.execute("""
                        UPDATE users_balance SET Balance_RUB = ?, Balance_USD = ?, Balance_EUR = ?
                        WHERE UserID = ?; 
                        """, update_params)

            # Фиксируем изменения
            db.commit()

            return (f'Обмен успешно произведен.\n\n'
                    f'Ваш баланс:\n'
                    f'{user_data[1]:.1f} RUB\n'
                    f'{user_data[2]:.1f} USD\n'
                    f'{user_data[3]:.1f} EUR')


# Класс приложения
class Application:
    # Словарь, содержащий обменный курс
    EXCHANGE_RATE = {
        '2/1': 70.0,  # 1 USD = 70 RUB
        '2/3': 0.87,  # 1 USD = 0.87 EUR
        '3/1': 80.0,  # 1 EUR = 80 RUB
        '3/2': 1.15,  # 1 EUR = 1.15 USD
        '1/2': 1 / 70,  # 1 RUB = 1 / 70 USD
        '1/3': 1 / 80  # 1 RUB = 1 / 80 EUR
    }

    # Добавляем менеджера для работы с БД
    def __init__(self, db_manager: DBManager):
        self.db = db_manager

    @staticmethod
    def welcome():
        print('Добро пожаловать в наш обменный пункт, курс валют следующий:\n'
              '1 USD = 70 RUB\n'
              '1 EUR = 80 RUB\n'
              '1 USD = 0,87 EUR\n'
              '1 EUR = 1,15 USD\n')

        print('Введите какую валюту желаете получить:\n'
              '1. RUB\n'
              '2. USD\n'
              '3. EUR\n')

        print("Или введите 'x' для выхода.")

    @staticmethod
    def goodbye():
        print("Завершение работы. Всего доброго!")

    # Точка входа в приложение.
    # Выбираем желаемую валюту
    def start(self) -> None:
        self.welcome()

        while True:
            user_input = input()

            if user_input in ('1', '2', '3'):
                return self.step2(user_input)

            if user_input == 'x':
                return self.goodbye()

            print("Некорректный ввод.\n"
                  "Повторите попытку:")

    # Проверяем корректность введенной суммы
    @staticmethod
    def get_valid_amount() -> float:
        while True:
            user_input = input()

            if user_input.isdigit() and float(user_input) > 0:
                return float(user_input)

            print("Введите корректную сумму в виде целого положительного числа:")

    # Шаг 2 (после точки входа). Вводим желаемую сумму новой валюты
    def step2(self, target_currency: str) -> None:
        print("Какая сумма Вас интересует?")

        self.step3(target_currency, self.get_valid_amount())

    # Проверяем корректность выбора желаемой валюты
    @staticmethod
    def correct_input(target_currency: str) -> str:
        while True:
            user_input = input()

            if user_input in ('1', '2', '3') and user_input != target_currency:
                return user_input

            print("Некорректный ввод.\n"
                  "Повторите попытку:")

    # Выбираем исходную валюту
    def step3(self, target_currency: str, amount: float) -> None:
        print('Какую валюту готовы предложить взамен?:\n'
              '1. RUB\n'
              '2. USD\n'
              '3. EUR\n')

        self.step4(target_currency, amount, self.correct_input(target_currency))

    def step4(self, target_currency: str, amount: float, source_currency: str) -> None:
        # Формируем валютную пару (ключ), для запроса данных из словаря
        currency_pair = ''.join([target_currency, '/', source_currency])

        # Считаем сумму новой валюты
        new_amount = Application.EXCHANGE_RATE[currency_pair] * amount

        # Передаем запрос в класс менеджера БД и выводим ответ
        print(self.db.exchange(target_currency, new_amount, source_currency, amount))


class Main:
    # Имя БД
    db_name = 'exchanger.db'

    # Подключение к БД с помощью вспомогательного класса
    db_manager = DBManager(db_name)

    # Добавление пользователя с помощью класса для работы с БД
    # user = User(100000, 1000, 1000)
    # db_manager.create_user(user)

    # Запуск приложения с передачей менеджера по работе с БД в аргументах
    Application(db_manager).start()
