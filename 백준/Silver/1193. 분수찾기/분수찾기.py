def result(x):
    cnt = 1
    while x > cnt:
        x -= cnt
        cnt += 1
    
    if cnt % 2 == 0:
        a = x
        b = cnt - x + 1
    else:
        a = cnt - x + 1
        b = x
    
    return f"{a}/{b}"

X = int(input())

print(result(X))

# 각 대각선(cnt)마다 분자(a)와 분모(b)의 합 일정. 
# 첫 번째 대각선은 합이 2, 두 번째 대각선은 합이 3, 세 번째 대각선은 합이 4, ..., n번째 대각선은 합 n+1
# 짝수 대각선의 경우 분자는 증가하고 분모는 감소. 홀수 대각선의 경우 분자는 감소하고 분모는 증가.
