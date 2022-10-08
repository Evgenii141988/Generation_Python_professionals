import json


if __name__ == '__main__':
    filename = input()
    try:
        with open(filename) as file:
            try:
                data = json.load(file)
                print(data)
            except json.JSONDecodeError:
                print('Ошибка при десериализации')
    except FileNotFoundError:
        print('Файл не найден')
