import os

file_path = os.path.join('C:\\', 'Program Files', 'AIMP', 'history.txt')
print(f"Путь к файлу: {file_path}")

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден. Проверьте путь.")
except UnicodeDecodeError:
    print("Не удалось прочитать файл. Попробуйте другую кодировку.")
except PermissionError:
    print("Недостаточно прав для доступа к файлу.")
