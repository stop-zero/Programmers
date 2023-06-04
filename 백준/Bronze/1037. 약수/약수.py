n = int(input())  # 진짜 약수의 개수 입력
divisors = list(map(int, input().split()))  # 진짜 약수들 입력

min_divisor = min(divisors)  # 가장 작은 값
max_divisor = max(divisors)  # 가장 큰 값

n = min_divisor * max_divisor  # N 구하기

print(n)
