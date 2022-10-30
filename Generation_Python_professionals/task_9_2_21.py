if __name__ == '__main__':
    formula = input()
    a, b = [int(n) for n in input().split()]
    max_value = max(eval(formula) for x in range(a, b + 1))
    min_value = min([eval(formula) for x in range(a, b + 1)])
    print(f'Минимальное значение функции {formula} на отрезке [{a}; {b}] равно {min_value}')
    print(f'Максимальное значение функции {formula} на отрезке [{a}; {b}] равно {max_value}')