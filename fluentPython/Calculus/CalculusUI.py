# CalculusUI.py
"""contains the InterfaceLayer class. Used for interaction with the game"""

import fluentPython.Calculus
from fluentPython.Calculus.FrenchDeck import FrenchDeck
from fluentPython.Calculus.Game import Game


def print_sorted_hand(hand, trumps):
    current_highest_card = 0
    while current_highest_card < len(hand):
        if trumps == 'hearts':  # SDCH
            prior_high = current_highest_card
            current_highest_card += hand._num_of_spades
            print(f'spades: {hand[0:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_diamonds
            print(f'diamonds: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_clubs
            print(f'clubs: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_hearts
            print(f'hearts: {hand[prior_high:current_highest_card]}')
        elif trumps == 'clubs':  # HSDC
            prior_high = current_highest_card
            current_highest_card += hand._num_of_hearts
            print(f'hearts: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_spades
            print(f'spades: {hand[0:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_diamonds
            print(f'diamonds: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_clubs
            print(f'clubs: {hand[prior_high:current_highest_card]}')
        elif trumps == 'diamonds':  # CHSD
            prior_high = current_highest_card
            current_highest_card += hand._num_of_clubs
            print(f'clubs: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_hearts
            print(f'hearts: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_spades
            print(f'spades: {hand[0:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_diamonds
            print(f'diamonds: {hand[prior_high:current_highest_card]}')
        elif trumps == 'spades':  # DCHS
            prior_high = current_highest_card
            current_highest_card += hand._num_of_diamonds
            print(f'diamonds: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_clubs
            print(f'clubs: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_hearts
            print(f'hearts: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_spades
            print(f'spades: {hand[0:current_highest_card]}')
        else:
            raise Exception('trumps are invalid')


class InterfaceLayer:
    def __init__(self, current_menu=None, last_menu=None, current_game=None):
        self.current_menu = current_menu
        self.last_menu = last_menu
        self.current_game = current_game
        print('If you ever need to exist game, press -1\n')
        self.main_menu()

    def main_menu(self):
        self.last_menu = self.current_menu
        self.current_menu = 'Main Menu'
        print(f'\nCurrent Menu: {self.current_menu}, Last Menu: {self.last_menu}')

        print(f'select options: \n\t1-NewGame\n\t9-Last Menu\n\t10-Main Menu\n\t-1-Exit')
        choice = int(input('Enter option number: '))
        if choice == 1:
            num_of_players = int(input('Enter number of players: '))
            num_of_rounds = int(input('Enter number of rounds: '))
            self.current_game = Game(FrenchDeck(), num_of_players, num_of_rounds)
            players = []
            for names in range(num_of_players):
                players.append(input('Enter name of player: '))
            self.current_game.setupGame(*players)
            self.game_menu()
        elif choice == 9:
            if self.last_menu == 'Game Menu':
                self.game_menu()
            else:
                self.main_menu()
        elif choice == -1 or choice == 5:
            exit()
        else:
            exit()

    def game_menu(self):
        self.last_menu = self.current_menu
        self.current_menu = 'Game Menu'
        print(f'\nCurrent Menu: {self.current_menu}, Last Menu: {self.last_menu}')

        game_state = self.current_game.get_game_state()
        if game_state == 0:
            self.main_menu()
        elif game_state == 1:
            print('Setup Complete, actions below')
            print(f'select options: \n\t1-Get Players\n\t2-Play Round\n\t8-Game Menu\n\t9-Last Menu\n\t10-Main Menu\n\t-1-Exit')
            choice = int(input('Enter option number: '))
        else:
            exit()
        if choice == 1:
            for index, player in enumerate(self.current_game.getPlayers()):
                print(f'index: {index}, player: {player}')
            self.game_menu()
        elif choice == 2:
            current_round = self.current_game.getCurrentRound()
            self.round_menu()
        elif choice == 3:
            pass
            self.round_menu()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            self.game_menu()
        elif choice == 9:
            pass
        elif choice == 10:
            self.main_menu()
        elif choice == -1:
            exit()
        else:
            exit()

    def round_menu(self):
        self.last_menu = self.current_menu
        self.current_menu = 'Round Menu'
        print(f'\nCurrent Menu: {self.current_menu}, Last Menu: {self.last_menu}')

        game_state = self.current_game.get_game_state()
        current_round = self.current_game.getCurrentRound()
        if game_state == 0:
            self.main_menu()
        elif game_state == 1:
            print(f'select options: \n\t1-Deal\n\t2-Show Hand\n\t25-Sort Hand\n\t3-Show Trumps\n\t4-Show Round Detail\n\t5-Get '
                  f'Bets\n\t6-Show Actual\n\t7-Play Trick\n\t8-Play Tricks\n\t9-Last Menu\n\t10-Main Menu\n\t-1-Exit')
            choice = int(input('Enter option number: '))
        else:
            exit()
        if choice == 1:
            current_round.deal()
            self.round_menu()
        elif choice == 2:
            #current_round.showHand()
            hands = current_round.getHand()
            for each_hand in hands:
                print(f'player: {each_hand[0]}')
                print_sorted_hand(each_hand[1],each_hand[2])
                print('\n')

            self.round_menu()
        elif choice == 25:
            for player in self.current_game.getPlayers():
                player.hand.sort_hand(current_round.get_trumps())
            self.round_menu()
        elif choice == 3:
            print(current_round.get_trumps())
            self.round_menu()
        elif choice == 4:
            print(current_round)
            self.round_menu()
        elif choice == 5:
            current_round.getBets()
            self.round_menu()
        elif choice == 6:
            actual = current_round.show_actual()
            print(f'Player{"Actual":>12}    Bar')
            for record in actual:
                print(f'{record[0]:>6} {record[1]:>11}    {"*" * record[1]}')
            self.round_menu()
        elif choice == 7:
            current_round.play_next_trick()
            self.round_menu()
        elif choice == 8:
            current_round.playTricks()
            self.round_menu()
        elif choice == 9:
            pass
        elif choice == 10:
            self.main_menu()
        elif choice == -1:
            exit()
        else:
            exit()

    def trick_menu(self):
        #TODO make trick menu
        pass

if __name__ == "__main__":
    InterfaceLayer()