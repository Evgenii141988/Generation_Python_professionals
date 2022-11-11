from functools import wraps


def takes(*type_args: type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if all([type(elem) in type_args for elem in args]) and all(
                    [type(value) in type_args for value in kwargs.values()]):
                return func(*args, **kwargs)
            raise TypeError

        return wrapper

    return decorator


@takes(int, str)
def repeat_string(string, times):
    return string * times


@takes(list, bool, float, int)
def repeat_string1(string, times):
    return string * times


if __name__ == '__main__':
    print(repeat_string('bee', 3))

    try:
        print(repeat_string1('bee', 4))
    except TypeError as e:
        print(type(e))
