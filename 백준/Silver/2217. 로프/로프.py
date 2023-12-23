def max_weight_possible(N, ropes):
    ropes.sort() 
    max_weight = 0

    for i in range(N):
        weight = ropes[i] * (N - i)  
        max_weight = max(max_weight, weight)

    return max_weight

N = int(input()) 
ropes = []
for _ in range(N):
    ropes.append(int(input()))  

print(max_weight_possible(N, ropes))
