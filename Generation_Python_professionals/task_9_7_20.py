def print_decorator(func):
    def wrapper(*args, **kwargs):
        args = tuple(str(arg).upper() for arg in args)
        kwargs = {k: v.upper() for k, v in kwargs.items()}
        func(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    print = print_decorator(print)
    print('hi', 'there', end='!')
    print('are you in trouble?')
    print(111, 222, 333, sep='xxx')