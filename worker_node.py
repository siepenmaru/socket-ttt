import socket
import threading
import pickle
import game_logic
from typing import Tuple

SERVER_NAME = ""
SERVER_PORT = 4321
BUFFER_SIZE = 1024


def socketHandler(connection: socket.socket, address: Tuple[str, int]):
    # Handles sockets
    print(f"Incoming connection from {address}")

    # Receives input from player in the form of 2d list, representing the game board
    while True:
        inputValue = connection.recv(BUFFER_SIZE)
        if inputValue == b'':
            connection.close()
        else:
            gameBoard = pickle.loads(inputValue)
            print(f"Input from {address}: {inputValue}")

            outputValue = logic(gameBoard)
            data = pickle.dumps(outputValue)
            connection.send(data)


def logic(board: list):
    # tic-tac-toe game logic
    ticTacToe = game_logic.TicTacToe(board)
    ticTacToe.moveAI()
    return ticTacToe.boardList


def main():
    # init program
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.bind((SERVER_NAME, SERVER_PORT))
        sc.listen(0)

        print("Program running...")
        print("Terminate with Ctrl+C")

        while True:
            connection, address = sc.accept()

            thread = threading.Thread(target=socketHandler, args=(connection, address))
            thread.start()


if __name__ == "__main__":
    main()
