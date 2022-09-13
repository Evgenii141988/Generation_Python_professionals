if __name__ == '__main__':
    conformity_str = input()
    text = input().lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    translate_text = text.maketrans(alphabet, conformity_str)
    print(text.translate(translate_text))