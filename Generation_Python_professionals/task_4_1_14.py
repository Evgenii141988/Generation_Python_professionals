import sys

if __name__ == '__main__':
    my_line = ''
    for line in sys.stdin:
        my_line = line.strip()
        try:
            if my_line[0] != '#':
                sys.stdout.write(line)
        except IndexError:
            print()