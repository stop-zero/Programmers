N=int(input())
axios=[]

for i in range(N):
    [x, y] = map(int, input().split())
    axios.append([y, x])
    
sorted_axios = sorted(axios)

for i in range(N):
    print(sorted_axios[i][1], sorted_axios[i][0])
