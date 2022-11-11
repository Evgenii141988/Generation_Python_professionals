from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(times: int):
    def decorator(func):
        @wraps(func)
        def wrappers(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    continue
            raise MaxRetriesException

        return wrappers

    return decorator


@retry(3)
def no_way():
    raise ValueError


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


if __name__ == '__main__':
    try:
        no_way()
    except Exception as e:
        print(type(e))

    beegeek()
