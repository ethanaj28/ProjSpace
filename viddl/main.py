# Ethan's Game Collection
# All of my consoles and some of my games.
# Console - name, manufacturer and year
# Games - title, studio and year
# See all games and see all consoles
# Add new games and add new consoles

import sys
# Initialize the console class
class Console:
    def __init__(self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
    # Define console details
    def console_details(self):
        print(f'{self.name} | {self.manufacturer} | {self.year}')
# Initialize the games class
class Game:
    def __init__(self, title, studio, year):
        self.title = title
        self.studio = studio
        self.year = year
    # Define console details
    def game_details(self):
        print(f'{self.title} | {self.studio} | {self.year}')
# Initialize the closet class
class Closet:
    def __init__(self):
        self.consoles = []
        self.games = []

    def add_console(self, console):
        self.consoles.append(console)

    def add_game(self, game):
        self.games.append(game)

    def list_consoles(self):
        if self.consoles:
            print('The consoles Ethan has or had in the past.')
            for console in self.consoles:
                console.console_details()
        else:
            print('Ethan has never had a console.')

    def list_games(self):
        # If closet has games, print()
        if self.games:
            print('The games Ethan has or had in the past.')
            # Loop game details of all games
            for game in self.games:
                game.game_details()
        else:
            print('Ethan has never had a game.')
    # Defining add new console
    def add_new_console(self):
        name = input('What is the name of the console? ')
        manufacturer = input('Who manufactured the console? ')
        year = int(input('What year did you get the console? '))
        # Initializing the new console variable
        new_console = Console(name, manufacturer, year)
        # Adding new console to the closet
        self.add_console(new_console)
        print('New Console added.')
        # Print new console details
        new_console.console_details()

    def add_new_game(self):
        title = input('What is the title of the game? ')
        studio = input('Who created the game? ')
        year = int(input('What year did you get the game? '))
        new_game = Game(title, studio, year)
        self.add_game(new_game)
        print('New Game added.')
        new_game.game_details()

def main():
    closet = Closet()

    console0 = Console(name='Dreamcast', manufacturer='SEGA', year=2004)
    console1 = Console(name='PlayStation', manufacturer='Sony', year=2003)
    console3 = Console(name='Xbox', manufacturer='Microsoft', year=2005)

    closet.add_console(console0)
    closet.add_console(console1)
    closet.add_console(console3)

    game0 = Game(title='Crazy Taxi', studio='SEGA', year=2004)
    game1 = Game(title='Halo', studio='Bungie', year=2005)
    game2 = Game(title='Halo 2', studio='Bungie', year=2006)

    closet.add_game(game0)
    closet.add_game(game1)
    closet.add_game(game2)

    while True:
        print('\nWelcome to Ethan\'s Gaming Closet')
        print('1. View Consoles')
        print('2. View Games')
        print('3. Add New Game')
        print('4. Add New Console')
        print('5. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            closet.list_consoles()
        elif choice == '2':
            closet.list_games()
        elif choice == '3':
            closet.add_new_game()
        elif choice == '4':
            closet.add_new_console()
        elif choice == '5':
            print('Thanks for checking out my closet. Have a great day!')
            sys.exit()
        else:
            print('Invalid Input')

if __name__ == '__main__':
    main()