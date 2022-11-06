def get_digits(number: int | float) -> list[int]:
    return [int(i) for i in str(number) if i != '.']


if __name__ == '__main__':
    print(get_digits(16733))
    print(get_digits(13.909934))
    annotations = get_digits.__annotations__

    print(annotations['return'])
