# 그리디 알고리즘
N=int(input())
cnt=0

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        break
    N -= 3
    cnt += 1
else:
    cnt = -1

print(cnt)