import itertools as it
import time

if __name__ == '__main__':

    symbols = ['.', '-', "'", '"', "'", '-', '.', '_']

    for c in it.cycle(symbols):
        print(c, end='')
        time.sleep(0.05)
