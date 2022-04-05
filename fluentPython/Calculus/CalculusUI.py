# CalculusUI.py
"""contains the InterfaceLayer class. Used for interaction with the game"""

import logging
import fluentPython.Calculus
from fluentPython.Calculus.CalculusExceptions import RoundError
from fluentPython.Calculus.FrenchDeck import FrenchDeck
from fluentPython.Calculus.Game import Game
from fluentPython.Calculus.Round import Round


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)


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
            print(f'hearts: {hand[0:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_spades
            print(f'spades: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_diamonds
            print(f'diamonds: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_clubs
            print(f'clubs: {hand[prior_high:current_highest_card]}')
        elif trumps == 'diamonds':  # CHSD
            prior_high = current_highest_card
            current_highest_card += hand._num_of_clubs
            print(f'clubs: {hand[0:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_hearts
            print(f'hearts: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_spades
            print(f'spades: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_diamonds
            print(f'diamonds: {hand[prior_high:current_highest_card]}')
        elif trumps == 'spades':  # DCHS
            prior_high = current_highest_card
            current_highest_card += hand._num_of_diamonds
            print(f'diamonds: {hand[0:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_clubs
            print(f'clubs: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_hearts
            print(f'hearts: {hand[prior_high:current_highest_card]}')
            prior_high = current_highest_card
            current_highest_card += hand._num_of_spades
            print(f'spades: {hand[prior_high:current_highest_card]}')
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
        #print(f'\nCurrent Menu: {self.current_menu}, Last Menu: {self.last_menu}')

        print(f'\nselect options: \n\t1-NewGame\n\t9-Last Menu\n\t10-Main Menu\n\t-1-Exit')
        choice = int(input('Enter option number: '))

        if choice == 1:
            num_of_players = int(input('Enter number of players: '))
            #num_of_rounds = int(input('Enter number of rounds: '))
            self.current_game = Game(FrenchDeck(), num_of_players, 10)
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
        #print(f'\nCurrent Menu: {self.current_menu}, Last Menu: {self.last_menu}')

        game_state = self.current_game.get_game_state()
        if game_state == 0:
            self.main_menu()
        elif game_state == 1:
            print('\nSetup Complete, actions below')
            print(f'select options: \n\t1-Get Players\n\t2-Play Round\n\t8-Game Menu\t9-Last Menu\t10-Main Menu\t-1-Exit')
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
        #print(f'\nCurrent Menu: {self.current_menu}, Last Menu: {self.last_menu}')

        game_state = self.current_game.get_game_state()
        current_round = self.current_game.getCurrentRound()
        # print the current state of the round to indicate next action
        if game_state == 0:
            self.main_menu()

        elif game_state == 1:
            # cards dealt | bets gathered | tricks played | round scored | tricks setup
            if current_round.get_round_state_detail()[0] == 0:
                print(f'select options: \n\t1-Deal\n\t'
                      f'9-Last Menu\t10-Main Menu\t-1-Exit')
            elif current_round.get_round_state_detail()[0] == 1 and current_round.get_round_state_detail()[1] == 0 :
                print(f'select options: \n\t2-Show Hand\t25-Sort Hand\t3-Show Trumps\t5-Get Bets\n\t'
                      f'9-Last Menu\t10-Main Menu\t-1-Exit')
            elif current_round.get_round_state_detail()[0] == 1 and current_round.get_round_state_detail()[1] == 1 :
                print(
                    f'select options: \n\t2-Show Hand\t25-Sort Hand\t3-Show Trumps\t7-Play Trick\t8-Play Tricks\n\t'
                    f'9-Last Menu\t10-Main Menu\t-1-Exit\t4-Show Round Detail')
            else:
                print(f'select options: \n\t1-Deal\t2-Show Hand\t25-Sort Hand\t3-Show Trumps\t4-Show Round Detail\n\t5-Get '
                      f'Bets\t6-Show Actual\t7-Play Trick\t8-Play Tricks\tt9-Last Menu\t10-Main Menu\t-1-Exit')
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
            try:
                current_round.setBets()
            except RoundError as error:
                print(f'action: {error.action}, message: {error.msg}')
            finally:
                self.round_menu()
        elif choice == 6:
            actual = current_round.get_actual()
            print(f'Player{"Actual":>12}    Bar')
            for record in actual:
                print(f'{record[0]:>6} {record[1]:>11}    {"*" * record[1]}')
            self.round_menu()
        elif choice == 7:
            #current_round.play_next_trick()
            self.trick_menu()
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
        self.last_menu = self.current_menu
        self.current_menu = 'Trick Menu'
        # print(f'\nCurrent Menu: {self.current_menu}, Last Menu: {self.last_menu}')

        game_state = self.current_game.get_game_state()
        current_round = self.current_game.getCurrentRound()
        # print the current state of the round to indicate next action
        if game_state == 0:
            self.main_menu()
        elif game_state == 1:
            # cards dealt | bets gathered | tricks played | round scored | tricks setup
            if current_round.get_round_state_detail()[0] == 0:
                self.round_menu()
            elif current_round.get_round_state_detail()[1] == 0:
                self.round_menu()
            elif current_round.get_round_state_detail()[2] == 0:
                current_trick = current_round.get_current_trick()

if __name__ == "__main__":
    InterfaceLayer()