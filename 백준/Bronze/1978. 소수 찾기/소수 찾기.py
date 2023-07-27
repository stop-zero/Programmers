# 소수 : 약수가 1과 자기 자신만 있는 애들
# 소수 찾기 : 1~N까지 나눴을 때 하나라도 나누어 떨어지지 않으면 소수 

N=int(input())
Number = map(int, input().split())
cnt = 0

for i in Number:
    for j in range(2, i+1):
        if i%j == 0:
            if i == j:
                cnt += 1
            break
    
print(cnt)