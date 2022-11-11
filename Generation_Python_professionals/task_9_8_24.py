from functools import wraps


def ignore_exception(*out_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as ex:
                if type(ex) not in out_args:
                    raise ex
                print(f'Исключение {ex.__class__.__name__} обработано')

        return wrapper

    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


if __name__ == '__main__':
    f(0)

    min = ignore_exception(ZeroDivisionError)(min)

    try:
        print(min(1, '2', 3, [4, 5]))
    except Exception as e:
        print(type(e))