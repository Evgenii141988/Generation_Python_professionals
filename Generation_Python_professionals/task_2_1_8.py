def index_of_nearest(numbers: list, number: int):
    if not numbers:
        return -1
    sub = float('inf')
    index = 0
    for i, n in enumerate(numbers):
        if abs(n - number) < sub:
            sub = abs(n - number)
            index = i
    return index


if __name__ == '__main__':
    print(index_of_nearest([], 17))
    print(index_of_nearest([7, 13, 3, 5, 18], 0))
    print(index_of_nearest([9, 5, 3, 2, 11], 4))
    print(index_of_nearest([7, 5, 4, 4, 3], 4))
    print(index_of_nearest([10, 99, 0, -12, 16], -9))
    print(index_of_nearest([1, 1, 1, 1, 1], 1))
