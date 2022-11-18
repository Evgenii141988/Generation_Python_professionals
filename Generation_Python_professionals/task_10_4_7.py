class BoundedRepeater:
    def __init__(self, obj: object, times: int):
        self.obj = obj
        self.times = times
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.times:
            raise StopIteration
        self.counter += 1
        return self.obj


if __name__ == '__main__':
    bee = BoundedRepeater('bee', 2)

    print(next(bee))
    print(next(bee))

    geek = BoundedRepeater('geek', 3)

    print(next(geek))
    print(next(geek))
    print(next(geek))

    try:
        print(next(geek))
    except StopIteration:
        print('Error')
