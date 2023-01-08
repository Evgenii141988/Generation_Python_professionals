import sys, re

if __name__ == '__main__':
    string = input()
    count = 0
    for i, lit in enumerate(string):
        if lit == 'a':
            for s in string[i + 1:]:
                if s == 'b':
                    count += 1
    print(count)
