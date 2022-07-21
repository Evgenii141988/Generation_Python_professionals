def is_valid(string: str) -> bool:
   return 4 <= len(string) <= 6 and all((s.isdigit() for s in string))


if __name__ == '__main__':
    print(is_valid('4367'))
    print(is_valid('92134'))
    print(is_valid('89abc1'))
    print(is_valid('900876'))
    print(is_valid('49 83'))