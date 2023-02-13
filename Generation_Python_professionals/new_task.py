def calculate(x: float, y: float, operation: str = 'a') -> None:
    def addition(a: float, b: float) -> None:
        print(a + b)

    def subtraction(a: float, b: float) -> None:
        print(a - b)

    def division(a: float, b: float) -> None:
        if b == 0:
            print('На ноль делить нельзя!')
            return
        print(a / b)

    def multiplication(a: float, b: float) -> None:
        print(a * b)

    match operation:
        case 'a':
            addition(x, y)
        case 's':
            subtraction(x, y)
        case 'd':
            division(x, y)
        case 'm':
            multiplication(x, y)
        case _:
            print('Ошибка. Данной операции не существует')


if __name__ == '__main__':
    calculate(2, 5)  # Печатает 7.0
    calculate(2.2, 15, 'a')  # Печатает 17.2
    calculate(22, 15, 's')  # Печатает 7.0
    calculate(2, 3.2, 'm')  # Печатает 6.4
    calculate(10, 0.4, 'd')  # Печатает 25.0
    calculate(10, 0.4, 'ff')
    calculate(10, 0, 'd')