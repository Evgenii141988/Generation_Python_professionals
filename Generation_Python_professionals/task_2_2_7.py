def check_litters(word: str, check_word: str) -> bool:
    litters = 'ауоыиэяюёе'
    index_lit_word = [i for i, n in enumerate(word) if n in litters]
    index_lit_check_word = [i for i, n in enumerate(check_word) if n in litters]
    return all((i in index_lit_word for i, n in enumerate(check_word) if n in litters)) and len(index_lit_word) == len(index_lit_check_word)


if __name__ == '__main__':
    word = input()
    n = int(input())
    for _ in range(n):
        check_word = input()
        if check_litters(word, check_word):
            print(check_word)
