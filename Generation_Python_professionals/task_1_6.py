if __name__ == '__main__':
    string = input()
    print(string[:3].upper() + string[3:-3].lower() + string[-3:].upper())

