import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: FrenchDeck):
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print(rank_value)
    print(rank_value * len(suit_values) + suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()
    # print(len(deck))
    # print(deck[4])
    # print(deck[43::])
    # print(choice(deck))
    # for card in deck:
    #     print(card)
    for card in sorted(deck, key=spades_high):
        print(card)