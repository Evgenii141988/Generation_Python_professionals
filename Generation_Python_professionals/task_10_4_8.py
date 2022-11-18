class Square:
    def __init__(self, n: int):
        self.number = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration
        self.counter += 1
        return self.counter ** 2


if __name__ == '__main__':
    squares = Square(2)

    print(next(squares))
    print(next(squares))

    squares = Square(10)

    print(list(squares))

    squares = Square(1)

    print(list(squares))
