N = int(input()) 
arr = list(map(int, input().split()))  
M = int(input()) 
targets = list(map(int, input().split()))  

arr_set = set(arr)

for target in targets:
    if target in arr_set:
        print(1)
    else:
        print(0)
