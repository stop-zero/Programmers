T = int(input())

for _ in range(T):
    n = int(input())
    position = 0
    positions = []
    
    while n > 0:
        if n % 2 == 1:
            positions.append(position)
        n = n // 2
        position += 1
    
    print(" ".join(map(str, positions)))