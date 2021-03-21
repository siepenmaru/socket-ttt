import game_logic


def main():
    exampleBoard = [
        [0, 1, 2],
        [0, 1, 0],
        [0, 0, 2]
    ]

    exampleGame = game_logic.TicTacToe(exampleBoard)
    exampleGame.moveAI
    print(exampleGame.boardList)


if __name__ == "__main__":
    main()