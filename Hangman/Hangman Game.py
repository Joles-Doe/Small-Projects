import random
import sys
import time
import turtle

def Hang1():
    turtle.lt(180)          #All of these are functions for the turtle graphics
    turtle.fd(200)

def Hang2():
    turtle.rt(90)
    turtle.fd(300)

def Hang3():
    turtle.rt(90)
    turtle.fd(300)

def Hang4():
    turtle.rt(90)
    turtle.fd(45)

def Hang5():
    turtle.rt(90)
    turtle.circle(25)

def Hang6():
    turtle.lt(90)
    turtle.penup()
    turtle.fd(53)
    turtle.pendown()
    turtle.fd(90)

def Hang7():
    turtle.penup()
    turtle.backward(70)
    turtle.pendown()
    turtle.left(45)
    turtle.fd(50)

def Hang8():
    turtle.backward(50)
    turtle.rt(90)
    turtle.fd(50)
    turtle.backward(50)
    turtle.lt(45)

def Hang9():
    turtle.fd(70)
    turtle.rt(45)
    turtle.fd(50)
    turtle.backward(50)

def Hang10():
    turtle.lt(90)
    turtle.fd(50)


List = ["insert", "production", "sweep", "distort", "genetic", "disappoint", "double", "thread", "object", "action", "sculpture", "meat", "skate", "testify", "window",
        "short", "lonely", "investigation", "missile", 'house', 'bomb', 'pray', 'space', 'environment', 'violation', 'children', 'haircut', 'intelligence', 'conspiracy',
        'estimate', 'circumstance', 'cat', 'reward', 'house', 'bean', 'earthquake', 'citizen', 'needle', 'scott', 'friend', 'enemy', 'dumb', 'motorcycle', 'german']
#List of words for hangman

alphabet = 'abcdefghijklmnopqrstuvwxyz'
game = False
wordguess = []
wordbank = []
word = random.choice(List) #Chooses a word for hangman
length_word = len(word) #Counts the amount of letters in the word for later
guesses = 0

for character in word:
    wordguess.append('-')   #Appends a '-' inside the array for every character in the word


print('Welcome to hangman!')
time.sleep(1)

choice = input('You have 3 modes: Easy(1) Medium(2) Hard(3)')
if choice == '1':
    print('You have 10 guesses to try and guess my secret word!')
if choice == '2':
    guesses = 3
    print('You have 7 guesses to try and guess my secret word!') #This bit allows you to choose a mode
if choice == '3':
    guesses = 5
    print('You have 5 guesses to try and guess my secret word!')
    
time.sleep(1)
print('My secret word has', length_word, 'letters!')
time.sleep(1)
while guesses < 10:
    guess = input('Guess a letter or the word')
    if guess == word:
        print('You won! Thanks for playing!')
        game = True
        break
    elif guess in wordbank:
        print('You already guessed that!') #If the letter has already been guessed
        
    elif guess not in alphabet:
        print('Please guess a letter between a-z') #If guess is not a single letter
        
    elif guess in word:
        wordbank.append(guess) #Puts the letter inside the word
        for x in range(0, length_word):
            if word[x] == guess:
                wordguess[x] = guess 
        print(wordguess)
        if not '-' in wordguess:
            print('You won! Thanks for playing!') #Detects whether or not '-' is left
            game = True
            break
    elif guess not in word:
        wordbank.append(guess)
        print('You guessed incorrectly!')
        guesses = guesses + 1 #Adds 1 guess to the counter
        if choice == '1': #This whole segment does the turtle graphics using functions above
            if guesses == 1:
                Hang1()
            if guesses == 2:
                Hang2()
            if guesses == 3:
                Hang3()
            if guesses == 4:
                Hang4()
            if guesses == 5:
                Hang5()
            if guesses == 6:
                Hang6()
            if guesses == 7:
                Hang7()
            if guesses == 8:
                Hang8()
            if guesses == 9:
                Hang9()
            if guesses == 10:
                Hang10()
        if choice == '2':
            if guesses == 4:
                Hang1()
                Hang2()
            if guesses == 5:
                Hang3()
                Hang4()
            if guesses == 6:
                Hang5()
            if guesses == 7:
                Hang6()
                Hang7()
            if guesses == 8:
                Hang8()
            if guesses == 9:
                Hang9()
            if guesses == 10:
                Hang10()
        if choice == '3':
            if guesses == 6:
                Hang1()
                Hang2()
            if guesses == 7:
                Hang3()
                Hang4()
            if guesses == 8:
                Hang5()
                Hang6()
            if guesses == 9:
                Hang7()
                Hang8()
            if guesses == 10:
                Hang9()
                Hang10()



if (game == False):
    print('You lost! The word was', word)
