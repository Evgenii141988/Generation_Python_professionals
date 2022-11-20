class Alphabet:
    EN_RU_ALPHABET = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}

    def __init__(self, language: str):
        self.language = language
        self.litters = iter(self.EN_RU_ALPHABET[language])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.litters)
        except StopIteration:
            self.litters = iter(self.EN_RU_ALPHABET[self.language])
            return next(self.litters)


if __name__ == '__main__':
    ru_alpha = Alphabet('ru')

    print(next(ru_alpha))
    print(next(ru_alpha))
    print(next(ru_alpha))

    en_alpha = Alphabet('en')

    letters = [next(en_alpha) for _ in range(28)]

    print(*letters)