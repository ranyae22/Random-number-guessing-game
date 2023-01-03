
import random

flag = True
while flag:
    num = input('What would you like the maximum number to be?: ')

    if num.isdigit():
        print("Let's play!")
        num = int(num)
        flag = False
    else:
        print('Invalid input. Please try again.')

secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
    guess = input('Guess a number between 1 and ' + str(num) + ': ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Invalid input. Please try again.')
        continue
    if guess == secret:
        print('You got it! It took you ' + str(count) + ' guesses.')
    else:
        if guess > secret:
            print('Too high, try again.')
        else:
            print('Too low, try again.')
        count += 1
        continue
    play_again = input('Would you like to play again? (y/n): ')
    if play_again == 'y':
        flag = True
    else:
        print('Thanks for playing!')
        break
    while flag:
        num = input('What would you like the maximum number to be?: ')
        if num.isdigit():
            print("Let's play!")
            num = int(num)
            flag = False
        else:
            print('Invalid input. Please try again.')
    secret