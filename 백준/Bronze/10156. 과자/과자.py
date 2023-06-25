# 과자 한 개의 가격 K
# 과자 개수 N
# 가진 돈 M
# 모자란 돈 구하기
N, K, M = map(int, input().split())

result = K*N-M
if result>0:
    print(result)   
else: 
    print(0)