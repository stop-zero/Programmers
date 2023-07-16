N=int(input())

axios=[]
for i in range(N):
    [x, y] = map(int, input().split())
    axios.append([x,y])
    
# sorted_axios = sorted(axios, key=lambda p:(p[0], p[1]))
sorted_axios = sorted(axios)

for i in range(N):
    print(sorted_axios[i][0], sorted_axios[i][1])
