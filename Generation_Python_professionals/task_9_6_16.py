def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step > 0:
        for _ in range(step):
            numbers.insert(0, numbers.pop())
    if step < 0:
        for _ in range(abs(step)):
            numbers.append(numbers.pop(0))


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    cyclic_shift(numbers, 3)

    print(numbers)

    numbers = [1, 2, 3, 4, 5]
    cyclic_shift(numbers, -2)

    print(numbers)
