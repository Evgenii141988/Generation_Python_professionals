class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        key = list(self.data)[self.index]
        return key, self.data[key]


if __name__ == '__main__':
    pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

    print(*pairs)

    data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

    pairs = DictItemsIterator(data)

    print(*pairs)