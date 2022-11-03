def remove_marks(text: str, marks: str):
    remove_marks.count += 1
    return ''.join([lit for lit in text if lit not in marks])


remove_marks.count = 0


if __name__ == '__main__':
    text = 'Hi! Will we go together?'

    print(remove_marks.count)
    print(remove_marks(text, '!?'))
    print(remove_marks.count)