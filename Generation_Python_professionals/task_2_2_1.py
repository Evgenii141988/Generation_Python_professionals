def get_min_distance(d1: int, d2: int, d3: int) -> int:
    return min([d1 + d2 + d3, d1 * 2 + d2 * 2, d1 * 2 + d3 * 2, d2 * 2 + d3 * 2])


if __name__ == '__main__':
    d1 = int(input())
    d2 = int(input())
    d3 = int(input())
    print(get_min_distance(d1, d2, d3))
