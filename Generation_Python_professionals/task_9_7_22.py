def reverse_args(func):
    def wrapper(*args, **kwargs):
        result = func(*args[::-1], **kwargs)
        return result

    return wrapper


@reverse_args
def power(a, n):
    return a ** n


@reverse_args
def concat(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print(power(2, 3))
    print(concat('apple', 'cherry', 'melon'))
