import random
import time
import os
from Funcs import *

gameState = 1
runTurn = 1
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

chosenWord = wordChoices[random.randint(0, numberWords)]

# This splits the chosen word into a list of characters
charList = list(chosenWord)
charsLeft = charList


while (gameState == 1):

    # Prints title page
    clearTerm()
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
        while runTurn:
            userInput = input("Guess One: Enter your 5 letter word guess: ").lower()

            clearTerm()

            guessOne = list(userInput)

            if checkLetters(guessOne, userInput, wordChoices, charList):
                continue
            else:
                runTurn = 0

        printBoardTwo(guessOne)

        if checkForWin(userInput, chosenWord):
            printWin(charList)
            gameState = 0
            continue

        runTurn = 1

        # ------------------
        while runTurn:
            userInputTwo = input("Guess Two: Enter your 5 letter word guess: ").lower()

            clearTerm()

            guessTwo = list(userInputTwo)

            if checkLetters(guessTwo, userInputTwo, wordChoices, charList):
                continue
            else:
                runTurn = 0

        printBoardThree(guessOne, guessTwo)

        checkForWin(userInput, chosenWord)

        if checkForWin(userInputTwo, chosenWord):
            printWin(charList)
            gameState = 0
            continue

        runTurn = 1

        # ------------------

        while runTurn:

            userInputThree = input("Guess Three: Enter your 5 letter word guess: ").lower()

            clearTerm()

            guessThree = list(userInputThree)

            if checkLetters(guessThree, userInputThree, wordChoices, charList):
                continue
            else:
                runTurn = 0

        printBoardFour(guessOne, guessTwo, guessThree)

        if checkForWin(userInputThree, chosenWord):
            printWin(charList)
            gameState = 0
            continue

        runTurn = 1

        # ------------------

        while runTurn:

            userInputFour = input("Guess Four: Enter your 5 letter word guess: ").lower()

            clearTerm()

            guessFour = list(userInputFour)

            if checkLetters(guessFour, userInputFour, wordChoices, charList):
                continue
            else:
                runTurn = 0

        printBoardFive(guessOne, guessTwo, guessThree, guessFour)

        if checkForWin(userInputFour, chosenWord):
            printWin(charList)
            gameState = 0
            continue

        runTurn = 1

        # ------------------

        while runTurn:
        
            userInputFive = input("Guess Five: Enter your 5 letter word guess: ").lower()

            clearTerm()

            guessFive = list(userInputFive)

            if checkLetters(guessFive, userInputFive, wordChoices, charList):
                continue
            else:
                runTurn = 0

        printBoardSix(guessOne, guessTwo, guessThree, guessFour, guessFive)

        if checkForWin(userInputFive, chosenWord):
            printWin(charList)
            gameState = 0
            continue

        runTurn = 1

        # ------------------

        while runTurn:

            userInputSix = input("Guess Six: Enter your 5 letter word guess: ").lower()

            clearTerm()

            guessSix = list(userInputSix)

            if checkLetters(guessSix, userInputSix, wordChoices, charList):
                continue
            else:
                runTurn = 0

        printBoardSeven(guessOne, guessTwo, guessThree, guessFour, guessFive, guessSix)

        if checkForWin(userInputSix, chosenWord):
            printWin(charList)
            gameState = 0
            continue
        else:
            printLose(charList)
            gameState = 0
            continue

        # ------------------

    elif (startGame == "rules"):
        clearTerm()
        print("The only rules are that there are no rules... and that this page is under construction!")
        gameState = 0;
        break
    elif (startGame == "exit"):
        clearTerm()
        print("Thank you for playing!")
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
        