# Group B2
Socket Programming assignment from members of Group B2 in Computer Networks 2020-2021 Even course.

## Our Application
A tic-tac-toe game implementing Minimax Adversarial Search

## Group B2 Members
- Al Taaj Kautsar Supangkat - 1906426746
- Avatar Putra Pertama Azka - 1906426802
- Seto Adhi Prasetyo - 1906426960

## Requirements / Dependencies
- Python 3.7.3 or later
- Terminal Emulator (Must support ANSI escape codes for colored mode)
- An internet connection

## Execution Instructions
**For Client**
1. Download the folder Group B2 Tic-Tac-Toe Client
2. Navigate your preferred terminal emulator to the folder
3. Run the client program with `python3 client.py`
4. Enjoy the game!

## How To Play The Game
1. Choose if you want to play with colored symbols (terminal must support ANSI escape codes)
2. Choose a symbol to play with (X or O)
3. Choose if you want to go first
4. Choose which square you would like to place your symbol on (squares are indexed 1 - 9)
5. The first player who gets 3 of their own symbols in a row, column, or diagonal wins the game.

## Implemented Features
- [x] Implement a program for a manager node which can receive tasks from the user. In this case, the manager node will be the local machine of the user itself.
- [x] Implement a program for worker node(s) and which can receive tasks from the manager node and process the tasks. In this case, use Compute Engine instance(s) as the worker node(s). The worker node(s) must be able to work in multithreaded mode.
- [x] Implement a socket-based communication system between manager and worker nodes so that tasks can be sent and received.
- [x] Implement a mechanism to limit the number of tasks running in a worker node. A worker node should queue tasks if the number of currently active tasks exceed that limitation. You can use the FCFS algorithm for this.
- [x] Implement a mechanism to limit the size of a worker node’s queue. If the queue is full, the worker node should refuse tasks from the manager node.
- [x] Implement an auto-downscaling mechanism in which worker node(s) that are idle for too long can be shut down to save resource.
