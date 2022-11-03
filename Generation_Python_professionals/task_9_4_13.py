def polynom(x: float):
    if not polynom.__dict__:
        polynom.values = set()
    polynom.values.add(x ** 2 + 1)
    return x ** 2 + 1


if __name__ == '__main__':
    for _ in range(10):
        polynom(10)

    print(polynom.values)