from collections import Counter

if __name__ == '__main__':
    with open('pythonzen.txt', 'r', encoding='utf-8') as file:
        text = [elm for elm in file.read().lower() if elm in 'abcdefghijklmnopqrstuvwxyz']
    litters = Counter(text)
    for key in sorted(litters):
        print(f'{key}: {litters[key]}')