def sum_num(string: str) -> int:
    print(sum((int(s) for s in string if s.isdigit())))


if __name__ == '__main__':
    sum_num(input())
