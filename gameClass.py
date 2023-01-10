import random
import time
import os
from Funcs import *

class Pydle: 
    # Initializing the class variables
    def __init__(self):
        self.__gameState = 1
        self.__runTurn = 1
        self.__guessOne = []
        self.__guessTwo = []
        self.__guessThree = []
        self.__guessFour = []
        self.__guessFive = []
        self.__guessSix = []
        self.__wordChoices = []
        self.__chosenWord = ""
        self.__charList = []
        self.__charsLeft = []
        self.__startGame = 0
        self.__userInput = ""
        self.__guess = ""
        self.__count = 1
        self.__charCount = 0
        self.__greenColor = "\033[92m"
        self.__yellowColor = "\033[33m"
        self.__redColor = "\033[31m"
        self.__whiteColor = "\033[37m"
    # default print
    def __str__(self):
        return 'This is the class that runs the Py-dle game.'
    # Getters
    def getGuessOne(self):
        return self.__guessOne
    def getGuessTwo(self):
        return self.__guessTwo
    def getGuessThree(self):
        return self.__guessThree
    def getGuessFour(self):
        return self.__guessFour
    def getGuessFive(self):
        return self.__guessFive
    def getGuessSix(self):
        return self.__guessSix
    def getWordChoices(self):
        return self.__wordChoices
    def getChosenWord(self):
        return self.__chosenWord
    def getCharList(self):
        return self.__charList
    def getCharsLeft(self):
        return self.__charsLeft
    def getStartGame(self):
        return self.__startGame
    def getUserInput(self):
        return self.__userInput
    def getGuess(self):
        return self.__guess
    def getCount(self):
        return self.__count
    def getGameState(self):
        return self.__gameState
    def getRunTurn(self):
        return self.__runTurn
    def getCharCount(self):
        return self.__charCount
    #setters
    def setGuessOne(self, x):
        self.__guessOne = x
    def setGuessTwo(self, x):
        self.__guessTwo = x
    def setGuessThree(self, x):
        self.__guessThree = x
    def setGuessFour(self, x):
        self.__guessFour = x
    def setGuessFive(self, x):
        self.__guessFive = x
    def setGuessSix(self, x):
        self.__guessSix = x
    def setWordChoices(self, x):
        self.__wordChoices = x
    def setChosenWord(self, x):
        self.__chosenWord = x
    def setCharList(self, x):
        self.__charList = x
    def setCharsLeft(self, x):
        self.__charsLeft = x
    def setStartGame(self, x):
        self.__startGame = x
    def setUserInput(self, x):
        self.__userInput = x
    def setGuess(self, x):
        self.__guess = x
    def setCount(self, x):
        self.__count = x
    def setGameState(self, x):
        self.__gameState = x
    def setRunTurn(self, x):
        self.__runTurn = x
    def setCharCount(self, x):
        self.__charCount = x

    # class functions
    def clearTerm(self):
        # Check for linux/mac
        if(os.name == 'posix'):
            # issues correct clear command for linux/mac
            os.system('clear')
        # If windows
        else:
            # issues correct clear command for windows
            os.system('cls')

    def chooseWord(self):
        f = open("wordList.txt", "r", encoding = "utf8")

        fileContents = f.read()

        f.close()

        self.__wordChoices = fileContents.split()

        numberWords = len(self.__wordChoices)

        self.__chosenWord = self.__wordChoices[random.randint(0, numberWords)]

        self.__charList = list(self.__chosenWord)
        self.__charsLeft = self.__charList

    def wordReal(self, word, list):
        if word in list:
            return 1
        else:
            print("This is not a valid word!")
            return 0

    def checkLetters(self):
        if (len(self.__guess) == 5):
            if self.wordReal(self.__userInput, self.__wordChoices):
                self.__charsLeft = []
                self.__charCount = 0

                for letter in self.__guess:
                    self.__charsLeft.append(self.__charList[self.__charCount])
                    self.__charCount += 1

                count = 0

                for letter in self.__guess:
                    if letter == self.__charList[count]:
                        self.__guess[count] = self.__greenColor + letter + self.__whiteColor
                        self.__charsLeft[count] = '*'
                        count += 1
                    else:
                        self.__guess[count] = letter
                        count += 1
                
                count = 0
                
                for letter in self.__guess:
                    if letter in self.__charList and letter != self.__charList[count] and letter in self.__charsLeft:
                        self.__guess[count] = self.__yellowColor + letter + self.__whiteColor
                        count += 1
                    else:
                        self.__guess[count] = letter
                        count += 1
            else:
                print("You must enter a valid word!")
                return 1

        else:
            print("The entered word is not 5 characters long! Try Again")
            return 1

    def printBoardBlank(self):
        print("\n")
        print ("-----  -----  -----  -----  -----")
        print ("|   |  |   |  |   |  |   |  |   |")
        print ("|   |  |   |  |   |  |   |  |   |")
        print ("|   |  |   |  |   |  |   |  |   |")
        print ("-----  -----  -----  -----  -----")
        print("\n")
        print("\n")

    def printBoard(self):
        print("\n")
        print ("-----  -----  -----  -----  -----")
        print ("|   |  |   |  |   |  |   |  |   |")
        print ("|",self.__guess[0],"|  |",self.__guess[1],"|  |",self.__guess[2],"|  |",self.__guess[3],"|  |",self.__guess[4],"|")
        print ("|   |  |   |  |   |  |   |  |   |")
        print ("-----  -----  -----  -----  -----")
        print("\n")
        print("\n")

    def checkForWin(self):
        if self.__userInput == self.__chosenWord:
            return 1;
        else:
            return 0;

    def printWin(self):
        self.clearTerm()
        firstLet = self.__greenColor + 'W' + self.__whiteColor
        secondLet = self.__greenColor + 'I' + self.__whiteColor
        thirdLet = self.__greenColor + 'N' + self.__whiteColor
        self.__charList[0] = self.__greenColor + self.__charList[0] + self.__whiteColor
        self.__charList[1] = self.__greenColor + self.__charList[1] + self.__whiteColor
        self.__charList[2] = self.__greenColor + self.__charList[2] + self.__whiteColor
        self.__charList[3] = self.__greenColor + self.__charList[3] + self.__whiteColor
        self.__charList[4] = self.__greenColor + self.__charList[4] + self.__whiteColor
        print("\n")
        print ("-----  -----  -----  -----  -----")
        print ("|   |  |",firstLet,"|  |",secondLet,"|  |",thirdLet,"|  |   |")
        print ("|   |  |   |  |   |  |   |  |   |")
        print ("|",self.__charList[0],"|  |",self.__charList[1],"|  |",self.__charList[2],"|  |",self.__charList[3],"|  |",self.__charList[4],"|")
        print ("-----  -----  -----  -----  -----")
        print("\n")
        print("\n")

    def printLose(self):
        self.clearTerm()
        firstLet = self.__redColor + 'L' + self.__whiteColor
        secondLet = self.__redColor + 'O' + self.__whiteColor
        thirdLet = self.__redColor + 'S' + self.__whiteColor
        fourthLet = self.__redColor + 'E' + self.__whiteColor
        fifthLet = self.__redColor + 'R' + self.__whiteColor
        self.__charList[0] = self.__redColor + self.__charList[0] + self.__whiteColor
        self.__charList[1] = self.__redColor + self.__charList[1] + self.__whiteColor
        self.__charList[2] = self.__redColor + self.__charList[2] + self.__whiteColor
        self.__charList[3] = self.__redColor + self.__charList[3] + self.__whiteColor
        self.__charList[4] = self.__redColor + self.__charList[4] + self.__whiteColor
        print("\n")
        print ("-----  -----  -----  -----  -----")
        print ("|",firstLet,"|  |",secondLet,"|  |",thirdLet,"|  |",fourthLet,"|  |",fifthLet,"|")
        print ("|   |  |   |  |   |  |   |  |   |")
        print ("|",self.__charList[0],"|  |",self.__charList[1],"|  |",self.__charList[2],"|  |",self.__charList[3],"|  |",self.__charList[4],"|")
        print ("-----  -----  -----  -----  -----")
        print("\n")
        print("\n")
        
    def runTurn(self):
        while self.__runTurn:
            self.__userInput = input("Guess " + str(self.__count) + ": Enter your 5 letter word guess: ").lower()

            self.setGuess(list(self.__userInput))

            if self.checkLetters():
                continue
            else:
                self.setRunTurn(0)
                continue

        self.printBoard()

        if self.checkForWin():
            self.printWin()
            return 0
        elif self.checkForWin() == 0 and self.getCount() == 6:
            self.printLose()
            return 0
        else:
            self.__count += 1
            self.setRunTurn(1)
            return 1

    def runGame(self):
        self.chooseWord()
        while self.__gameState:
            self.clearTerm()
            self.printBoardBlank()

            # ------------------ Turn 1
            
            if self.runTurn() == 0:
                self.setGameState(0)
                return self.__gameState

            # ------------------ Turn 2
            
            if self.runTurn() == 0:
                self.setGameState(0)
                return self.__gameState

            # ------------------ Turn 3

            if self.runTurn() == 0:
                self.setGameState(0)
                return self.__gameState

            # ------------------ Turn 4

            if self.runTurn() == 0:
                self.setGameState(0)
                return self.__gameState

            # ------------------ Turn 5

            if self.runTurn() == 0:
                self.setGameState(0)
                return self.__gameState

            # ------------------ Turn 6

            if self.runTurn() == 0:
                self.setGameState(0)
                return self.__gameState

            # ------------------


    
