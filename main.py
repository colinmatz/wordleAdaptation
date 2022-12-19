import random
import time
import os
from Funcs import *

gameState = 1
greenColor = "\033[92m"
yellowColor = "\033[33m"
whiteColor = "\033[37m"
charsList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guessOne = []
guessTwo = []
guessThree = []
guessFour = []
guessFive = []
guessSix = []

# Selecting a random option from the list of words
f = open("wordList.txt", "r", encoding="utf8")

fileContents = f.read()

wordChoices = fileContents.split()

numberWords = len(wordChoices)

#chosenWord = wordChoices[random.randint(0, numberWords)]
chosenWord = "forma"

# This splits the chosen word into a list of characters
charList = list(chosenWord)
charsLeft = charList


while (gameState == 1):

    # Prints title page
    clearTerm()
    print(charsLeft)
    print("\n")
    print ("------------------------------------------------------------------------")
    print ("|                                                                      |")
    print ("|                   Welcome to Py-dle by Colin Matz!                   |")
    print ("|                                                                      |")
    print ("------------------------------------------------------------------------")
    print("\n")
    print("Ready to start the game, hear the rules, or exit?")
    print("\n")
    print("\n")
    startGame = input("(enter 'start' to begin game, 'rules to read the rules, or 'exit' to end the game): ").lower()
    print(startGame)
    print("\n")
    print("\n")

    if (startGame == "start"):
        clearTerm()
        print("\n")
        printAvailableChars(charsList)
        printBoardOne()

        # ------------------

        userInput = input("Enter your 5 letter word guess: ").lower()

        clearTerm()

        guessOne = list(userInput)

        checkLetters(guessOne, userInput, wordChoices, charList)

        print(guessOne)

        printBoardTwo(guessOne)

        # ------------------

        userInputTwo = input("Enter your 5 letter word guess: ").lower()

        clearTerm()

        guessTwo = list(userInputTwo)

        checkLetters(guessTwo, userInputTwo, wordChoices, charList)

        printBoardThree(guessOne, guessTwo)

        # ------------------

        userInputThree = input("Enter your 5 letter word guess: ").lower()

        clearTerm()

        guessThree = list(userInputThree)

        checkLetters(guessThree, userInputThree, wordChoices, charList)

        printBoardFour(guessOne, guessTwo, guessThree)

        # ------------------

        userInputFour = input("Enter your 5 letter word guess: ").lower()

        clearTerm()

        guessFour = list(userInputFour)

        checkLetters(guessFour, userInputFour, wordChoices, charList)

        printBoardFive(guessOne, guessTwo, guessThree, guessFour)

        # ------------------

        userInputFive = input("Enter your 5 letter word guess: ").lower()

        clearTerm()

        guessFive = list(userInputFive)

        checkLetters(guessFive, userInputFive, wordChoices, charList)

        printBoardSix(guessOne, guessTwo, guessThree, guessFour, guessFive)

        # ------------------

        userInputSix = input("Enter your 5 letter word guess: ").lower()

        clearTerm()

        guessSix = list(userInputSix)

        checkLetters(guessSix, userInputSix, wordChoices, charList)

        printBoardSeven(guessOne, guessTwo, guessThree, guessFour, guessFive, guessSix)

        # ------------------



        gameState = 0;
        break
    elif (startGame == "rules"):
        print("The code to rules has been entered!")
        gameState = 0;
        break
    elif (startGame == "exit"):
        print("the code to exit has been entered")
        gameState = 0;
        break
    else:
        print("Invalid option given, please try again!")
        print("Restarting game in 3...")
        time.sleep(1)
        print("                   2...")
        time.sleep(1)
        print("                   1...")
        time.sleep(1)
        continue
        