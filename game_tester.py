import game_logic
import unittest


class TestGameLogic(unittest.TestCase):

    def test_game_beginning(self):
        testBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        testGame = game_logic.TicTacToe(testBoard)
        testGame.moveAI()
        self.assertEqual(testGame.boardList[1][1], 2)

    # TODO: FIX THIS
    def test_prevent_enemy_winning(self):
        testBoard = [
            [0, 1, 0],
            [0, 0, 1],
            [2, 2, 1]
        ]
        testGame = game_logic.TicTacToe(testBoard)
        testGame.moveAI()
        print("\n")
        for row in testBoard:
            print(row)
        self.assertEqual(testGame.boardList[0][2], 2)

    def test_ai_can_win(self):
        testBoard = [
            [1, 2, 0],
            [0, 2, 2],
            [1, 0, 1]
        ]
        testGame = game_logic.TicTacToe(testBoard)
        testGame.moveAI()
        self.assertEqual(testGame.boardList[1][0], 2)

    def test_end_game_with_win(self):
        testBoard = [
            [1, 2, 1],
            [1, 2, 2],
            [2, 0, 1]
        ]
        testGame = game_logic.TicTacToe(testBoard)
        testGame.moveAI()
        self.assertEqual(testGame.boardList[2][1], 2)

    def test_end_game_with_tie(self):
        testBoard = [
            [2, 1, 2],
            [1, 1, 2],
            [0, 2, 1]
        ]
        testGame = game_logic.TicTacToe(testBoard)
        testGame.moveAI()
        self.assertEqual(testGame.boardList[2][0], 2)

# def main():
#     exampleBoard = [
#         [2, 1, 2],
#         [1, 2, 1],
#         [1, 0, 2]
#     ]

#     exampleGame = game_logic.TicTacToe(exampleBoard)
#     exampleGame.moveAI()
#     for row in exampleGame.boardList:
#         print(row)


if __name__ == "__main__":
    unittest.main()
