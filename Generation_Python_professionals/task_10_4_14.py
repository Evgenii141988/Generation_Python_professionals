from random import randint


class RandomNumbers:
    def __init__(self, left: int, right: int, n: int):
        self.left = left
        self.right = right
        self.n = n
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= self.n:
            raise StopIteration
        return randint(self.left, self.right)


if __name__ == '__main__':
    iterator = RandomNumbers(1, 1, 3)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    iterator = RandomNumbers(1, 10, 2)

    print(next(iterator) in range(1, 11))
    print(next(iterator) in range(1, 11))
