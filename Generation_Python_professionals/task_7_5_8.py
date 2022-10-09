import sys


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
        raise LengthError('LengthError')
    elif string == string.upper() or string == string.lower():
        raise LetterError('LetterError')
    elif not any([elm.isdigit() for elm in string]):
        raise DigitError('DigitError')
    return 'Success!'


if __name__ == '__main__':
    passwords = [password.strip() for password in sys.stdin.readlines()]
    for password in passwords:
        try:
            result = is_good_password(password)
            print(result)
            break
        except Exception as err:
            print(err)