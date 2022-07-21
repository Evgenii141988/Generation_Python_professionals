def print_given(*args, **kwargs):
    for elm in args:
        print(f'{elm} {type(elm)}')
    keys = sorted(kwargs)
    for k in keys:
        print(f'{k} {kwargs[k]} {type(kwargs[k])}')


if __name__ == '__main__':
    print_given(1, [1, 2, 3], 'three', two=2)
    print_given('apple', 'cherry', 'watermelon')
    print_given()
