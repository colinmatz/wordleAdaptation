
def printMenuScreen():
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

    return startGame