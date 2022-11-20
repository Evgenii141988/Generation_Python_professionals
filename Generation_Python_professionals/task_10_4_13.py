class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)


if __name__ == '__main__':
    cycle = Cycle('be')

    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))

    cycle = Cycle([1])

    print(next(cycle) + next(cycle) + next(cycle))

    cycle = Cycle(range(100_000_000))

    print(next(cycle))
    print(next(cycle))