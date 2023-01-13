if __name__ == '__main__':
    string = input()
    while string:
        l = len(string)
        string = string.replace('()', '')
        if len(string) == l:
            break
    print(('YES', 'NO')[bool(string)])
