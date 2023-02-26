from typing import Generator


def gen_fibonacci_numbers(n: int) -> Generator[int, int, None]:
    num1 = 0
    num2 = 1
    for _ in range(n):
        num1 += num2
        yield num2
        num1, num2 = num2, num1


if __name__ == '__main__':
    for i in gen_fibonacci_numbers(10):
        print(i)
