import pickle


def filter_dump(filename: str, objects: list, typename: type):
    with open(filename, 'wb') as file:
        pickle.dump([obj for obj in objects if type(obj) == typename], file)


if __name__ == '__main__':
   filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)