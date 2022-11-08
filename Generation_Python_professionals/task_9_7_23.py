def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except Exception:
            return None, 'При вызове функции произошла ошибка'

    return wrapper


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1


if __name__ == '__main__':
    print(f(7))
    sum = exception_decorator(sum)

    print(sum(['199', '1', 187]))
