import sys

if __name__ == '__main__':
    count = 0
    for line in sys.stdin:
        if line.strip()[0] == '#':
            count += 1
    print(count)
