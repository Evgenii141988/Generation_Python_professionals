import pickle
from collections import namedtuple

if __name__ == '__main__':
    Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
    with open('data.pkl', 'rb') as file:
        tuple_list = pickle.load(file)
    for elm in tuple_list:
        print(f'name: {elm.name}', f'family: {elm.family}', f'sex: {elm.sex}', f'color: {elm.color}', sep='\n')
        print()