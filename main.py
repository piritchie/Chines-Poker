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
    poker_hands = ['pass', 'Single', 'Pair', 'Three-of-a-kind', 'Straight', 'Flush', 'Full House', 'Four-of-a-kind', 'Straight-Flush']

    def __init__(self, hand, high_card, player, list_of_cards):
        self.hand = hand
        self.high_card = high_card
        self.player = player
        self.list_of_cards = list_of_cards

        # high number is a card object

    def __lt__(self, other):
        if self.hand == Hand.poker_hands[5] or self.hand == Hand.poker_hands[-1]:
            if self.high_card.suit_rank < other.high_card.suit_rank:
                return True
        elif Hand.poker_hands.index(self.hand) < Hand.poker_hands.index(other.hand) or Hand.poker_hands.index(
                self.hand) == Hand.poker_hands.index(other.hand):
            if self.high_card < other.high_card:
                return True

    def __gt__(self, other):
        if Hand.poker_hands.index(self.hand) > Hand.poker_hands.index(other.hand):
            return True

        elif Hand.poker_hands.index(self.hand) == Hand.poker_hands.index(other.hand):
            if self.hand == Hand.poker_hands[5] or self.hand == Hand.poker_hands[-1]:
                if self.high_card.suit_rank > other.high_card.suit_rank:
                    return True
                elif self.high_card.suit_rank == other.high_card.suit_rank:
                    return Card.two_low_numbers.index(self.high_card.number) > Card.two_low_numbers.index(other.high_card.number)
            elif self.hand == Hand.poker_hands[6] or self.hand == Hand.poker_hands[7]:
                return Card.two_low_numbers.index(self.high_card.number) > Card.two_low_numbers.index(other.high_card.number)
            else:
                return self.high_card > other.high_card



    def __repr__(self):
        if self.hand in Hand.poker_hands[3:-1]:
            poker_hand_description = str(self.hand) + ', ' + str(self.high_card) + ' high'
            return poker_hand_description

        elif self.hand == Hand.poker_hands[2]:
            pair_description = 'Pair of ' + str(self.high_card.number) + 's, ' + str(self.high_card) + ' high'
            return pair_description

        elif self.hand == Hand.poker_hands[1]:
            return Hand.poker_hands[1] + ' ' + str(self.high_card)

        if self.hand == Hand.poker_hands[0]:
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
                    return Hand(Hand.poker_hands[7], sorted([card for card in cards_played], key= lambda card: Card.two_low_numbers.index(card.number))[-1], self, cards_played)

                for card in cards_played:
                    if card_numbers.count(card.number) == 4:
                       return Hand(Hand.poker_hands[7], card.number, self, cards_played)

                if len(fh_three) == 3 and len(fh_two) == 2:
                    return Hand(Hand.poker_hands[6], sorted(fh_three)[-1], self, cards_played)

                elif sum(1 for card in cards_played if card.suit == cards_played[0].suit) == 5:
                    return Hand(Hand.poker_hands[5], sorted([card for card in cards_played], key= lambda card: Card.two_low_numbers.index(card.number))[-1], self, cards_played)

                elif is_in(sorted([card.number for card in cards_played], key= lambda card: Card.two_low_numbers.index(card)), Card.two_low_numbers) == True:
                    return Hand(Hand.poker_hands[4], sorted([card for card in cards_played], key= lambda card: Card.two_low_numbers.index(card.number))[-1], self, cards_played)
                else:
                    return 'Not a valid poker hand'

            elif len(cards) == 4:
                print('There is no valid hand containing four cards. If you are attemptng to play a four-of-a-kind, please include an extra card.')

            elif len(cards) == 3:
                if sum(1 for card in cards_played if card.number == cards_played[0].number) == 3:
                    return Hand(Hand.poker_hands[3], cards_played[0].number, self, cards_played)
                else:
                    return 'The only permissible hand containing three cards is a Three-of-a-kind'

            elif len(cards) == 2:
                if cards_played[0].number == cards_played[1].number:
                    return Hand(Hand.poker_hands[2], sorted(cards_played)[-1], self, cards_played)
                else:
                    return 'The only permissible hand containing two cards is a pair'

            elif len(cards) == 1:
                if type(cards[0]) == int:
                    return Hand(Hand.poker_hands[1], cards_played[0], self, cards_played)
            else:
                return 'Not a permissible play. Please Try again'
        return what_is_it(cards)


def pop_reset(turn_ints):
    for card_played in turn_ints:
        player.hand.pop(card_played)
    player.hand = dict(zip((range(1, len(player.hand) + 1)), (player.hand.values())))
    return player.hand

def list_ints(turn_input):
    return [int(entry) for entry in turn_input]

def keep_score(players):

    for player in players:
        if len(player.hand) == 0:
            for i in players:
                if len(i.hand) <= 7 and len(i.hand) != 0:
                    player.score += len(i.hand)
                elif len(i.hand) > 7 and len(i.hand) < 13:
                    player.score += 2 * len(i.hand)
                elif len(i.hand) == 13:
                    player.score += 3 * len(i.hand)
        elif len(player.hand) <= 7:
            player.score -= len(player.hand)
        elif len(player.hand) > 7 and len(player.hand) < 13:
            player.score -= 2 * len(player.hand)
        elif len(player.hand) == 13:
            player.score -= 3 * len(player.hand)
    score_board = {player1: player1.score, player2: player2.score, player3: player3.score, player4: player4.score}
    return score_board


cheat_sheet = '''
Suit order ranked highest to lowest:     Poker Hands ranked highest to lowest:
Spades                                   Straight-Flush (A run of five cards all the same suit)
Hearts                                   Four-of-a-kind (Four of the same number with one random card)
Clubs                                    Full House (Three of one number and two of another)
Diamonds                                 Flush (Five cards of the same suit)
                                         Straight (A run of five cards) 
'''




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
player1 = Player(input('Player 1, please enter your name: '))
player2 = Player(input('Player 2, please enter your name: '))
player3 = Player(input('Player 3, please enter your name: '))
player4 = Player(input('Player 4, please enter your name: '))
print('\n')

players = [player1, player2, player3, player4]

for i in range(len(players) - 1, 0, -1):
    r = random.randint(0, i)
    players[i], players[r] = players[r], players[i]


round_count = 1


while round_count < 11:
    turns = []
    new_deck = Deck()
    new_deck.shuffle()
    new_deck.deal()

    while len(player1.hand) != 0 and len(player2.hand) != 0 and len(player3.hand) != 0 and len(player4.hand) != 0:
        round_notification = 'Round {round_number}'.format(round_number= round_count)


        while len(turns) == 0:
            for i in players:
                for card in list(i.hand.values()):
                    # print(player.hand)
                    if card.suit == 'Diamonds' and card.number == 3:
                        first_counter = 0
                        print(i.name + ", you have the 3-of-Diamonds. Please go first and include the 3-of-Diamonds in your opening hand.\nType the numbers of the cards you wish to play separated by a comma below:\nType h to view your hand\nTo view the cheatsheet, type help\n")
                        # print(first_turn)
                        while first_counter == 0:
                            try:
                                first_turn = input('').split(',')
                                first_turn_ints = [int(entry) for entry in first_turn]
                                if type(i.play(first_turn_ints)) == str:
                                    print('Please play a valid hand containing the 3-of-Diamonds')
                                    continue
                                else:
                                    print("You are trying to play a {hand}. type y/n to confirm: ".format(
                                    hand=i.play(first_turn_ints)))
                                y_n_counter = 0
                                while y_n_counter == 0:
                                    verification = input('')
                                    if verification == 'y':
                                        three_of_diamonds_counter = 0
                                        for c in i.play(first_turn_ints).list_of_cards:
                                            if c.suit == 'Diamonds' and c.number == 3:
                                                turns.append(i.play(first_turn_ints))
                                                for card_played in first_turn_ints:
                                                    i.hand.pop(card_played)
                                                i.hand = dict(zip((range(1, len(i.hand) + 1)), (i.hand.values())))
                                                first_counter += 1
                                                y_n_counter += 1
                                                three_of_diamonds_counter += 1
                                                continue
                                        if three_of_diamonds_counter == 0:
                                            print('The hand you are attempting to play must contain the 3-of-Diamonds.')
                                            y_n_counter += 1
                                            continue

                                    elif verification == 'n':
                                        print(i.name + ", you have the 3-of-Diamonds. Please go first and include the 3-of-Diamonds in your opening hand.\nType the numbers of the cards you wish to play separated by a comma below:\nType h to view you hand\nTo vie the cheatsheet, type help\n")
                                        y_n_counter += 1
                                        continue

                                    else:
                                        print('Press y/n to confirm.')
                                        continue

                            except ValueError:
                                if first_turn == ['h']:
                                    print(i.hand)
                                    continue
                                elif first_turn == ['help']:
                                    print(cheat_sheet)
                                    continue
                                elif first_turn == ['pass']:
                                    print('Are you sure you want to pass? y/n')
                                    pass_verify_count = 0
                                    while pass_verify_count == 0:
                                        pass_verify = input('')
                                        if pass_verify == 'y':
                                            print('Don\'t be silly. You are first. Please play a valid hand including the 3-of-Diamonds.')
                                            pass_verify_count +=1
                                            continue
                                        elif pass_verify == 'n':
                                            print(i.name + ", you have the 3-of-Diamonds. Please go first and include the 3-of-Diamonds in your opening hand.\nType the numbers of the cards you wish to play separated by a comma below:\nType h to view you hand\nTo view the cheatsheet, type help")
                                            pass_verify_count += 1
                                            continue
                                        else:
                                            print('Press y/n to confirm')
                                            continue
                                    continue
                                else:
                                    print('Not a valid selection. Please play a valid hand containing the 3-of-Diamonds')
                            except AttributeError:
                                print('Not a valid selection. Please play a valid hand containing the 3-of-Diamonds')
                            except KeyError:
                                print('Invalid selction. Please play a valid hand')
    ### End of first turn block

        for player in players:
            if len(turns[-1].player.hand) == 0:
                break
            while turns[-1].player == players[players.index(player) - 1]:
                counter = 0
                # Checks to see if the player before has passed and displays the hand


                if sum(1 for hand in turns[-3:] if hand.hand == 'pass') == 3:
                    print('{player}, it is your lead. You may play any valid hand.\nPress h to view your hand\nTo view the cheatsheet, type help\n'.format(player= player))
                    for has_one in players:
                        if len(has_one.hand) == 1:
                            print('{player} has one card left'.format(player=has_one))
                    lead_counter = 0
                    while lead_counter == 0:
                        try:
                            turn_input = input('').split(',')
                            turn_ints = [int(entry) for entry in turn_input]
                            if type(player.play(turn_ints)) == str:
                                print(player.play(turn_ints))
                                continue
                            print('You are trying to play a {hand}. Type y/n to confirm'.format(hand=player.play(turn_ints)))
                            verify_counter = 0

                            while verify_counter == 0:
                                verify = input('')
                                if verify == 'y':
                                    verify_counter += 1
                                    lead_counter += 1
                                    turns.append(player.play(turn_ints))
                                    pop_reset(turn_ints)
                                    counter += 1
                                    continue
                                elif verify == 'n':
                                    verify_counter += 1
                                    continue
                                else:
                                    print("Type y/n to confirm")

                        except ValueError:
                            if turn_input == ['h']:
                                print(player.hand)
                                continue
                            elif turn_input == ['pass']:
                                print('Don\'t be silly. You have the lead. Please play any valid hand.')
                                continue
                            elif turn_input == ['help']:
                                print(cheat_sheet)
                                continue
                            else:
                                print('Not a valid hand. Please try again.')
                                continue
                        except AttributeError:
                            print(player.play(turn_ints))
                        except KeyError:
                            print('Invalid selction. Please play a valid hand')
                        continue

                elif sum(1 for hand in turns[-2:] if hand.hand == 'pass') == 2:
                    print('{player}, {prev_player} passed. Please play a higher hand than {not_pass_player}\'s {not_pass_turn}\nTo view your hand, press h\n To view the cheatsheet, type help\nTo pass, type pass\n'.format(player= player, prev_player= turns[-1].player, not_pass_player= turns[-3].player, not_pass_turn= turns[-3]))
                    for has_one in players:
                        if len(has_one.hand) == 1:
                            print('{player} has one card left'.format(player=has_one))
                elif str(turns[-1]) == 'pass':
                    print('{player}, {prev_player} passed. Please play a higher hand than {prev_turn}\'s {prev_hand}\nTo view your hand, press h\nTo view the cheatsheet, type help\nTo pass, type pass\n'.format(player=player,prev_player=turns[-1].player,prev_turn=turns[-2].player, prev_hand= turns[-2]))
                    for has_one in players:
                        if len(has_one.hand) == 1:
                            print('{player} has one card left'.format(player=has_one))
                # Instructs the program to let the player who last played a hand to lead with any card

                else:
                    print(str(turns[-1].player) + ' played a ' + str(turns[-1]) + '\n\n')
                    print('{player_name} it is your turn.\nPlease play a higher hand than {previous_player}\'s {previous_turn}\nTo pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h\nTo view the cheatsheet, type help\n'.format(player_name=player.name, previous_player=turns[-1].player, previous_turn= turns[-1]))
                    for has_one in players:
                        if len(has_one.hand) == 1:
                            print('{player} has one card left'.format(player=has_one))
                while counter == 0:
                    if turns[-1].hand == 'pass' and turns[-2].hand == 'pass':
                        try:
                            turn_input = input('').split(',')
                            turn_ints = [int(entry) for entry in turn_input]
                            if type(player.play(turn_ints)) == str:
                                print(player.play(turn_ints))
                                continue
                            verify_counter = 0
                            while verify_counter == 0:
                                print('You are trying to play a {hand}. Type y/n to confirm'.format(
                                    hand=player.play(turn_ints)))
                                verify = input('')
                                if verify == 'y':
                                    verify_counter +=1
                                    if len(player.play(turn_ints).list_of_cards) == len(turns[-3].list_of_cards):
                                        print('hi')
                                        if type(player.play(turn_ints)) == str:
                                            print(player.play(turn_ints))
                                            continue
                                        elif player.play(turn_ints).hand == 'Single':
                                            if player.play(turn_ints) > turns[-3]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            elif player.play(turn_ints) < turns[-3]:
                                                print(str(player.play(turn_ints)) + ' is not higher than ' + str(turns[-3]))
                                            # except ValueError:
                                            #     print(
                                            #         'Not a valid hand. Please play a hand higher than {prev_turn}'.format(
                                            #             prev_turn=turns[-3]))

                                        elif player.play(turn_ints).hand == 'Pair':
                                            if player.play(turn_ints).hand == Hand.poker_hands[2] and player.play(turn_ints) > turns[-3]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            else:
                                                print(str(turns[-3].player) + ' played a ' + str(
                                                    turns[-3]) + '. Please play a higher pair.')

                                        elif player.play(turn_ints).hand == 'Three-of-a-kind':
                                            if player.play(turn_ints) == Hand.poker_hands[3] and player.play(turn_ints) > turns[-3]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            else:
                                                print(str(turns[-3].player) + ' played a ' + str(
                                                    turns[-3]) + '. Please play a higher Three-of-a-kind.')

                                        elif len(turn_ints) == 4:
                                            print(
                                                'Error: 4 cards is not a valid entry. If you are trying to play a Four-of-a-kind, please include any fifth card')

                                        elif len(turn_ints) == 5:
                                            if player.play(turn_ints) != 'Not a valid poker hand' and turns[-3].hand in Hand.poker_hands[4:]:
                                                if player.play(turn_ints) > turns[-3]:
                                                    turns.append(player.play(turn_ints))
                                                    pop_reset(turn_ints)
                                                    counter += 1
                                                elif player.play(turn_ints) < turns[-3]:
                                                    print('{player_passed} passed. Please play a higher poker hand than {last_hand_player}\'s {last_valid hand}'.format(player_passed= str(turns[-1].player), last_hand_player=str(turns[-3].hand)))
                                    else:
                                        print(str(turns[-3].player) + ' played a ' + str(turns[-3]) + '. Your hand must contain the same number of cards.')
                                elif verify == 'n':
                                    print('Please play a higher hand than {previous_player}\'s {previous_turn}\nTo pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h\nTo vie the cheatsheet, type help\n'.format(player_name=player.name, previous_player=turns[-1].player, previous_turn= turns[-1]))
                                    verify_counter += 1
                                else:
                                    print('Press y/n to confirm')
                                    continue

                        except ValueError:
                            if turn_input == ['h']:
                                print(player.hand)
                                continue

                            elif turn_input == ['pass']:
                                print('Are you sure you want to pass? y/n')
                                pass_verify_count = 0
                                while pass_verify_count == 0:
                                    pass_verify = input('')
                                    if pass_verify == 'y':
                                        turns.append(player.play(turn_input))
                                        counter += 1
                                        pass_verify_count += 1
                                    elif pass_verify == 'n':
                                        print(
                                            'Please play a higher hand than {previous_player}\'s {previous_turn}\nTo pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h\nTo vie the cheatsheet, type help\n'.format(player_name=player.name, previous_player=str(turns[-1].player), previous_turn=str(turns[-1])))
                                        pass_verify_count += 1
                                        continue
                                    else:
                                        print('Press y/n to confirm')
                            else:
                                print('Invalid selection. Please play a valid hand.')
                        except AttributeError:
                            print(player.play(turn_ints))
                        except KeyError:
                            print('Invalid selection. Please play a valid hand')

                    elif turns[-1].hand == 'pass':
                        # print('yoyo')
                        try:
                            turn_input = input('').split(',')
                            turn_ints = [int(entry) for entry in turn_input]
                            if type(player.play(turn_ints)) == str:
                                print(player.play(turn_ints))
                                continue
                            print('You are trying to play a {hand}. Type y/n to confirm'.format(hand=player.play(turn_ints)))
                            verify_counter = 0
                            while verify_counter == 0:
                                verify = input('')
                                if verify == 'y':
                                    verify_counter += 1
                                    if len(player.play(turn_ints).list_of_cards) == len(turns[-2].list_of_cards):
                                        if type(player.play(turn_ints)) == str:
                                            print(player.play(turn_ints))
                                            continue

                                        elif player.play(turn_ints).hand == 'Single':
                                            if player.play(turn_ints) > turns[-2]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            elif player.play(turn_ints) < turns[-2]:
                                                print(str(player.play(turn_ints)) + ' is not higher than ' + str(turns[-2]))

                                        elif player.play(turn_ints).hand == 'Pair':
                                            if player.play(turn_ints).hand == Hand.poker_hands[2] and player.play(turn_ints) > turns[-2]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            else:
                                                print(str(turns[-2].player) + 'passed played a ' + str(
                                                    turns[-2]) + '. Please play a higher pair.')

                                        elif player.play(turn_ints).hand == 'Three-of-a-kind':
                                            if player.play(turn_ints) == Hand.poker_hands[3] and player.play(turn_ints) > turns[-2]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            else:
                                                print(str(turns[-2].player) + ' played a ' + str(
                                                    turns[-2]) + '. Please play a higher Three-of-a-kind.')

                                        elif len(turn_ints) == 4:
                                            print(
                                                'Error: 4 cards is not a valid entry. If you are trying to play a Four-of-a-kind, please include any fifth card')

                                        elif len(turn_ints) == 5:
                                            print(player.play(turn_ints) > turns[-2])
                                            if player.play(turn_ints) != 'Not a valid poker hand' and player.play(turn_ints) > turns[-2]:

                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            elif player.play(turn_ints) < turns[-2]:
                                                print(str(turns[-2].player) + ' played a ' + str(turns[
                                                    -2]) + '. Please play a higher poker hand.')
                                    else:
                                        print(str(turns[-2].player) + ' played a ' + str(turns[-2]) + '. Your hand must contain the same number of cards.')
                                elif verify == 'n':
                                    print('Please play a higher hand than {previous_player}\'s {previous_turn}\nTo pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h\nTo view the cheatsheet, type help\n').format(player_name=player.name, previous_player=str(turns[-1].player), previous_turn=str(turns[-1]))
                                    verify_counter += 1
                                else:
                                    print('Press y/n to confirm')

                        except ValueError:
                            if turn_input == ['h']:
                                print(player.hand)
                                continue
                            elif turn_input == ['help']:
                                print(cheat_sheet)
                                continue

                            elif turn_input == ['pass']:
                                print('Are you sure you want to pass? y/n')
                                pass_verify_count = 0
                                while pass_verify_count == 0:
                                    pass_verify = input('')
                                    if pass_verify == 'y':
                                        turns.append(player.play(turn_input))
                                        counter += 1
                                        pass_verify_count += 1
                                    elif pass_verify == 'n':
                                        print(
                                            'Please play a higher hand than {previous_player}\'s {previous_turn}\nTo pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h\nTo view the cheatsheet, type help'.format(
                                                player_name=player.name, previous_player=str(turns[-1].player),
                                                previous_turn=turns[-1]))
                                        pass_verify_count += 1
                                        continue
                                    else:
                                        print('Press y/n to confirm')
                            else:
                                print('Invalid selection. Please play a valid hand.')

                        except AttributeError:
                            print(player.play(turn_ints))
                        except KeyError:
                            print('Invalid selection. Please play a valid hand')
                    else:
                        try:
                            turn_input= input('').split(',')
                            turn_ints = [int(entry) for entry in turn_input]
                            if type(player.play(turn_ints)) == str:
                                print(player.play(turn_ints))
                                continue
                            print('You are trying to play a {hand}. Type y/n to confirm'.format(
                                hand=player.play(turn_ints)))
                            verify_counter = 0
                            while verify_counter == 0:
                                verify = input('')
                                if verify == 'y':
                                    verify_counter += 1
                                    if len(player.play(turn_ints).list_of_cards) == len(turns[-1].list_of_cards):
                                        if player.play(turn_ints) == str:
                                            print(player.play(turn_ints))
                                            continue

                                        elif player.play(turn_ints).hand == 'Single':
                                            if player.play(turn_ints) > turns[-1]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            elif player.play(turn_ints) < turns[-1]:
                                                print(str(player.play(turn_ints)) + ' is not higher than ' + str(turns[-1]))

                                        elif player.play(turn_ints).hand == 'Pair':
                                            print('I know this is a pair')
                                            if player.play(turn_ints).hand == Hand.poker_hands[2] and player.play(turn_ints) > turns[-1]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            else:
                                                print(str(turns[-1].player) + ' played a ' + str(turns[-1]) + '. Please play a higher pair.')

                                        elif player.play(turn_ints).hand == 'Three-of-a-kind':
                                            if player.play(turn_ints) == Hand.poker_hands[3] and player.play(turn_ints) > turns[-1]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter +=1
                                            else:
                                                print(str(turns[-1].player) + ' played a ' + str(turns[-1]) + '. Please play a higher Three-of-a-kind.')

                                        elif len(turn_ints) == 4:
                                            print('Error: 4 cards is not a valid entry. If you are trying to play a Four-of-a-kind, please include any fifth card')

                                        elif len(turn_ints) == 5:
                                            print(player.play(turn_ints) > turns[-1])
                                            if player.play(turn_ints) != 'Not a valid poker hand' and player.play(turn_ints) > turns[-1]:
                                                turns.append(player.play(turn_ints))
                                                pop_reset(turn_ints)
                                                counter += 1
                                            elif player.play(turn_ints) < turns[-1]:
                                                print(str(turns[-1].player) + ' played a ' + str(turns[-1]) + '. Please play a higher poker hand.')
                                            else:
                                                print(player.play(turn_ints))
                                    else:
                                        print(str(turns[-1].player) + ' played a ' + str(turns[-1]) + '. Your hand must contain the same number of cards.')
                                elif verify == 'n':
                                    print('Please play a higher hand than {previous_player}\'s {previous_turn}\nTo pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h\n'.format(player_name=player.name, previous_player=str(turns[-1].player), previous_turn= str(turns[-1])))
                                    verify_counter += 1
                                else:
                                    print('Press y/n to confirm')
                                    continue

                        except ValueError:
                            if turn_input == ['h']:
                                print(player.hand)
                                continue
                            elif turn_input == ['help']:
                                print(cheat_sheet)
                                continue

                            elif turn_input == ['pass']:
                                print('Are you sure you want to pass? y/n')
                                pass_verify_count = 0
                                while pass_verify_count ==0:
                                    pass_verify = input('')
                                    if pass_verify == 'y':
                                        turns.append(player.play(turn_input))
                                        counter += 1
                                        pass_verify_count += 1
                                    elif pass_verify == 'n':
                                        print('Please play a higher hand than {previous_player}\'s {previous_turn}\nTo pass, type pass\nTo play a hand, type the numbers that correspond to the cards you want play separated by a comma\nTo view your hand, type h\n'.format(player_name=player.name, previous_player=str(turns[-1].player), previous_turn= str(turns[-1])))
                                        pass_verify_count += 1
                                        continue
                                    else:
                                        print('Press y/n to confirm')
                            else:
                                print('Not a valid hand. Please play a valid hand below')
                        except AttributeError:
                            print(player.play(turn_ints))
                        except KeyError:
                            print('Invalid selection. Please play a valid hand')


    for player in players:
        if len(player.hand) == 0:
            print('{player} won round {round}'.format(player=player, round=round_count))
    round_count += 1
    print(keep_score(players))

    for player in players:
        player.hand = {}

print('Final Score')
print(keep_score(players))
print(keep_score(players).keys()[keep_score(players).values().index(max(keep_score(players).values()))] + ' Wins!!!')













