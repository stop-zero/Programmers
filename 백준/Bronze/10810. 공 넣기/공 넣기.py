N, M = map(int, input().split())
b = [0]*N #공이 없는 바구니는 0으로 출력
 
for _ in range(M):
        i, j, k = map(int, input().split())
        for x in range(i , j+1):
            b[x-1]=k
            
for x in range(N):
    print(b[x], end=' ')