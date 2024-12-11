from idlelib.pyparse import trans
from pprint import pprint
from timeit import default_number
from typing import TypeIs

from numpy.f2py.auxfuncs import throw_error, replace


def valid_mail(mail):
    mail_ = mail.lower().strip()

    if '@' not in mail_ or '.ru' not in mail_:
        return 'Bad'

    parts = mail_.split('@')

    if parts[1].endswith('.ru'):
        return 'Good'
    return 'Bad'


def new_function_1(number):
    if number < 0:
        return -number

    return number


def str_to_float(x):
    f = x
    try:
        f = float(x)
    except Exception as e:
        print(f"Так делать нельзя, потому что {e}")

    return f


def new_function_2(number):
    if number == 2:
        return 'Два'

    if number == 5:
        return 'Пять'

    return 'Bad'


def new_function_3(number, x=7):
    if number % x == 0:
        return 'Good'

    return 'Bad'


def logic_1(number):
    if number % 2 == 0:
        return even()

    return odd()


def even_1():
    return 'ЧЕТ'


def odd_1():
    return 'НЕЧЕТ'


def new_function_4(string):
    return string.split()[1]


def new_function_5(string):
    fio = string.split()

    return fio[0] + ' ' + fio[1][0] + '.' + fio[2][0] + '.'


def new_function_6(name, year):
    return f'Меня зовут {name}, мне {2024 - year}.'


def logic_11(name, country):
    if country == 'Россия':
        return russia(name)

    return england(name)


def russia_11(name):
    with open('russia.txt', 'w') as file:
        file.write(name)

    with open('russia.txt', 'r') as file:
        return file.read()


def england_11(name):
    with open('england.txt', 'w') as file:
        file.write(name)

    with open('england.txt', 'r') as file:
        return file.read()


# 2.27 Список расходов
def new_function_7(day, balance):
    if balance < 30 or not (0 < day < 4):
        return 'Bad'

    recording('file.txt', day, balance)

    return expenses('file.txt')


def recording(path, day, bal):
    with open(path, 'w') as file:
        for i in range(1, day + 1):
            file.write(f'{i} день - баланс {bal} -'
                       f' списалось 7 - осталось {bal - 7}\n')
            bal -= 7


def expenses(path):
    with open(path, 'r') as file:
        return file.read()


def new_function_8(balance, summ):
    if summ <= balance:
        return balance - summ

    return 'Не хватает денежных средств'


def new_function(food, tea):
    if tea > food:
        return 'Bad'

    return food * 3000 + tea * 500


#Calculator
def calc():
    try:
        num_1 = valid_input()
        action = input("Введите оператор:\n")
        num_2 = valid_input()
    except ValueError:
        return 'Введенное вами число не является корректным.'

    if action == '+':
        return num_1 + num_2

    if action == '-':
        return num_1 - num_2

    if action == '*':
        return num_1 * num_2

    if action == '/':
        try:
            return num_1 / num_2
        except ZeroDivisionError:
            return 'На ноль делить нельзя.'

    return 'Введен неизвестный оператор.'


def valid_input():
    return int(input("Введите число:\n"))


def button(string):
    button_index = string.find('кнопку') + 7
    string_1 = string[:button_index]

    space_index = string.find(' ', button_index + 1)
    button_name = f'"{string[button_index:space_index]}"'

    string_2 = string[space_index:]

    return string_1 + button_name + string_2


def clear_path(path):
    if '/' in path:
        return path[path.rfind('/') + 1:path.find('.')]

    return path[path.rfind('\\') + 1:path.find('.')]


def correct_phone_(number: str) -> str:
    num_list = list(number[-10:])

    num_list.insert(-4, '-')
    num_list.insert(-2, '-')
    num_list.insert(3, ') ')
    num_list.insert(0, '+7 (')

    return ''.join(num_list)


def correct_phone(number: str) -> str:
    number = number[-10:]

    return f'+7 ({number[:3]}) {number[3:6]}-{number[6:8]}-{number[8:]}'


def date_correct(date: str) -> str:
    date_list = date.split('.')

    for i in range(2):
        num = date_list[i]

        if len(num) == 1:
            date_list[i] = '0' + num

    return ".".join(date_list)


def movie_info():
    movie_info = {'Название': 'Гладиатор',
                  'Год выпуска': 2000,
                  'Продолжительность': 155,
                  'Жанр': 'Историческая драма',
                  'Режиссер': 'Ридли Скотт',
                  'В главных ролях': 'Рассел Кроу',
                  'Статус фильма': 'ЛЕГЕНДА'}

    for key, value in movie_info.items():
        print(f'{key} - {value}')


def str_in_dict() -> None:
    movie_info = "Название 'Армагеддон', Год выпуска '1998', Продолжительность '144', Жанр 'Фантастика', Режиссер 'Майкл Бэй', В главных ролях 'Брюс Уиллис', Статус фильма 'Брюса жалко'"
    movie_list = movie_info.split(', ')
    movie_dict = {}

    for string in movie_list:
        find = string.find(" '")

        key = string[:find]
        value = string[find + 2:-1]

        movie_dict[key] = value

    for key, value in movie_dict.items():
        print(f'{key} : {value}')


def validator(login: str, password: str) -> str:
    person_data = {'Login': 'User1',
                   'Password': 'Qwer_1234'}

    if values[0] == login and values[1] == password:
        return "Good"

    return "Bad"


def del_null_val_dict() -> None:
    data = {'a': 1, 'b': 0, 'c': 3, 'd': 0}
    new_data = dict()

    for key, value in data.items():
        if value != 0:
            new_data[key] = value

    for key, value in new_data.items():
        print(f'{key} - {value}')


def max_value_in_dict(my_dict: dict) -> str:
    max_value = 0
    max_key = ''

    for key, value in my_dict.items():

        if value > max_value:
            max_value = value;
            max_key = key

    return f'{max_key} - {max_value}'


def dict_from_lists(keys: list, values: list) -> str:
    new_dict = dict(zip(keys, values))

    return '\n'.join(f'{key} - {value}' for key, value in new_dict.items())


def is_key_in_dict(my_dict: dict, key: str) -> str:
    if key in my_dict:
        return "Good"

    return "Bad"


def del_key_in_dic(my_dict: dict, key: str) -> str:
    if key in my_dict.keys():
        del (my_dict[key])

    return '\n'.join(f'{key} - {value}' for key, value in my_dict.items())


def dict_from_list(new_list: list) -> str:
    my_dict = dict()
    new_list.sort()

    for i in new_list:
        if i in my_dict.keys():
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    return '\n'.join(f'{key} - {value}' for key, value in my_dict.items())


def is_correct_letter(address: str, subject: str, text: str) -> str:
    mail_data = {'address': 'test@test.ru',
                 'subject': 'Спец.письмо',
                 'text': 'Царский указ'}

    if mail_data['address'] != address or mail_data['subject'] != subject:
        return 'Bad'

    if mail_data['text'] == text or text == '':
        return 'Good'


# address = input()
# subject = input()
# try:
#     text = input()
# except EOFError:
#     text = ''
#
# print(is_correct_letter(input(), input(), input()))

def generate_dict_from_n(n: int) -> str:
    new_dict = dict()

    for i in range(1, n + 1):
        new_dict[i] = i ** 2

    return '\n'.join(f'{key} - {value}' for key, value in new_dict.items())


def replace_str(string: str) -> str:
    return string.replace('.', '..')


def a_counter(string: str) -> int:
    return string.lower().count('а')


def sharp_replacer(string: str) -> str:
    new_string = ''

    for i, char in enumerate(string):
        if char == '#':
            new_string += str(i + 1)
        else:
            new_string += string[i]

    return new_string


def discounter(price: int) -> str:
    if price < 10_000:
        return f'{price}\n0'

    new_price = int(price * 0.7)
    discount = int(price * 0.3)

    return f'{new_price}\n{discount}'


def money_changer(money: int) -> str:
    if money % 5 != 0:
        return "Bad"

    one_hundred = 0
    ten = 0
    five = 0

    one_hundred = money // 100
    money %= 100

    ten = money // 10
    money %= 10

    if (money == 5):
        five = 1

    return '\n'.join(f'{value} - {count}' for value, count in [(100, one_hundred), (10, ten), (5, five)] if count > 0)


def time_in_twelve(time: str) -> str:
    hh, mm = map(int, time.split(':'))
    tf = 'pm'

    if hh < 13:
        tf = 'am'

    return f'{tf} - {hh % 12}:{mm:02}'


def time_plus_min(time: str, minute: str) -> str:
    hh, mm = map(int, time.split(':'))

    min = int(minute)
    mm += min

    if mm > 59:
        hh += mm // 60
        mm %= 60

    if hh > 23:
        hh %= 24

    return f'{hh:02}:{mm:02}'


def sum_all_in_list(new_list: list) -> int:
    return sum(map(int, new_list))


def find_char_in_string(str_1: str, str_2: str) -> str:
    for i in str_1:
        if i in str_2:
            return "Good"

    return "Bad"


print(find_char_in_string(input(), input()))
