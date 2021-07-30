import random, time, sys

# Main interface for the game
def main():
    print("Welcome to Niko's Dice Simulator!")
    print('Enjoy!')

    print()
    print()
    print("Press 'r' to roll your die.")
    print("Enter 'q' to end the program")
    user_input = input()

    if user_input == "q":
         sys.exit()
    else:
         roll()
         main()
#logic for visualization of dice
def dice(a):
    if (a==1):
        print('|       |')
        print('|       |')
        print('|   •   |')
        print('|       |')
        print('|       |\n')

    elif (a==2):
        print('|       |')
        print('|  •    |')
        print('|       |')
        print('|    •  |')
        print('|       |\n')

    elif (a==3):
        print('|       |')
        print('|  •    |')
        print('|   •   |')
        print('|    •  |')
        print('|       |\n')

    elif (a==4):
        print('|        |')
        print('|  •  •  |')
        print('|        |')
        print('|  •  •  |')
        print('|        |\n')


    elif (a==5):
        print('|       |')
        print('|  • •  |')
        print('|   •   |')
        print('|  • •  |')
        print('|       |\n')

    elif (a==6):
        print('|        |')
        print('|  •  •  |')
        print('|  •  •  |')
        print('|  •  •  |')
        print('|        |\n')

#logic for rolling the dice
def roll():
    player = random.randint(1,6)
    print('You rolled')
    time.sleep(1)
    print('You rolled a', player)
    dice(player)
    print('')

    ai = random.randint(1,6)
    print('The computer rolls...')
    time.sleep(2)
    print('The computer rolled a', ai)
    dice(ai)
    print('')

    if player > ai:
        print('You win.')
    elif player == ai:
        print('Tie game.')
    else:
        print('You lose.')

    print('---------------\n')

if __name__ == '__main__':
    main()
