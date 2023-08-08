def count(lst):
    cnt = ans = 1
    for i in range(1, len(lst)):
        if lst[i]==lst[i-1]:
            cnt+=1
            ans = max(ans, cnt)
        else:
            cnt=1
    return ans

# 행과 열에서 연속된 같은 사탱의 최대 개수 
def solve(arr):
    mx = 0
    for i in range(N-1):
        for j in range(0,N):
            # 오른쪽 사탕과 교환
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
            mx = max(mx, count(arr[i]))
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]

            # 아래쪽 사탕과 교환
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j]
            mx = max(mx, count(arr[i]),count(arr[i+1]))
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j]
    return mx

N = int(input())
arr = [list(input())+[0] for _ in range(N)]+[[0]*(N+1)] # 정사각형 그리드의 크기 
arr_t = list(map(list, zip(*arr)))  # 사탕의 색상을 나타내는 문자열 리스트
ans = max(solve(arr), solve(arr_t)) # 연속된 같은 사탕의 최대 개수 계산
print(ans)