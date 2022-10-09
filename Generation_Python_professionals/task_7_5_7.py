class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str) -> bool:
    if len(string) < 9:
        raise LengthError
    elif string == string.upper() or string == string.lower():
        raise LetterError
    elif not any([elm.isdigit() for elm in string]):
        raise DigitError
    return True


if __name__ == '__main__':
    try:
        print(is_good_password('Short7'))
    except Exception as err:
        print(type(err))

    print(is_good_password('еПQSНгиfУЙ70qE'))

    try:
        print(is_good_password('41157081231232'))
    except Exception as err:
        print(type(err))
