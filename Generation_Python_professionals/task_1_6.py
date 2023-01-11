if __name__ == '__main__':
    string = input()
    sentence = 'Вопросительное' if string[-1] == '?' else 'Обычное'
    print(sentence)
