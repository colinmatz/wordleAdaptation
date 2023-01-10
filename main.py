from gameClass import *
from Funcs import *

gameState = 1
run = 1
gameMenu = Pydle()

while (gameState == 1):

    # Prints title page
    gameMenu.clearTerm()
    startGame = printMenuScreen()

    if (startGame == "start"):
        while run == 1:
            gameRun = Pydle()
            gameRun.runGame()
            replay = input("Would you like to play again? ('Y' or 'N'): ").upper()
            if replay == 'N':
                run = 0
                gameState = 0
                gameRun.clearTerm()
                print("Thank you for playing my Wordle adaptation!")
                break
    elif (startGame == "rules"):
        gameMenu.clearTerm()
        print("\nRule 1: You have to guess the Wordle in six goes or less.")
        print("Rule 2: Every word you enter must be a real word and must be included in the program's word list.")
        print("Rule 3: A correct letter in the correct spot turns \033[92mgreen\033[37m.")
        print("Rule 4: A correct letter in the wrong place turns \033[33myellow\033[37m.")
        print("Rule 5: An incorrect letter remains gray.")
        print("Rule 6: Letters can be used more than once.")
        input("\nPress Enter to return to the menu! ")
        continue
    elif (startGame == "exit"):
        gameMenu.clearTerm()
        print("Thank you for trying my Wordle adaptation!")
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
        