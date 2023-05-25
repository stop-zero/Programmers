T = int(input())

for _ in range(T):
    n = int(input()) 
    positions = [] 

    index = 0
    while n > 0:
        if n % 2 == 1:
            positions.append(index)
        n //= 2
        index += 1
    
    print(' '.join(map(str, positions)))  
