class CardDeck:
    def __init__(self):
        self.suits = ("пик", "треф", "бубен", "червей")
        self.ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.cards = iter(f'{rank} {suit}' for suit in self.suits for rank in self.ranks)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cards)


if __name__ == '__main__':
    cards = CardDeck()

    print(next(cards))
    print(next(cards))

    cards = list(CardDeck())

    print(cards[9])
    print(cards[23])
    print(cards[37])
    print(cards[51])