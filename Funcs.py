import os

greenColor = "\033[92m"
yellowColor = "\033[33m"
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
    else:
        print("This is not a valid word!")

def checkLetters(guess, userInput, wordChoices, charList):
    if (len(guess) == 5):
        wordReal(userInput, wordChoices)
        charsLeft = guess
        count = 0

        for letter in guess:
            if letter == charList[count]:
                guess[count] = greenColor + letter + whiteColor
                print(guess[count])
                count += 1
            else:
                guess[count] = letter
                print(guess[count])
                count += 1
        
        print("\n")
        count = 0
        
        # for letter in guess:
            #if letter in charList and letter != charList[count] and letter in charsLeft:
                #guess[count] = yellowColor + letter + whiteColor
                #print(guess[count])
                #count += 1
                #continue
            #else:
                #guess[count] = letter
                #print(guess[count])
                #count += 1
                #continue
    
    else:
        print("The entered word is not 5 characters long! Try Again")

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

