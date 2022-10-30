def get_elm(string: str):
    obj = eval(string)
    if type(obj) == list:
        return obj[-1]
    if type(obj) == tuple:
        return obj[0]
    return len(obj)


if __name__ == '__main__':
    print(get_elm(input()))
    print(get_elm('[[1, 2], [3, 4], [5, 6]]'))
    print(get_elm("{'Arthur', 'Timur', 'Anri', 'Ruslan', 'Dima'}"))
    print(get_elm("('black', 'blue', 'red', 'orange', 'green', 'gray')"))
