# N개의 바구니 M번 공을 바꿀 거 보자마자 든 생각 tmp?
N, M = map(int, input().split())
b = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = b[i - 1]
    b[i - 1] = b[j - 1]
    b[j - 1] = tmp
 #   b[i], b[j] = b[j], b[i]

#result = ' '.join(map(str, b[1:])) #1~N번까지 번호를 문자열로 변환
#print(result) # 런타임 에러남 왜인지..

for x in b:
     print(x, end=" ")
