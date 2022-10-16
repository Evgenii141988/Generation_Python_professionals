def range_sum(numbers: list, start: int, end: int) -> int:
    if start == end:
        return numbers[end]
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)


if __name__ == '__main__':
    print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
    print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
    print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
