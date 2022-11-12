import sys
from functools import lru_cache


@lru_cache()
def learn_alphabet(word: str):
    return ''.join(sorted([lit for lit in word]))


if __name__ == '__main__':
    for word in sys.stdin.readlines():
        print(learn_alphabet(word.strip()))
