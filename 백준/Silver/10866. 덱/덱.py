# push_front, push_back, pop_front, pop_back, size, empty, front, back 연산 수행
from collections import deque
import sys

N = int(input())
deq = deque()

def process(command):
    if command[0] == "push_front":
        deq.appendleft(command[1])
    elif command[0] == "push_back":
        deq.append(command[1])
    elif command[0] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deq))
    elif command[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif command[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    process(command)
    
