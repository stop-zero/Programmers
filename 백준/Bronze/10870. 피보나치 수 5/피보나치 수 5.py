n= int(input())

# 피보나치 수열? => 재귀 사용
def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# n번째 피보나치 수 계산
result = fibonacci(n)
print(result)
