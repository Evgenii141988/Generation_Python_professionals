def get_min_max(iterable) -> tuple:
    new_iter = iter(iterable)
    try:
        max_value = mix_value = next(new_iter)
        for elm in iterable:
            if elm > max_value:
                max_value = elm
            if elm < mix_value:
                mix_value = elm
        return mix_value, max_value
    except StopIteration:
        return None


if __name__ == '__main__':
    iterable = iter(range(10))

    print(get_min_max(iterable))

    iterable = [6, 4, 2, 33, 19, 1]

    print(get_min_max(iterable))

    iterable = iter([])

    print(get_min_max(iterable))
