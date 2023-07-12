N = int(input())

M = N
cnt = 0

while True:
    A = N // 10
    B = N % 10
    N = 10*B + (A+B)%10
    cnt += 1
    
    if N == M:
        break
print(cnt)