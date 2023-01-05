import sys
if __name__ == '__main__':
    numbers = map(int, [num.strip() for num in sys.stdin])
    # print([hex(num)[2:].upper().zfill(2) for num in numbers])
    print(f'#{"".join([hex(num)[2:].upper().zfill(2) for num in numbers])}')

