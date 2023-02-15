class Card:
    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"Card({self.value} of {self.suit})"
    
    def __it__(self, other):
        return self.value < other.value

    def __eq__(self, other: object):
        return self.value == other.value


class Deck:
    def __init__(self):
        self.values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.card_list = [Card(value, suit) for suit in self.suits for value in self.values]
    
    def __len__(self):
        return len(self.card_list)

    def sort(self):
        self.card_list = sorted(self.card_list, key= lambda x: x.suit)

    def __repr__(self):
        return f'{self.card_list}'

    def shuffle(self):
        from random import shuffle
        shuffle(self.values)
        shuffle(self.suits)
        self.card_list = [Card(value, suit) for suit in self.suits for value in self.values]
        shuffle(self.card_list)
    
    def draw_top(self):
        if not self.card_list:
            raise "Deck is empty"
        return self.card_list.pop()

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return f'{self.cards}'

    def play(self, card):
        card = f"Card({card.value} of {card.suit})"
        if card not in self.cards:
            raise f"{card} not in hand"
        else:
            self.cards.remove(card)

    
h_clubs = Hand([Card(value, 'clubs') for value in range(5, 0, -1)])
print(h_clubs)