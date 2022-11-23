def card_deck(my_suit: str):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    suits = ["пик", "треф", "бубен", "червей"]
    gen_cards = (f'{rank} {suit}' for suit in suits for rank in ranks if suit != my_suit)
    while True:
        try:
            yield next(gen_cards)
        except StopIteration:
            gen_cards = (f'{rank} {suit}' for suit in suits for rank in ranks if suit != my_suit)


if __name__ == '__main__':
    generator = card_deck('пик')

    print(next(generator))
    print(next(generator))
    print(next(generator))

    generator = card_deck('треф')
    cards = [next(generator) for _ in range(40)]

    print(*cards)
