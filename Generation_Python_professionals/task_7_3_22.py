if __name__ == '__main__':
    filename = input()
    try:
        try:
            file = open(filename, encoding='utf-8')
            print(file.read())
        finally:
            file.close()
    except:
        print('Файл не найден')