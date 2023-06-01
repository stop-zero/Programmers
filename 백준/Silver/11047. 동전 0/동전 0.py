N, K = map(int, input().split()) 

count = 0
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

for coin in coins:
    if K >= coin:
        count += K // coin
        K %= coin 
        if K <= 0: 
       		break
            
print(count) 