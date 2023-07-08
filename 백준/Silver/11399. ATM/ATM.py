N=int(input())
t=list(map(int, input().split()))
t.sort()
result = 0

for i in range(N):
    result += t[i]*(N-i)

print(result)