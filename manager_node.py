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
    data = pickle.dumps(gameBoard)
    sc.send(data)

def receiveState(sc):
    outputValue = sc.recv(BUFFER_SIZE)
    nextBoard = pickle.loads(outputValue)
    return nextBoard
