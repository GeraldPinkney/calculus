import fluentPython.Calculus
from fluentPython.Calculus.FrenchDeck import FrenchDeck
from fluentPython.Calculus.Game import Game


class InterfaceLayer:
    def __init__(self):
        current_menu = None
        last_menu = None
        current_game = None

    def main_menu(self):
        self.last_menu = self.current_menu
        self.current_menu = 'main_menu'
        print(f'select options: \n\t1-NewGame\n\t2-Exit')
        choice = input('Enter option number: ')
        if choice == 1:
            num_of_players = input('Enter number of players: ')
            num_of_rounds = input('Enter number of rounds: ')
            self.current_game = Game(FrenchDeck(), num_of_players, num_of_rounds)
        else:
            exit()
