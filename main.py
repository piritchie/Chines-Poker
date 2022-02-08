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
        description = "{number}-of-{suit}".format(number=self.number, suit=self.suit)
        return description


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for num in Card.two_low_numbers:
                self.cards.append(Card(suit, num))

    def deal(self):
        for card in self.cards:
            for i in range(len(new_deck.cards)):
                if i % 4 == 4 or i % 4 == 0:
                    player1.hand[len(player1.hand) + 1] = new_deck.cards[i]
                elif i % 4 == 3:
                    player2.hand[len(player2.hand) + 1] = new_deck.cards[i]
                elif i % 4 == 2:
                    player3.hand[len(player3.hand) + 1] = new_deck.cards[i]
                elif i % 4 == 1:
                    player4.hand[len(player4.hand) + 1] = new_deck.cards[i]

    def show(self):
        for c in self.cards:
            print(c)

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


class Hand:
    poker_hands = ['Single', 'Pair', 'Three-of-a-kind', 'Straight', 'Flush', 'Full House', 'Four-of-a-kind', 'Straight-Flush']

    def __init__(self, hand, high_card, player, list_of_cards):
        self.hand = hand
        self.high_card = high_card
        self.player = player
        self.list_of_cards = list_of_cards

        # high number is a card object

    def __lt__(self, other):
        if Hand.poker_hands.index(self.hand) < Hand.poker_hands.index(other.hand):
            if self.high_card < other.high_card:
                return True

    def __gt__(self, other):
        if self.hand == poker_hands[4] or self.hand == poker_hands[-1]:
            return self.high_card.suit_rank > other.high_card.suit_rank
        elif Hand.poker_hands.index(self.hand) > Hand.poker_hands.index(other.hand):
            if self.high_card > other.high_card:
                return True

    def __repr__(self):
        if self.hand in Hand.poker_hands[2:-1]:
            poker_hand_description = str(self.hand) + ', ' + str(self.high_card) + ' high'
            return poker_hand_description

        elif self.hand == Hand.poker_hands[1]:
            pair_description = 'Pair of ' + str(self.high_card.number) + 's, ' + str(self.high_card) + ' high'
            return pair_description

        elif self.hand == Hand.poker_hands[0]:
            return self.high_card

        if self.hand == 'pass':
            return 'pass'


class Player:
    def __init__(self, name):
        self.hand = {}
        self.name = name
        self.score = 0

    def __repr__(self):
        return self.name

    def play(self, cards):
        cards_played = [self.hand.pop(card) for card in cards]
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
            if len(cards) == 5:
                if is_in(sorted([card.number for card in cards_played], key= lambda card: Card.two_low_numbers.index(card)), Card.two_low_numbers) == True and sum(1 for card in cards_played if card.suit == cards_played[0].suit) == 5:
                    return Hand(Hand.poker_hands[4], sorted(cards_played)[-1], self, cards_played)

                for card in cards_played:
                    if card_numbers.count(card.number) == 4:
                       return Hand(Hand.poker_hands[3], card.number, self, cards_played)

                if len(fh_three) == 3 and len(fh_two) == 2:
                    return Hand(Hand.poker_hands[2], sorted(fh_three)[-1], self, cards_played)

                elif sum(1 for card in cards_played if card.suit == cards_played[0].suit) == 5:
                    return Hand(Hand.poker_hands[1], sorted(cards_played)[-1], self, cards_played)

                elif is_in(sorted([card.number for card in cards_played], key= lambda card: Card.two_low_numbers.index(card)), Card.two_low_numbers) == True:
                    return Hand(Hand.poker_hands[0], sorted(cards_played)[-1], self, cards_played)
                else:
                    return 'Not a valid poker hand'
            elif len(cards) == 3:
                if sum(1 for card in cards_played if card.number == cards_played[0].number) == 3:
                    return Hand('Three-of-a-kind', cards_played[0].number, self, cards_played)
                else:
                    return 'The only permissible hand containing two cards is a Three-of-a-kind'
            elif len(cards) == 2:
                if cards_played[0].number == cards_played[1].number:
                    return Hand(Hand.poker_hands[1], sorted(cards_played)[-1], self, cards_played)
                else:
                    return 'The only permissible hand containing two cards is a pair'
            elif len(cards) == 1:
                return Hand(Hand.poker_hands[0], cards_played[0], self, cards_played)
            elif cards == 'pass':
                return Hand('pass', '', self, [])
            else:
                return 'Not a permissible play. Please Try again'
        return what_is_it(cards)













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
print(type(welcome))
print(welcome)
print('Welcome to Chinese Poker!')
player1 = Player('Jacob')
player2 = Player('Cory')
player3 = Player('Emily')
player4 = Player('Dad')

players = [player1, player2, player3, player4]

for i in range(len(players) - 1, 0, -1):
    r = random.randint(0, i)
    players[i], players[r] = players[r], players[i]

new_deck = Deck()

new_deck.shuffle()
new_deck.deal()
turns = []
round_count = 1


print(players)

print(len(turns))
score_board = {player1: 0, player2: 0, player3: 0, player4: 0}

while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(player4.hand) != 0:
    for player in players:
        if len(turns) == 0:

            for card in player.hand.values():

                if card.suit == 'Diamonds' and card.number == 3:
                    first_turn = input(player.name + ", you have the 3-of-Diamonds. Please go first and include the 3-of-Diamonds in your opening hand.\nType the numbers of the cards you wish to play below:\n")

                    for card in player.play(first_turn).cards_played:
                        if card.suit == 'Diamonds' and card.number == 3:
                            turns.append(player.play(first_turn))

                            if len(first_turn) == 1:
                                if type(player_input[-1]) == 'int':
                                    turns.append(player.play(first_turn))

                                elif type(player_input[-1]) == 'str':
                                    if player_input[-1] == 'h':
                                        print(player.hand)
                                    elif player_input[-1] == 'pass':
                                        print('Don\'t be silly. You are first. Please play a valid hand includinf the 3-of-Diamonds')
                        else:
                            continue
                else:
                    continue

        if turns[-1].hand == 'pass':
            print(turns[-1].player + "passed")

        else:
            print(turns[-1].player + ' played a ' + turns[-1])

        while turns[-1].player == Player[players.index(player) - 1]:
            player_input = [input('{player_name} it is your turn.\n to pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h'.format(player_name=player.name))]
            if len(player_input) == 1:
                if type(player_input[-1]) == 'int':
                    if player.play(player_input) > turns[-1]:
                        turns.append(player.play(player_input))
                    else:
                        print(turns[-1].player + ' played a ' + turns[-1] + '. Please play a higher single card.')

                if type(player_input[-1]) == 'str':
                    if player_input[-1] == 'h':
                        print(player.hand)
                    if player_input[-1] == 'pass':
                        turns.append(player.play(player_input))

            elif len(player_input) == 2:
                if player.play(player_input) == Hand.poker_hands[1] and player.play(player_input) > turns[-1]:
                    turns.append(player.player(player_input))
                else:
                    print((turns[-1].player + ' played a ' + turns[-1] + '. Please play a higher single.'))

            elif len(player_input) == 3:
                if player.play(player_input) == Hand.poker_hands[1] and player.play(player_input) > turns[-1]:
                    turns.append(player.player(player_input))
                else:
                    print((turns[-1].player + ' played a ' + turns[-1] + '. Please play a higher pair.'))
            elif len(player_input) == 4:
                print('Error: 4 cards is not a valid entry. If you are trying to play a Four-of-a-kind, please include any fifth card')
            elif len(player_input) == 5:
                if player.play(player_input) != 'Not a valid poker hand' and player.play(player_input) > turns[-1]:
                    turns.append(player.play(player_input))
                elif player.play(player_input) <= turns[-1]:
                    print((turns[-1].player + ' played a ' + turns[-1] + '. Please play a higher poker hand.'))
            elif player.play(player_input) == 'Not a permissible play. Please Try again':
                player.play(player_input)














