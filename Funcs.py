import os

greenColor = "\033[92m"
yellowColor = "\033[33m"
redColor = "\033[31m"
whiteColor = "\033[37m"

def clearTerm():
    # Check for linux/mac
    if(os.name == 'posix'):
        # issues correct clear command for linux/mac
        os.system('clear')
    # If windows
    else:
        # issues correct clear command for windows
        os.system('cls')

def printAvailableChars(charsList):
    print("Available Characters:", *charsList, sep='  ')

def wordReal(word, list):
    if word in list:
        print("This is a valid word!")
        return 1
    else:
        print("This is not a valid word!")
        return 0

def checkLetters(guess, userInput, wordChoices, charList):
    if (len(guess) == 5):
        if wordReal(userInput, wordChoices):
            charsLeft = []
            charCount = 0

            for letter in guess:
                charsLeft.append(charList[charCount])
                charCount += 1

            count = 0

            for letter in guess:
                if letter == charList[count]:
                    guess[count] = greenColor + letter + whiteColor
                    charsLeft[count] = '*'
                    count += 1
                else:
                    guess[count] = letter
                    count += 1
            
            count = 0
            
            for letter in guess:
                if letter in charList and letter != charList[count] and letter in charsLeft:
                    guess[count] = yellowColor + letter + whiteColor
                    count += 1
                else:
                    guess[count] = letter
                    count += 1
        else:
            print("You must enter a valid word!")
            return 1

    else:
        print("The entered word is not 5 characters long! Try Again")
        return 1

def printBoardOne():
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

def printBoardTwo(guessOne):
    printBoardOne()
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|",guessOne[0],"|  |",guessOne[1],"|  |",guessOne[2],"|  |",guessOne[3],"|  |",guessOne[4],"|")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

def printBoardThree(guessOne, guessTwo):
    printBoardTwo(guessOne)
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|",guessTwo[0],"|  |",guessTwo[1],"|  |",guessTwo[2],"|  |",guessTwo[3],"|  |",guessTwo[4],"|")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

def printBoardFour(guessOne, guessTwo, guessThree):
    printBoardThree(guessOne, guessTwo)
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|",guessThree[0],"|  |",guessThree[1],"|  |",guessThree[2],"|  |",guessThree[3],"|  |",guessThree[4],"|")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

def printBoardFive(guessOne, guessTwo, guessThree, guessFour):
    printBoardFour(guessOne, guessTwo, guessThree)
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|",guessFour[0],"|  |",guessFour[1],"|  |",guessFour[2],"|  |",guessFour[3],"|  |",guessFour[4],"|")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

def printBoardSix(guessOne, guessTwo, guessThree, guessFour, guessFive):
    printBoardFive(guessOne, guessTwo, guessThree, guessFour)
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|",guessFive[0],"|  |",guessFive[1],"|  |",guessFive[2],"|  |",guessFive[3],"|  |",guessFive[4],"|")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

def printBoardSeven(guessOne, guessTwo, guessThree, guessFour, guessFive, guessSix):
    printBoardSix(guessOne, guessTwo, guessThree, guessFour, guessFive)
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|",guessSix[0],"|  |",guessSix[1],"|  |",guessSix[2],"|  |",guessSix[3],"|  |",guessSix[4],"|")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

def checkForWin(userGuess, wordChosen):
    if userGuess == wordChosen:
        return 1;
    else:
        return 0;

def printWin(word):
    clearTerm()
    firstLet = greenColor + 'W' + whiteColor
    secondLet = greenColor + 'I' + whiteColor
    thirdLet = greenColor + 'N' + whiteColor
    word[0] = greenColor + word[0] + whiteColor
    word[1] = greenColor + word[1] + whiteColor
    word[2] = greenColor + word[2] + whiteColor
    word[3] = greenColor + word[3] + whiteColor
    word[4] = greenColor + word[4] + whiteColor
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|   |  |",firstLet,"|  |",secondLet,"|  |",thirdLet,"|  |   |")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|",word[0],"|  |",word[1],"|  |",word[2],"|  |",word[3],"|  |",word[4],"|")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

def printLose(word):
    clearTerm()
    firstLet = redColor + 'L' + whiteColor
    secondLet = redColor + 'O' + whiteColor
    thirdLet = redColor + 'S' + whiteColor
    fourthLet = redColor + 'E' + whiteColor
    fifthLet = redColor + 'R' + whiteColor
    word[0] = redColor + word[0] + whiteColor
    word[1] = redColor + word[1] + whiteColor
    word[2] = redColor + word[2] + whiteColor
    word[3] = redColor + word[3] + whiteColor
    word[4] = redColor + word[4] + whiteColor
    print("\n")
    print ("-----  -----  -----  -----  -----")
    print ("|",firstLet,"|  |",secondLet,"|  |",thirdLet,"|  |",fourthLet,"|  |",fifthLet,"|")
    print ("|   |  |   |  |   |  |   |  |   |")
    print ("|",word[0],"|  |",word[1],"|  |",word[2],"|  |",word[3],"|  |",word[4],"|")
    print ("-----  -----  -----  -----  -----")
    print("\n")
    print("\n")

