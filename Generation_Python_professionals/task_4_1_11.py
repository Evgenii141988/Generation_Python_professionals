import sys

if __name__ == '__main__':
    marks = [int(mark.strip()) for mark in sys.stdin]
    if (len(marks) % 2 != 0 and marks[-1] % 2 == 0) or (len(marks) % 2 == 0 and marks[-1] % 2 != 0):
        print('Анри')
    else:
        print('Дима')