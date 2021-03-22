import manager_node as manager


def checkWinState(boardList):
    winConditions = [
            # 3 in a Column
            [boardList[0][0], boardList[0][1], boardList[0][2]],
            [boardList[1][0], boardList[1][1], boardList[1][2]],
            [boardList[2][0], boardList[2][1], boardList[2][2]],
            # 3 in a Row
            [boardList[0][0], boardList[1][0], boardList[2][0]],
            [boardList[0][1], boardList[1][1], boardList[2][1]],
            [boardList[0][2], boardList[1][2], boardList[2][2]],
            # 3 in a Diagonal
            [boardList[0][0], boardList[1][1], boardList[2][2]],
            [boardList[2][0], boardList[1][1], boardList[0][2]]
        ]

    for winCondition in winConditions:
        # Check if player occupies all the positions in a win condition
        if winCondition == [1, 1, 1]:
            return 1
        if winCondition == [2, 2, 2]:
            return 2

    return 0

def hasEmptySquares(boardList):
    hasEmpty = False
    for row in boardList:
        for square in row:
            if square == 0:
                hasEmpty = True
    return hasEmpty

def printBoard(boardList, playerSymbol, aiSymbol):
    border = "-----------"
    for x, row in enumerate(boardList):
        display = ''
        for y, square in enumerate(row):
            ch = ''
            if square == 0:
                ch = f"{ y+1 + (3*(x)) }"
            elif square == 1:
                ch = playerSymbol
            else:
                ch = aiSymbol

            if y == 0:
                display += f" {ch}"
            elif y == 1:
                display += f" | {ch} | "
            elif y == 2:
                display += f"{ch} "
        print(display)
        if x != 2:
            print(border)

def chooseSymbol():
    symbolDict = {0: "X", 1: "O", 2: "X"}
    print("Choose a symbol: ")
    print("1: O")
    print("2: X")
    playerSymbol = int(input(""))
    if playerSymbol in [1, 2]:
        return [symbolDict.get(playerSymbol), symbolDict.get(playerSymbol-1)]
    else:
        print("Invalid input!")
        return chooseSymbol()

def chooseGoFirst():
    answer = input("Do you want to go first? (y/n)")
    if answer.upper() == "Y":
        return True
    if answer.upper() == "N":
        return False
    else:
        print("Invalid response!")
        return chooseGoFirst()

def getPlayerMove(gameBoard):
    position = int(input("Which square would you like to pick? (1-9)"))
    positionDict = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2]
    }
    position = positionDict.get(position)
    if gameBoard[position[0]][position[1]] == 0:
        gameBoard[position[0]][position[1]] = 1
        return gameBoard
    else:
        print("Invalid square!")
        return getPlayerMove(gameBoard)

def main():
    running = True
    socket = manager.establishConnection()
    while running:
        gameBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        print(f"\n{38*'='}")
        print("Group B2\'s Unbeatable Tic-Tac-Toe Game")
        print(f"\n{38*'='}")

        # [0]: player symbol, [1]: AI symbol
        symbols = chooseSymbol()
        print(f"Now playing as {symbols[0]}...")
        if chooseGoFirst():
            printBoard(gameBoard, symbols[0], symbols[1])
            gameBoard = getPlayerMove(gameBoard)
            manager.sendState(socket, gameBoard)
            gameBoard = manager.receiveState(socket)
            printBoard(gameBoard, symbols[0], symbols[1])
        else:
            manager.sendState(socket, gameBoard)
            gameBoard = manager.receiveState(socket)
            printBoard(gameBoard, symbols[0], symbols[1])
        
        while checkWinState(gameBoard) == 0 and hasEmptySquares(gameBoard):
            gameBoard = getPlayerMove(gameBoard)

            manager.sendState(socket, gameBoard)
            gameBoard = manager.receiveState(socket)

            printBoard(gameBoard, symbols[0], symbols[1])
        
        if checkWinState(gameBoard) == 0:
            print("It's a Tie!")
        elif checkWinState(gameBoard) == 1:
            print("You Win! Wait.. How did you do that?")
        elif checkWinState(gameBoard) == 2:
            print("Computer Wins! Truth is, the game was rigged from the start..")

        goAgain = input("Go again? (y/n)")
        if goAgain.upper() == "N":
            running = False


if __name__ == "__main__":
    main()
