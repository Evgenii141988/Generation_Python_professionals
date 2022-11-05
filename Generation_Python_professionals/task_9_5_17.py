def generator_square_polynom(a: float, b: float, c: float):
    def inner(x: float):
        return a * x ** 2 + b * x + c

    return inner


if __name__ == '__main__':
    f = generator_square_polynom(1, 2, 1)
    print(f(5))