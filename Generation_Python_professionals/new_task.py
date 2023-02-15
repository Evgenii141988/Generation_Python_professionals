def text_decor(func):
    def inner(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')

    return inner


@text_decor
def simple_func():
    print('I just simple python func')


@text_decor
def multiply(num1, num2):
    print(num1 * num2)


if __name__ == '__main__':
    simple_func()
    multiply(3, 5)
