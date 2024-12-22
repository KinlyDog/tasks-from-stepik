import sqlite3
import re


class DBSetup:
    def __init__(self, db_name: str, table_name: str,
                 field_0: str, field_1: str, field_2: str, field_3: str):
        self.db_name = db_name
        self.table_name = table_name
        self.field_0 = field_0
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

        print("База данных создана успешно")

    # Проверка, что имя поля состоит из букв, цифр или нижнего подчеркивания и начинается с буквы
    def validate_field_name(self, field_name: str) -> bool:
        return bool(re.match(r"^[A-Za-z_]\w*$", field_name))

    def create_table(self):
        # Проверка всех полей на безопасность
        if not all(map(self.validate_field_name, [self.field_0, self.field_1, self.field_2, self.field_3, ])):
            raise ValueError("Одно или несколько полей имеют недопустимые символы или некорректны")

        # Используем контекстный менеджер для автоматического закрытия соединения
        with sqlite3.connect(self.db_name) as db:
            cur = db.cursor()

            cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                            {self.field_0} INTEGER PRIMARY KEY,
                            {self.field_1} TEXT NOT NULL,
                            {self.field_2} TEXT NOT NULL,
                            {self.field_3} TEXT NOT NULL
                        );''')

            db.commit()
            print("Таблица создана успешно")
