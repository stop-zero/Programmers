sum=int(input())
type=int(input())
result = 0

for i in range(type):
    a, b = map(int, input().split())
    result += a* b

if sum==result:
    print("Yes")
else:
    print("No")