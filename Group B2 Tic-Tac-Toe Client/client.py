import manager_node as manager
from pretty_text import PrettyText as pt

"""
Client-side CLI Game Implementation
Uses manager node to communicate with server
"""


def checkWinState(boardList):
    """
    Check if there are any winners on the board
    1: Player wins
    2: AI wins
    0: No winner
    """
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
    """
    Check if there are remaining empty squares on the board
    """
    hasEmpty = False
    for row in boardList:
        for square in row:
            if square == 0:
                hasEmpty = True
    return hasEmpty


def printBoard(boardList, playerSymbol, aiSymbol, colorsOn):
    """
    Display board in CLI
    """
    border = "-----------"
    for x, row in enumerate(boardList):
        display = ''    # Row string
        for y, square in enumerate(row):
            ch = ''

            # Mark symbol on the board
            if square == 0:
                ch = f"{ y+1 + (3*(x)) }"
            elif square == 1:
                if colorsOn:
                    ch = pt.BOLD + pt.BLUE + playerSymbol + pt.END
                else:
                    ch = playerSymbol
            else:
                if colorsOn:
                    ch = pt.BOLD + pt.RED + aiSymbol + pt.END
                else:
                    ch = aiSymbol

            # Append to row string
            if y == 0:
                display += f" {ch}"
            elif y == 1:
                display += f" | {ch} | "
            elif y == 2:
                display += f"{ch} "

        print(display)
        if x != 2:
            print(border)


def chooseColor():
    """
    Enable or disable terminal colors
    Terminals must support ANSI escape codes for colors
    """
    answer = input("Enable colors? (Windows cmd unsupported) (y/n): ")
    if answer.upper() == "Y":
        return True
    if answer.upper() == "N":
        return False
    else:
        print("Invalid response!")
        return chooseColor()


def chooseSymbol():
    """
    Player chooses their symbol
    """
    symbolDict = {0: "X", 1: "O", 2: "X"}
    playerSymbol = -1
    print("Choose a symbol: ")
    print("1: O")
    print("2: X")

    try:
        playerSymbol = int(input(""))
    except ValueError:
        pass

    if playerSymbol in [1, 2]:
        return [symbolDict.get(playerSymbol), symbolDict.get(playerSymbol-1)]
    else:
        print("Invalid input!")
        return chooseSymbol()


def chooseGoFirst():
    """
    Player chooses who goes first
    """
    answer = input("Do you want to go first? (y/n): ")
    if answer.upper() == "Y":
        return True
    if answer.upper() == "N":
        return False
    else:
        print("Invalid response!")
        return chooseGoFirst()


def getPlayerMove(gameBoard):
    """
    Marks position on game board for player
    """
    position = int(input("Which square would you like to pick? (1-9): "))
    positionDict = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2]
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
    socket = manager.establishConnection()  # Establish connection with worker node
    while running:
        gameBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        print(f"\n{40*'='}")
        print("Group B2\'s \"Unbeatable\" Tic-Tac-Toe Game")
        print(f"{40*'='}")

        colorsOn = chooseColor()

        # [0]: player symbol, [1]: AI symbol
        symbols = chooseSymbol()
        print(f"Now playing as {symbols[0]}...")

        if chooseGoFirst():
            printBoard(gameBoard, symbols[0], symbols[1], colorsOn)
            gameBoard = getPlayerMove(gameBoard)

        try:
            manager.sendState(socket, gameBoard)
            gameBoard = manager.receiveState(socket)
        except EOFError:
            manager.closeConnection(socket)
            return

        printBoard(gameBoard, symbols[0], symbols[1], colorsOn)

        # Game is running
        while checkWinState(gameBoard) == 0 and hasEmptySquares(gameBoard):
            gameBoard = getPlayerMove(gameBoard)

            if checkWinState(gameBoard) != 0:
                printBoard(gameBoard, symbols[0], symbols[1], colorsOn)
                break

            try:
                manager.sendState(socket, gameBoard)
                gameBoard = manager.receiveState(socket)
            except EOFError:
                manager.closeConnection(socket)
                return

            printBoard(gameBoard, symbols[0], symbols[1], colorsOn)

        if checkWinState(gameBoard) == 0:
            print("It's a Tie!")
        elif checkWinState(gameBoard) == 1:
            print("You Win! Wait.. How did you do that?")
        else:
            print("Computer Wins! Truth is, the game was rigged from the start..")

        goAgain = input("Go again? (y/n): ")
        if goAgain.upper() == "N":
            print("See you next time!")
            running = False
    manager.closeConnection(socket)


if __name__ == "__main__":
    main()
