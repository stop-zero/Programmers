from collections import deque
import sys

N = int(input())
queue = deque()

def function(command):
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    function(command)
