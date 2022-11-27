def parse_ranges(ranges: str):
    new_ranges = (tuple(map(int, elm.split('-'))) for elm in ranges.split(','))
    return (i for a, b in new_ranges for i in range(a, b + 1))


if __name__ == '__main__':
    print(*parse_ranges('1-2,4-4,8-10'))
    print(*parse_ranges('1-10,2-10'))
    print(*parse_ranges('7-32'))
