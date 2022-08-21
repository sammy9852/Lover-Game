# Importing colors module
from colors import *
# importing random module
from random import randint

# Welcome Screen
print(YELLOW, '***** Welcome to LOVER-GAME *****')
user_input = int(input(WHITE + '1. Start Game\n'
                               '2. About Lover-Game\n'
                               '3. Exit Application\n\n'
                               'Choose an option above : '))
s
# determine user input
if user_input == 1:
    user_input = int(input(WHITE + 'Choose your Level\n'
                                   '1. Lazy(1-100)\n'
                                   '2. Hard(1-500)\n'
                                   '3. Difficult(1-1000)\n'
                                   'Choose your level:  '))
    guess_range = 0
    if user_input == 1:
        guess_range = 100
    elif user_input == 2:
        guess_range = 500
    elif user_input == 3:
        guess_range = 1000
    print(RED, 'Choose from the above option')
    #        generate random number base on the guess range
    generated_number = randint(1, guess_range)
    #  user guessing attempt
    user_chance = 3
    for chance in range(3):
        user_guess = int(input(WHITE + 'Provide Your Guess Number:\t'))
        #             Determine/Validate User Guess
        if user_guess == generated_number:
            print(GREEN, f'Congratulations!! You Guess {generated_number} right')
            break
        elif user_guess > generated_number:
            print(PURPLE, f'{user_guess}\tToo High, Try Again!!!')
            user_chance -= 1
        elif user_guess < generated_number:
            print(PURPLE, f'{user_guess}\tToo Low, Try again!!!')
            user_chance -= 1

    if user_chance < 1:
        print(RED, f'You Failed, Try Again !!\n'
                   f'The Correct Guess Number is\t{generated_number}')


elif user_input == 2:
    print(YELLOW,
          'Love Guessing Number game which you will fall in love with it the moment you start to play it\tCHEERS')
elif user_input == 3:
    print(WHITE, 'Hope to see you again.')
    exit(1)
else:
    print(RED, 'Invalid Option\tTRY AGAIN!!!')
