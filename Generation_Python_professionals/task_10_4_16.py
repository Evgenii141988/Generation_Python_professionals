class Xrange:
    def __init__(self, start: int | float, end: int | float, step: int | float = 1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        result = self.start
        if (self.start >= self.end and self.step > 0) or (self.start <= self.end and self.step < 0):
            raise StopIteration
        self.start += self.step
        return result


if __name__ == '__main__':
    evens = Xrange(0, 10, 2)

    print(*evens)

    xrange = Xrange(0, 3, 0.5)

    print(*xrange, sep='; ')

    xrange = Xrange(10, 1, -1)

    print(*xrange)

    xrange = Xrange(5, 10)

    print(*xrange)