import random
from operator import attrgetter
from typing import Tuple

class Card:
    two_low_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    two_high_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace', 2]
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


        if self.suit == 'Spades':
            suit_rank = 4
        elif self.suit == 'Hearts':
            suit_rank = 3
        elif self.suit == "Clubs":
            suit_rank = 2
        elif self.suit == 'Diamonds':
            suit_rank = 1
        self.suit_rank = suit_rank

    def __lt__(self, other):
        two_high_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace', 2]

        if two_high_numbers.index(self.number) < two_high_numbers.index(other.number):
            return True
        elif two_high_numbers.index(self.number) == two_high_numbers.index(other.number):
            if self.suit_rank < other.suit_rank:
                return True

    def __gt__(self, other):
        two_high_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace', 2]
        if two_high_numbers.index(self.number) > two_high_numbers.index(other.number):
            return True
        elif two_high_numbers.index(self.number) == two_high_numbers.index(other.number):
            if self.suit_rank > other.suit_rank:
                return True

    def __repr__(self):
        description = "{number} of {suit}".format(number=self.number, suit=self.suit)
        return description


class Deck:
    def __init__(self):
        self.cards = []
        # for suit in Card.suits:
        #     for num in Card.two_low_numbers:
        #         self.cards.append(Card(suit, num))

    # def deal(self):
    #     # for card in self.cards
    #     # for i in range(len(new_deck.cards)):
    #     #     if i % 4 == 4 or i % 4 == 0:
    #     #         player1.hand[len(player1.hand) + 1] = new_deck.cards[i]
    #     #     elif i % 4 == 3:
    #     #         player2.hand[len(player2.hand) + 1] = new_deck.cards[i]
    #     #     elif i % 4 == 2:
    #     #         player3.hand[len(player3.hand) + 1] = new_deck.cards[i]
    #     #     elif i % 4 == 1:
    #     #         player4.hand[len(player4.hand) + 1] = new_deck.cards[i]

    def show(self):
        for c in self.cards:
            print(c)

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


class Hand:
    poker_hands = ['Straight', 'Flush', 'Full House', 'Four-of-a-kind', 'Straight Flush']

    def __init__(self, hand, high_card):
        self.hand = hand
        self.high_card = high_card
        # high number is a card object

    def __lt__(self, other):
        if Hand.poker_hands.index(self.hand) < Hand.poker_hands.index(other.hand):
            if self.high_card < other.high_card:
                return True

    def __gt__(self, other):
        if Hand.poker_hands.index(self.hand) > Hand.poker_hands.index(other.hand):
            if self.high_card > other.high_card:
                return True

    def __repr__(self):
        description = str(self.hand) + ', ' + str(self.high_card) + ' high'
        return description


class Player:
    def __init__(self, name):
        self.hand = {}
        self.name = name

    def play(self, cards):
        cards_played = [self.hand[card] for card in cards]
        card_numbers = [card.number for card in cards_played]
        fh_three = []
        fh_two = []
        for card in cards_played:
            if card_numbers.count(card.number) == 3:
                fh_three.append(card)
            elif card_numbers.count(card.number) == 2:
                fh_two.append(card)

        def is_in(lst1, lst2):
            for i in range(len(lst2)):
                if lst1 == lst2[i: (i + len(lst1))]:
                    return True

        def what_is_it(cards):
            print((cards))
            if len(cards) == 5:
                if is_in(sorted([card.number for card in cards_played], key= lambda card: Card.two_low_numbers.index(card)), Card.two_low_numbers) == True and sum(1 for card in cards_played if card.suit == cards_played[0].suit) == 5:
                    return Hand(Hand.poker_hands[4], sorted(cards_played)[-1])

                for card in cards_played:
                    if card_numbers.count(card.number) == 4:
                       return Hand(Hand.poker_hands[3], card.number)

                if len(fh_three) == 3 and len(fh_two) == 2:
                    return Hand(Hand.poker_hands[2], sorted(fh_three)[-1])

                elif sum(1 for card in cards_played if card.suit == cards_played[0].suit) == 5:
                    return Hand(Hand.poker_hands[1], sorted(cards_played)[-1])

                elif is_in(sorted([card.number for card in cards_played], key= lambda card: Card.two_low_numbers.index(card)), Card.two_low_numbers) == True:
                    return Hand(Hand.poker_hands[0], sorted(cards_played)[-1])
            elif len(cards) == 3:
                    if card_numbers.count(card.number) == 3:
                        return Hand('Three-of-a-kind', card.number)
            elif len(cards) == 2:
                return Hand('Pair of ' + str(sorted(cards_played)[-1].number) + 's', sorted(cards_played)[-1])

        return what_is_it(cards_played)











welcome = '''
    ------------------------------------------------------------------------------------------------
    |  CCC   H   H  IIIII  N    N  EEEEE   SSS    EEEEE    PPPP    OOO   K   K  EEEEE  RRRR    !!! |
    | C   C  H   H    I    NN   N  E      S    S  E        P   P  O   O  K  K   E      R   R   !!! |
    | C      H   H    I    N N  N  E      S       E        P   P  O   O  K K    E      R   R   !!! |
    | C      HHHHH    I    N  N N  EEEEE   S S    EEEEE    PPPP   O   O  KK     EEEEE  R  R    !!! |
    | C      H   H    I    N    N  E           S  E        P      O   O  K K    E      RR      !!! |
    | C   C  H   H    I    N    N  E      S    S  E        P      O   O  K  K   E      R  R    ... |
    |  CCC   H   H  IIIII  N    N  EEEEE   SSS    EEEEE    P       OOO   K   K  EEEEE  R   R   ... |
    ------------------------------------------------------------------------------------------------
    '''

print(welcome)
print('Welcome to Chinese Poker!')
player1 = Player('Jacob')
player2 = Player('Emily')
player3 = Player('cory')
player4 = Player('Dad')

players = [player1, player2, player3, player4]
new_deck = Deck()

# new_deck.shuffle()
# new_deck.deal()
card1 = Card('Hearts', 'Jack')
card2 = Card('Spades', 'Jack')
card3 = Card('Clubs', 'Jack')
card4 = Card('Diamonds', 'Jack')
card5 = Card('Hearts', 8)
new_deck.cards = [card1, card2, card3, card4, card5]
player1.hand = {1: card2, 2: card5, 3: card1, 4: card3, 5: card4}

print(player1.play(([ 5, 4])))


