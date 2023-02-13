

if __name__ == '__main__':
    names = {'Дили': set(), 'Вили': set(), 'Били': set()}
    while True:
        string = input()
        if string == 'конец':
            break
        hero_name, user = string.split(': ')
        names[hero_name].add(user)
    for key in sorted(names, key=lambda x: len(names[x]), reverse=True):
        print(f'Количество уникальных комментаторов у {key} - {len(names[key])}')
