import sys

if __name__ == '__main__':
    numbers = [int(line.strip()) for line in sys.stdin]
    n = len(numbers)
    d = numbers[1] - numbers[0]
    q = numbers[1] / numbers[0]
    a1 = numbers[0]
    an = numbers[-1]
    if a1 + (n - 1) * d == an and all((numbers[i + 1] - numbers[i] == d for i in range(n - 1))):
        print('Арифметическая прогрессия')
    elif a1 * q ** (n - 1) == an and all((numbers[i + 1] / numbers[i] == q for i in range(n - 1))):
        print('Геометрическая прогрессия')
    else:
        print('Не прогрессия')
