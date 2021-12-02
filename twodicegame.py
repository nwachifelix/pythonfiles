# This is a two dice rolling game, where the two dice must output double sixes for the game to start.
# Importing the necessarry functions for the game. 
import random
import time
player = input('what\'s your name: ')
Roll_dice = 'yes'

while Roll_dice == 'yes' or Roll_dice == 'y':
    print(f'{player} is rolling the dice... ')
    time.sleep(0.1)

    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    print('The generated numbers are: ')
    print(f'Die1: {die_1}\nDie2: {die_2} ')

    if die_1 == 6 and die_2 == 6:
        print(f'That\'s a double {player}, your game starts now! ')
        print('Congratulations!')
        exit()
    
    else:
        print(f'You can do better {player}. ')
    Roll_dice = input(f'\nDo you wish to continue the game {player}? (Y/N) ')
