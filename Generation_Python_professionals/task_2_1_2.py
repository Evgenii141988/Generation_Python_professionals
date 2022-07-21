def same_parity(numbers: list) -> list:
    try:
        return list(filter((lambda x: x % 2 == 0) if numbers[0] % 2 == 0 else (lambda x: x % 2 != 0), numbers))
    except IndexError:
        return []

if __name__ == '__main__':
    print(same_parity([]))
    print(same_parity([6, 0, 67, -7, 10, -20]))
    print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
