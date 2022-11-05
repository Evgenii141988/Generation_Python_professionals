def power(degree: int):
    def inner(x):
        return x ** degree

    return inner


if __name__ == '__main__':
    square = power(2)
    print(square(5))
