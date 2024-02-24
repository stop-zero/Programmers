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
