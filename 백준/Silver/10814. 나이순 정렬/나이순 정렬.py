import sys
N = int(sys.stdin.readline())
info = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    info.append([int(age), name])

info.sort(key=lambda x:int(x[0]))

for i in info:
    print(i[0],i[1])