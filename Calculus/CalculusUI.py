import fluentPython.Calculus
from fluentPython.Calculus.FrenchDeck import FrenchDeck
from fluentPython.Calculus.Game import Game


class InterfaceLayer:
    def __init__(self, current_menu=None, last_menu=None, current_game=None):
        self.current_menu = current_menu
        self.last_menu = last_menu
        self.current_game = current_game
        print('If you ever need to exist game, press -1\n')
        self.main_menu()

    def main_menu(self):
        self.last_menu = self.current_menu
        self.current_menu = 'main_menu'
        print(f'select options: \n\t1-NewGame\n\t2-Exit')
        choice = int(input('Enter option number: '))
        if choice == 1:
            num_of_players = int(input('Enter number of players: '))
            num_of_rounds = int(input('Enter number of rounds: '))
            self.current_game = Game(FrenchDeck(), num_of_players, num_of_rounds)
            players = []
            for names in range(num_of_players):
                players.append(input('Enter name of player: '))
            self.current_game.setupGame(*players)

        else:
            exit()


if __name__ == "__main__":
    InterfaceLayer()