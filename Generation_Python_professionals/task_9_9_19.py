from functools import lru_cache


@lru_cache()
def add_one(number):
    print(number + 1, end=' ')


if __name__ == '__main__':

    numbers = [1, 2, 3, 1, 3, 4, 4, 1]

    for i in numbers:
        add_one(i)
