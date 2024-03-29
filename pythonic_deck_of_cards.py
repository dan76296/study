import collections

# Tuples are immutable, more secure than dictionaries
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # list comprehension, nice and clean
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # useful list creator
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # creates an instance of each card in a deck to ._cards
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# good way to sort something that isn't sortable already
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

deck = FrenchDeck()


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
