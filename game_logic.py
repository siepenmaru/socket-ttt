from math import inf as infinity


class TicTacToe:
    def __init__(self, boardList):
        """
        2D List of ints
        0: Not filled
        1: Player
        2: AI
        [x axis][y axis]
        """
        self.boardList = boardList
        print("initialized")

    def checkWin(self, player):
        winConditions = [
            # 3 in a Column
            [self.boardList[0][0], self.boardList[0][1], self.boardList[0][2]],
            [self.boardList[1][0], self.boardList[1][1], self.boardList[1][2]],
            [self.boardList[2][0], self.boardList[2][1], self.boardList[2][2]],
            # 3 in a Row
            [self.boardList[0][0], self.boardList[1][0], self.boardList[2][0]],
            [self.boardList[0][1], self.boardList[1][1], self.boardList[2][1]],
            [self.boardList[0][2], self.boardList[1][2], self.boardList[2][2]],
            # 3 in a Diagonal
            [self.boardList[0][0], self.boardList[1][1], self.boardList[2][2]],
            [self.boardList[2][0], self.boardList[1][1], self.boardList[0][2]]
        ]

        for winCondition in winConditions:
            if [player, player, player] == winCondition:
                return True

        return False

    def checkGameOver(self):
        # check if game is over
        return self.checkWin(1) or self.checkWin(2)

    def getScore(self, depth):
        # Heuristic value of the current node (board)
        if self.checkWin(2):
            return 1
        elif self.checkWin(1):
            return -1
        else:
            return 0

    def getEmptySquares(self):
        emptySquares = []
        for x, row in enumerate(self.boardList):
            for y, row in enumerate(self.boardList):
                emptySquares.append([x, y])
        return emptySquares

    def minimax(self, depth, player):
        """
        Minimax function for the game
        Returns heuristic value of the board
        depth: number of iterations left until terminal node (game over)
        player: current player (player 1 vs ai 2)
        """

        # On a terminal node (end of game), get score
        if self.checkGameOver() or depth == 0:
            return self.getScore(depth)

        # Maximize score for AI moves
        if player == 2:
            value = -infinity
            for square in self.getEmptySquares():
                self.boardList[square[0]][square[1]] = 2
                value = max(value, self.minimax(depth - 1, 1))
                self.boardList[square[0]][square[1]] = 0
            return value
        # Minimize score for player moves
        else:
            value = infinity
            for square in self.getEmptySquares():
                self.boardList[square[0]][square[1]] = 1
                value = min(value, self.minimax(square, depth - 1, 2))
                self.boardList[square[0]][square[1]] = 0
            return value

    def getNextMove(self):
        value = -infinity
        nextMove = [-1, -1]
        depth = len(self.getEmptySquares())
        print(f"value: {value}")

        if depth == 0 or self.checkGameOver():
            return
        if depth == 9:
            nextMove = [1, 1]
        else:
            for x in range(3):
                for y in range(3):
                    position = self.boardList[x][y]
                    if position == 0:
                        position = 2
                        newValue = self.minimax(depth, 1)
                        print(f"newValue: {newValue}")
                        
                        position = 0

                        if newValue > value:
                            nextMove = [x, y]
                            value = newValue
                            print(f"value: {value}")

        return nextMove

    def moveAI(self):
        print("moveAI")
        nextMove = self.getNextMove()
        x = nextMove[0]
        y = nextMove[1]
        self.boardList[x][y] = 2


def main():
    exampleBoard = [
        [0, 1, 2],
        [0, 1, 0],
        [0, 0, 2]
    ]

    exampleGame = TicTacToe(exampleBoard)
    exampleGame.moveAI()
    for row in exampleGame.boardList:
        print(row)


if __name__ == "__main__":
    main()
