from functools import lru_cache


@lru_cache()
def ways(n: int):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)


if __name__ == '__main__':
    print(ways(5))
    print(ways(1))
    print(ways(2))