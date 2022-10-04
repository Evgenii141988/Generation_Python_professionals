import sys

if __name__ == '__main__':
    total_number = 0
    counter_not_number = 0
    strings = (string.strip() for string in sys.stdin.readlines())
    for string in strings:
        try:
            total_number += int(string)
        except ValueError:
            try:
                total_number += float(string)
            except ValueError:
                counter_not_number += 1
    print(total_number, counter_not_number, sep='\n')