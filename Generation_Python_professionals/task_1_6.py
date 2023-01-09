def almost_double_factorial(n: int) -> int:
    mul = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            mul *= i
    return mul


if __name__ == '__main__':
    print(almost_double_factorial(10))
    print(almost_double_factorial(50))
    print(almost_double_factorial(100))
    print(almost_double_factorial(0))
