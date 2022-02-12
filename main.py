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
        if self.hand == Hand.poker_hands[4] or self.hand == Hand.poker_hands[-1]:
            if self.high_card.suit_rank > other.high_card.suit_rank:
                return True
        elif Hand.poker_hands.index(self.hand) > Hand.poker_hands.index(other.hand) or Hand.poker_hands.index(self.hand) == Hand.poker_hands.index(other.hand):
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
            return str(self.high_card)

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
        if cards == ['pass']:
            return Hand('pass', '', self, [])
        cards_played = [self.hand[j] for j in cards]
        print(cards_played)
        # print(cards_played)
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
                    return Hand(Hand.poker_hands[7], sorted(cards_played)[-1], self, cards_played)

                for card in cards_played:
                    if card_numbers.count(card.number) == 4:
                       return Hand(Hand.poker_hands[6], card.number, self, cards_played)

                if len(fh_three) == 3 and len(fh_two) == 2:
                    return Hand(Hand.poker_hands[5], sorted(fh_three)[-1], self, cards_played)

                elif sum(1 for card in cards_played if card.suit == cards_played[0].suit) == 5:
                    return Hand(Hand.poker_hands[4], sorted(cards_played)[-1], self, cards_played)

                elif is_in(sorted([card.number for card in cards_played], key= lambda card: Card.two_low_numbers.index(card)), Card.two_low_numbers) == True:
                    return Hand(Hand.poker_hands[3], sorted(cards_played)[-1], self, cards_played)
                else:
                    return 'Not a valid poker hand'
            elif len(cards) == 3:
                if sum(1 for card in cards_played if card.number == cards_played[0].number) == 3:
                    return Hand(Hand.poker_hands[2], cards_played[0].number, self, cards_played)
                else:
                    return 'The only permissible hand containing three cards is a Three-of-a-kind'
            elif len(cards) == 2:
                if cards_played[0].number == cards_played[1].number:
                    return Hand(Hand.poker_hands[1], sorted(cards_played)[-1], self, cards_played)
                else:
                    return 'The only permissible hand containing two cards is a pair'
            elif len(cards) == 1:
                if type(cards[0]) == int:
                    return Hand(Hand.poker_hands[0], cards_played[0], self, cards_played)

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

testcard1 = Card('Diamonds', 4)
testcard2 = Card('Spades', 'Ace')
print(testcard2 > testcard1)
new_deck = Deck()

new_deck.shuffle()
new_deck.deal()
turns = []
round_count = 1
if round_count == 11:
    print('{player} wins!')
print(len(turns))
score_board = {player1: player1.score, player2: player2.score, player3: player3.score, player4: player4.score}
while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(player4.hand) != 0:

    while len(turns) == 0:
        for i in players:
            for card in list(i.hand.values()):
                # print(player.hand)
                if card.suit == 'Diamonds' and card.number == 3:
                    first_turn = input(i.name + ", you have the 3-of-Diamonds. Please go first and include the 3-of-Diamonds in your opening hand.\nType the numbers of the cards you wish to play below:\nType h to view you hand\n").split(',')
                    # print(first_turn)
                    try:
                        first_turn_ints = [int(entry) for entry in first_turn]
                        # print(first_turn_ints)
                        for c in i.play(first_turn_ints).list_of_cards:
                            if c.suit == 'Diamonds' and c.number == 3:
                                turns.append(i.play(first_turn_ints))
                    except ValueError:
                        while first_turn == ['h'] or first_turn == ['pass'] :
                            if first_turn == ['h']:
                                print(i.hand)
                                first_turn = input().split(',')
                                continue
                            elif first_turn == ['pass']:
                                print('Don\'t be silly. You are first. Please play a valid hand including the 3-of-Diamonds.')
                                continue


                    try:
                        first_turn_ints = [int(entry) for entry in first_turn]
                        for c in i.play(first_turn_ints).list_of_cards:
                            if c.suit == 'Diamonds' and c.number == 3:
                                is_true = True
                                if is_true is True:
                                    turns.append(i.play(first_turn_ints))
                                    for card_played in first_turn_ints:
                                        i.hand.pop(card_played)
                                    i.hand = dict(zip((range(1, len(i.hand) + 1)), (i.hand.values())))
                                else:
                                    print('{player}, please play a valid hand containing the 3-of-Diamonds'.format(player= turns[0].player))
                    except ValueError:
                        print('Not a valid hand. Please try again.')
                    except AttributeError:
                        print(i.play(first_turn_ints))

    for player in players:
        while turns[-1].player == players[players.index(player) - 1]:
            # Checks to see if the player before has passed and displays the hand
            if sum(1 for hand in turns[-2:] if hand.hand == 'pass') == 2:
                lead_input = input('{player}, {prev_player} passed. Please play a higher hand than {prev_turm}'.format(player= player, prev_player= turns[-2].player, prev_turn= turns[-2]))
                lead_ints = [int(entry) for entry in lead_input]
                # print(first_turn)
                try:
                    lead_ints = [int(entry) for entry in lead_input]
                except ValueError:
                    while lead_input == ['h'] or lead_input == ['pass']:
                        if lead_input == ['h']:
                            print(player.hand)
                            lead_input = input().split(',')
                            continue
                        elif lead_input == ['pass']:
                            print(
                                'Don\'t be silly. You have the lead. Please play any valid hand.')
                            continue
                try:
                    turns.append(player.play(lead_ints))
                    for card_played in lead_ints:
                        player.hand.pop(card_played)
                    player.hand = dict(zip((range(1, len(player.hand) + 1)), (player.hand.values())))
                except ValueError:
                    print('Not a valid hand. Please try again.')
                except AttributeError:
                    print(player.play(lead_ints))
                continue
            if sum(1 for hand in turns[-3:] if hand.hand == 'pass') == 3:
                lead_input = input('{player}, it is your lead. You may play any valid hand.\nPress h to view your hand'.format(player= player)).split(',')
                lead_ints = [int(entry) for entry in lead_input]
                # print(first_turn)
                try:
                    lead_ints = [int(entry) for entry in lead_input]
                except ValueError:
                    while lead_input == ['h'] or lead_input == ['pass']:
                        if lead_input == ['h']:
                            print(player.hand)
                            lead_input = input().split(',')
                            continue
                        elif lead_input == ['pass']:
                            print(
                                'Don\'t be silly. You have the lead. Please play any valid hand.')
                            continue
                try:
                    turns.append(player.play(lead_ints))
                    for card_played in lead_ints:
                        player.hand.pop(card_played)
                    player.hand = dict(zip((range(1, len(player.hand) + 1)), (player.hand.values())))
                except ValueError:
                    print('Not a valid hand. Please try again.')
                except AttributeError:
                    print(player.play(lead_ints))
                continue
            if turns[-1].hand == 'pass':
                print(str(turns[-1].player) + " passed")

            else:
                print(str(turns[-1].player) + ' played a ' + str(turns[-1]))
            turn_input = input('{player_name} it is your turn.\nPlease play a higher hand than {previous_player}\nTo pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h\n'.format(player_name=player.name, previous_player=turns[-1].player)).split(',')
            print(turn_input)
            if turn_input == ['pass']:
                turns.append(player.play(turn_input))

            try:
                turn_ints = [int(entry) for entry in turn_input]
                print(player.play(turn_ints) > turns[-1])
                if player.play(turn_ints) > turns[-1]:
                    turns.append(player.play(turn_ints))
                    for card_played in turn_ints:
                        player.hand.pop(card_played)
                    player.hand = dict(zip((range(1, len(player.hand) + 1)), (player.hand.values())))
                    print(player.hand)

                else:
                    print(
                        '{player}, please play a higher single card than {card}'.format(player=player, card=turns[-1]))
            except ValueError:
                while turn_input == ['h']:
                    if turn_input == ['h']:
                        print(player.hand)
                        turn_input = input().split(',')
                        continue
                if turn_input == ['pass']:
                    turns.append(player.play(turn_input))
                    continue


            if len(turn_input) == 1:
                #print(turn_input)
                # try:
                #     turn_ints = [int(entry) for entry in turn_input]
                #     print(player.play(turn_ints) > turns[-1])
                #     if player.play(turn_ints) > turns[-1]:
                #         turns.append(player.play(turn_ints))
                #         for card_played in turn_ints:
                #             player.hand.pop(card_played)
                #         player.hand = dict(zip((range(1, len(player.hand) + 1)), (player.hand.values())))
                #         print(player.hand)
                #
                #     else:
                #         print('{player}, please play a higher single card than {card}'.format(player=player, card=turns[-1]))
                # except ValueError:
                #     while turn_input == ['h']:
                #         if turn_input == ['h']:
                #             print(player.hand)
                #             turn_input = input().split(',')
                #             continue
                #     if turn_input == ['pass']:
                #         turns.append(player.play(turn_input))

                    try:
                        turn_ints = [int(entry) for entry in turn_input]
                        print(player.play(turn_ints) > turns[-1])
                        if player.play(turn_ints) > turns[-1]:
                            turns.append(player.play(turn_ints))
                            for card_played in turn_ints:
                                player.hand.pop(card_played)
                            player.hand = dict(zip((range(1, len(player.hand) + 1)), (player.hand.values())))
                            print(player.hand)
                    except ValueError:
                            print('Not a valid hand. Please play a hand higher than {prev_turn}'.format(prev_turn=turns[-1]))



            elif len(turn_input) == 2:
                if player.play(turn_ints).hand == Hand.poker_hands[1] and player.play(turn_ints) > turns[-1]:
                    turns.append(player.player(turn_ints))
                else:
                    print((turns[-1].player + ' played a ' + turns[-1] + '. Please play a higher single.'))

            elif len(turn_ints) == 3:
                if player.play(turn_ints) == Hand.poker_hands[1] and player.play(turn_ints) > turns[-1]:
                    turns.append(player.player(turn_ints))
                else:
                    print((turns[-1].player + ' played a ' + turns[-1] + '. Please play a higher pair.'))

            elif len(turn_ints) == 4:
                print('Error: 4 cards is not a valid entry. If you are trying to play a Four-of-a-kind, please include any fifth card')

            elif len(turn_ints) == 5:
                if player.play(turn_input) != 'Not a valid poker hand' and player.play(turn_input) > turns[-1]:
                    turns.append(player.play(turn_ints))
                elif player.play(turn_input) <= turns[-1]:
                    print((turns[-1].player + ' played a ' + turns[-1] + '. Please play a higher poker hand.'))

            elif player.play(turn_ints) == 'Not a permissible play. Please Try again':
                player.play(turn_ints)














