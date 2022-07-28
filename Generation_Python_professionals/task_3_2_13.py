from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        d = date(year, month, day)
        return True
    except:
        return False


if __name__ == '__main__':
    print(is_correct(31, 12, 2021))
    print(is_correct(31, 13, 2021))
    print(is_correct(32, 10, 2021))