# Класс для работы с картой
class Card:
    def __init__(self, user_id: int, number: int, pin: int, balance: int) -> None:
        # Поля класса скрыты от посторонних, для исключения прямого вмешательства
        self.__user_id = user_id
        self.__number = number
        self.__pin = pin
        self.__balance = balance

    # Геттеры, возвращающие значения полей класса
    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def number(self) -> int:
        return self.__number

    @property
    def pin(self) -> int:
        return self.__pin

    @property
    def balance(self) -> int:
        return self.__balance

    # Метод для создания нового объекта с изменённым полем balance
    def with_balance(self, new_balance: int):
        if new_balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        return Card(self.__user_id, self.__number, self.__pin, new_balance)