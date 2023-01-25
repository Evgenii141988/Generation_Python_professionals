import pprint

if __name__ == '__main__':
    my_set = set()
    words = input().lower().split(',')
    for word in words:
        print('ДА' if word in my_set else 'НЕТ')
        my_set.add(word)
