def min_coin_count(n):
    count = n // 5
    
    remainder = n % 5
    
    while count >= 0:
        if remainder % 2 == 0:
            count += remainder // 2
            return count
        
        count -= 1
        remainder += 5

    return -1 

n = int(input())

print(min_coin_count(n))
