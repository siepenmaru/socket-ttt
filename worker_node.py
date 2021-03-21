import socket
import threading
import game_logic
from typing import Tuple

SERVER_NAME = ""
SERVER_PORT = 4321
BUFFER_SIZE = 1024


def socketHandler(connection: socket.socket, address: Tuple[str, int]):
    # Handles sockets
    print(f"Incoming connection from {address}")

    # Receives input from player in the form of 2d list, representing the game board
    input_value = connection.recv(BUFFER_SIZE)
    print(f"Input from {address}: {input_value}")

    output_value = logic(input_value)
    connection.send(output_value)


def logic(board: list):
    # tic-tac-toe game logic
    ticTacToe = game_logic.TicTacToe(board)
    return ticTacToe.getNextMove()


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