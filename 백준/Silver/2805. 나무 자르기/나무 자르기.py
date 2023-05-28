import sys

def search(heights, target):
    start = 0
    end = max(heights) 
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for height in heights:
            if height > mid:
                total += height - mid
       
        if total >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
            
    return result

N, M = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

max_height =search(heights, M)

print(max_height)
