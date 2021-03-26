# Group B2

Socket Programming assignment from members of Group B2 in Computer Networks 2020-2021 Even course.

## Our Application
A tic-tac-toe game implementing Minimax Adversarial Search

## Implemented Features
- [x] Implement a program for a manager node which can receive tasks from the user. In this case, the manager node will be the local machine of the user itself.
- [x] Implement a program for worker node(s) and which can receive tasks from the manager node and process the tasks. In this case, use Compute Engine instance(s) as the worker node(s). The worker node(s) must be able to work in multithreaded mode.
- [x] Implement a socket-based communication system between manager and worker nodes so that tasks can be sent and received.
- [x] Implement an auto-downscaling mechanism in which worker node(s) that are idle for too long can be shut down to save resource.