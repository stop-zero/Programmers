# 유클리드 호제법
# 큰 수 % 작은 수 나머지가 0이 아니면 나머지가 작은 수로
# 나머지가 0이면 작은 수가 최대공약수

N, M = map(int, input().split())
n, m = N, M
         
# 유클리드 > 최대공약수
while m != 0:
    n, m = m, n % m
gcd = n

# 최소공배수
lcm = N * M // gcd

print(gcd)
print(lcm)