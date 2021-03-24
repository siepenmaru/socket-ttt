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
    listening = True
    try:
        # Timeout after 45 seconds of not receiving any input
        connection.settimeout(45)
        while listening:
            inputValue = connection.recv(BUFFER_SIZE)
            if inputValue == b'':
                print(f"Closing connection with {address}")
                connection.close()
                listening = False
            else:
                gameBoard = pickle.loads(inputValue)
                print(f"Input from {address}: {gameBoard}")

                outputValue = logic(gameBoard)
                data = pickle.dumps(outputValue)
                connection.send(data)
    except socket.timeout:
        print(f"Connection with {address} timed out")
        connection.close()


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

        try:
            while True:
                connection, address = sc.accept()

                thread = threading.Thread(target=socketHandler, args=(connection, address))
                thread.start()
        except KeyboardInterrupt:
            print("\nTerminating program.")


if __name__ == "__main__":
    main()
