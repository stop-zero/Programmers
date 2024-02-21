import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if len(self.stack) == 0 else 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]

N = int(sys.stdin.readline())
stack = Stack()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        sys.stdout.write(str(stack.pop()) + '\n')
    elif command[0] == 'size':
        sys.stdout.write(str(stack.size()) + '\n')
    elif command[0] == 'empty':
        sys.stdout.write(str(stack.empty()) + '\n')
    elif command[0] == 'top':
        sys.stdout.write(str(stack.top()) + '\n')
