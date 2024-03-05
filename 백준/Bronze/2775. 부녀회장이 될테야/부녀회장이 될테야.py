def people(k, n):
    zero = [i for i in range(1, n+1)]
   
    for _ in range(k):
        for i in range(1, n):
            zero[i] += zero[i-1]
    return zero[n-1]

T = int(input())

for _ in range(T):
    k = int(input())  # 층 수 
    n = int(input())  # 호 수 
    print(people(k, n))  # 사람 수 
