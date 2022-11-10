from functools import wraps


def make_html(tag: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return wrapper

    return decorator


@make_html('del')
def get_text(text):
    return text


@make_html('i')
@make_html('del')
def get_text1(text):
    return text


if __name__ == '__main__':
    print(get_text('Python'))

    print(get_text1(text='decorators are so cool!'))