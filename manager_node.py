import socket
import pickle

# NOTE: this is a local ip for testing. change this when switching to GVM
SERVER_IP = "127.0.0.1"
SERVER_PORT = 4321
BUFFER_SIZE = 1024

def establishConnection():
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((SERVER_IP, SERVER_PORT))
    return sc

def closeConnection(sc):
    print("Closing connection...")
    sc.close()

def sendState(sc, gameBoard):
    print("Current board: ")
    for row in gameBoard:
        print(row)
    print("Sending the board to the server...")

    data = pickle.dumps(gameBoard)
    sc.send(data)

def receiveState(sc):
    outputValue = sc.recv(BUFFER_SIZE)
    nextBoard = pickle.loads(outputValue)
    print("New board state: ")
    for row in nextBoard:
        print(row)
    return nextBoard

def main():
    """
    GUI program
    stay on while user has not quit
    establish connection to server
    every time player moves, send and recv
    close connection when program ends
    """
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((SERVER_IP, SERVER_PORT))

    exampleBoard = [
        [1, 2, 0],
        [0, 2, 2],
        [1, 0, 1]
    ]

    print("Tic-Tac-Toe Client Tester")
    print("Current board: ")
    for row in exampleBoard:
        print(row)
    print("Sending the board to the server...")

    data = pickle.dumps(exampleBoard)
    sc.send(data)

    outputValue = sc.recv(BUFFER_SIZE)
    nextBoard = pickle.loads(outputValue)
    print("New board state: ")
    for row in nextBoard:
        print(row)

    print("Closing connection...")
    sc.close()


if __name__ == "__main__":
    main()
