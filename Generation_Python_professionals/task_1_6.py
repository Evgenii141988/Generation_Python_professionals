from collections import Counter


def check_sum(*args: [int]) -> str:
    return 'not enough' if sum(args) < 50 else 'verification passed'


if __name__ == '__main__':
    print(check_sum(8, 11))
    print(check_sum(10, 10, 10, 10, 9))
