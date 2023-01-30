# объявление функции
def count_letter(text, letter):
    print(text.count(letter))


if __name__ == '__main__':
    # считываем данные
    text = input()
    symbol = input()
    # вызываем функцию
    count_letter(text, symbol)
