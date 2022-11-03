new_print = print


def func(*args, sep=' ', end='\n'):
    new_print(*(arg.upper() if type(arg) == str else arg for arg in args), sep=sep.upper(), end=end.upper())


if __name__ == '__main__':
    print = func
    print('beegeek', [1, 2, 3], 4)
    print('bee', 'geek', sep=' and ', end=' wow')
    words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
    print(*words, sep=' to ', end=' LOVE')
