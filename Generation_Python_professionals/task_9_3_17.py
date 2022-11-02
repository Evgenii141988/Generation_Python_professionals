from string import ascii_letters, ascii_lowercase, ascii_uppercase


def verification(login, password, success, failure):
    text_message = ''
    if not any([elm in ascii_letters for elm in password]):
        text_message = 'в пароле нет ни одной буквы'
    elif not any([elm in ascii_uppercase for elm in password]):
        text_message = 'в пароле нет ни одной заглавной буквы'
    elif not any([elm in ascii_lowercase for elm in password]):
        text_message = 'в пароле нет ни одной строчной буквы'
    elif not any([elm in '0123456789' for elm in password]):
        text_message = 'в пароле нет ни одной цифры'

    failure(login, text_message) if text_message else success(login)


def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


def success1(login):
    print(f'Здравствуйте, {login}!')


def failure1(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


if __name__ == '__main__':
    verification('timyrik20', 'Beegeek314', success, failure)
    verification('Ruslan_Chaniev', 'stepikstepik2', success1, failure1)
