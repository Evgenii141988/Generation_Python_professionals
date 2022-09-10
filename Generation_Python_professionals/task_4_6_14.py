import pickle


def get_sum(obj: list | dict) -> int:
    numbers = [elm for elm in obj if type(elm) == int]
    if len(numbers) == 0:
        return 0
    if type(obj) == list:
        return max(numbers) * min(numbers)
    if type(obj) == dict:
        return sum(numbers)


if __name__ == '__main__':
    filename = input()
    number = int(input())
    with open(filename, 'rb') as file:
        obj = pickle.load(file)
    if number == get_sum(obj):
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')