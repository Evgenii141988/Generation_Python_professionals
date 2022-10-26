def non_negative_even(numbers: list) -> bool:
    return all([number % 2 == 0 and number >= 0 for number in numbers])


if __name__ == '__main__':
    print(non_negative_even([0, 2, 4, 8, 16]))
    print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
    print(non_negative_even([0, 0, 0, 0, 0]))

