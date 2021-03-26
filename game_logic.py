from math import inf as infinity


class TicTacToe:
    """
    Game logic for tic tac toe
    Processes state of board, then returns next move by computer
    """
    def __init__(self, boardList):
        """
        2D List of ints
        0: Not filled
        1: Player
        2: AI
        [x axis][y axis]
        """
        self.boardList = boardList

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
            # Check if player occupies all the positions in a win condition
            if [player, player, player] == winCondition:
                return True

        return False

    def checkGameOver(self):
        # Check if game is over
        return self.checkWin(1) or self.checkWin(2)

    def getScore(self, depth):
        """
        Heuristic value of the current node (board)
        1 if AI wins, -1 if player wins, 0 if tie
        """
        if self.checkWin(2):
            return depth - 1
        elif self.checkWin(1):
            return 1 - depth
        else:
            return 0

    def getEmptySquares(self):
        """
        Returns squares which have not been occupied by a player
        2D array of the x, y position
        """
        emptySquares = []
        for x, row in enumerate(self.boardList):
            for y, square in enumerate(row):
                if square == 0:
                    emptySquares.append([x, y])
        return emptySquares

    def minimax(self, depth, player):
        """
        Minimax function for the game
        Returns heuristic value of the board and position
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
                value = min(value, self.minimax(depth - 1, 2))
                self.boardList[square[0]][square[1]] = 0
            return value

    def getNextMove(self):
        """
        Get next move for AI.
        Returns next optimal position
        """
        value = -infinity
        nextMove = [-1, -1]
        depth = len(self.getEmptySquares())

        # AI moves first at game start
        if depth == 9:
            nextMove = [1, 1]
        else:
            # Exhaust all possible moves
            for x in range(3):
                for y in range(3):
                    if self.boardList[x][y] == 0:
                        self.boardList[x][y] = 2
                        # Calculate heuristic value of the board after move
                        newValue = self.minimax(depth, 1)
                        self.boardList[x][y] = 0

                        # Set new move if optimal
                        if newValue > value:
                            nextMove = [x, y]
                            value = newValue

        return nextMove

    def moveAI(self):
        """
        AI ticks the board with the next optimal move
        """
        nextMove = self.getNextMove()
        x = nextMove[0]
        y = nextMove[1]
        self.boardList[x][y] = 2
