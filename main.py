from gameClass import *
from Funcs import *

gameState = 1
game = Pydle()

while (gameState == 1):

    # Prints title page
    game.clearTerm()
    startGame = printMenuScreen()

    if (startGame == "start"):
        if game.runGame() == 0:
            gameState = 0
            break
    elif (startGame == "rules"):
        game.clearTerm()
        print("The only rules are that there are no rules... and that this page is under construction!")
        gameState = 0;
        break
    elif (startGame == "exit"):
        game.clearTerm()
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
        