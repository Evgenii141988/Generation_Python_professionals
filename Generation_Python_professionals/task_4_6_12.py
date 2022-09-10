import sys
import pickle

if __name__ == '__main__':
    file_name, *data = [line.strip() for line in sys.stdin]
    with open(file_name, 'rb') as file:
        func = pickle.load(file)
        print(func(*data))
