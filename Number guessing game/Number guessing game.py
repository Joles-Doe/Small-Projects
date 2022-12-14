import random
import time

guessesTaken = 0
num = random.randint(1, 50)

print('Welcome.')
time.sleep(3)
print('You get a number of tries depending of the difficulty to guess a randomly generated number between 1, 50.')
time.sleep(3)
mode = input('You have 3 modes, (1) - Easy - 10 guesses, (2) - Medium - 7 guesses, (3) - Hard - 5 guesses.')

if mode == '1':
    while guessesTaken <10:
        Guess1 = int(input('Take a guess.'))
        if Guess1 >num:
            print('Too high!')
            guessesTaken = guessesTaken + 1
        elif Guess1 <num:
            print('Too low!')
            guessesTaken = guessesTaken + 1
        elif Guess1 == num:
            print('You got the number! nice!')
            time.sleep(1000000000000)
        elif guessesTaken <10:
            print("Bad luck!")
            time.sleep(1000000000000)

elif mode == '2':
    while guessesTaken <7:
        Guess2 = int(input('Take a guess.'))
        if Guess2 >num:
            print('Too high!')
            guessesTaken = guessesTaken + 1
        elif Guess2 <num:
            print('Too low!')
            guessesTaken = guessesTaken + 1
        elif Guess2 == num:
            print('You got the number! nice!')
            time.sleep(1000000000000)
        elif guessesTaken <7:
            print("Bad luck!")
            time.sleep(1000000000000)

elif mode == '3':
    while guessesTaken <5:
        Guess3 = int(input('Take a guess.'))
        if Guess3 >num:
            print('Too high!')
            guessesTaken = guessesTaken + 1
        elif Guess3 <num:
            print('Too low!')
            guessesTaken = guessesTaken + 1
        elif Guess3 == num:
            print('You got the number! nice!')
            time.sleep(1000000000000)
        elif guessesTaken <5:
            print("Bad luck!")
            time.sleep(1000000000000)

