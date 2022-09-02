import random

print("Oxo Game for nalios_technical_test")

case = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameInterface = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

print("You = X, Bot = O")


# print the grid
def printGameInterface():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameInterface[x][y], end=" |")
    print("\n+---+---+---+")


def putSymbolInArray(num, attempt):
    num -= 1
    if (num == 0):
        gameInterface[0][0] = attempt
    elif (num == 1):
        gameInterface[0][1] = attempt
    elif (num == 2):
        gameInterface[0][2] = attempt
    elif (num == 3):
        gameInterface[1][0] = attempt
    elif (num == 4):
        gameInterface[1][1] = attempt
    elif (num == 5):
        gameInterface[1][2] = attempt
    elif (num == 6):
        gameInterface[2][0] = attempt
    elif (num == 7):
        gameInterface[2][1] = attempt
    elif (num == 8):
        gameInterface[2][2] = attempt


# check who is the winner
def checkForWinner(interface):
    ### Win vertical direction
    if gameInterface[0][0] == 'X' and gameInterface[0][1] == 'X' and gameInterface[0][2] == 'X':
        print("X is the winner !")
        return "X"
    elif gameInterface[0][0] == 'O' and gameInterface[0][1] == 'O' and gameInterface[0][2] == 'O':
        print("O is the winner !")
        return "O"
    elif gameInterface[1][0] == 'X' and gameInterface[1][1] == 'X' and gameInterface[1][2] == 'X':
        print("X is the winner !")
        return "X"
    elif gameInterface[1][0] == 'O' and gameInterface[1][1] == 'O' and gameInterface[1][2] == 'O':
        print("O is the winner !")
        return "O"
    elif gameInterface[2][0] == 'X' and gameInterface[2][1] == 'X' and gameInterface[2][2] == 'X':
        print("X is the winner !")
        return "X"
    elif gameInterface[2][0] == 'O' and gameInterface[2][1] == 'O' and gameInterface[2][2] == 'O':
        print("O is the winner !")
        return "O"
    ### Win horizontal direction
    if gameInterface[0][0] == 'X' and gameInterface[1][0] == 'X' and gameInterface[2][0] == 'X':
        print("X is the winner !")
        return "X"
    elif gameInterface[0][0] == 'O' and gameInterface[1][0] == 'O' and gameInterface[2][0] == 'O':
        print("O is the winner !")
        return "O"
    elif gameInterface[0][1] == 'X' and gameInterface[1][1] == 'X' and gameInterface[2][1] == 'X':
        print("X is the winner !")
        return "X"
    elif gameInterface[0][1] == 'O' and gameInterface[1][1] == 'O' and gameInterface[2][1] == 'O':
        print("O is the winner !")
        return "O"
    elif gameInterface[0][2] == 'X' and gameInterface[1][2] == 'X' and gameInterface[2][2] == 'X':
        print("X is the winner !")
        return "X"
    elif gameInterface[0][2] == 'O' and gameInterface[1][2] == 'O' and gameInterface[2][2] == 'O':
        print("O is the winner !")
        return "O"
    # Win in diagonal
    elif gameInterface[0][0] == 'X' and gameInterface[1][1] == 'X' and gameInterface[2][2] == 'X':
        print("X is the winner !")
        return "X"
    elif gameInterface[0][0] == 'O' and gameInterface[1][1] == 'O' and gameInterface[2][2] == 'O':
        print("O is the winner !")
        return "O"
    elif gameInterface[0][2] == 'X' and gameInterface[1][1] == 'X' and gameInterface[2][0] == 'X':
        print("X is the winner !")
        return "X"
    elif gameInterface[0][2] == 'O' and gameInterface[1][1] == 'O' and gameInterface[2][0] == 'O':
        print("O is the winner !")
        return "O"
    else:
        return "N"


def turn(game):
    loop = False
    turnCounter = 0

    while loop == False:
        # It's my turn
        if turnCounter % 2 == 0:
            game()
            input_number = int(input("\nChoose a number between 1 and 9: "))
            if input_number >= 1 or input_number <= 9:
                putSymbolInArray(input_number, 'X')
                case.remove(input_number)
            else:
                print("Invalid input. Choose a number between 1 and 9:")
            turnCounter += 1
        # It's the bot_player turn
        else:
            while True:
                bot_player = random.choice(case)
                print("\nBot Choose: ", bot_player)
                if bot_player in case:
                    putSymbolInArray(bot_player, 'O')
                    case.remove(bot_player)
                    turnCounter += 1
                    break

        winner = checkForWinner(gameInterface)
        if winner != "N":
            print("\nGood bye")
            break


turn(printGameInterface)
