import socket
import pickle

"""
NOTE: Mandatory Feature 1
Manager Node functionality
"""

# NOTE: GVM Static IP Address
SERVER_IP = "35.224.229.170"
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
    data = pickle.dumps(gameBoard)
    sc.send(data)


def receiveState(sc):
    try:
        outputValue = sc.recv(BUFFER_SIZE)
        nextBoard = pickle.loads(outputValue)
        return nextBoard
    except EOFError:
        print("Sorry! Connection with server refused. Try again later.")
        raise
