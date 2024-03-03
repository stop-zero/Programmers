N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()
result = 0

for i in range(N):
    for j in range(i + 1, N):
        left = j + 1
        right = N - 1
        target = M - (cards[i] + cards[j])
        
        while left <= right:
            mid = (left + right) // 2
            if cards[mid] <= target:
                result = max(result, cards[i] + cards[j] + cards[mid])
                left = mid + 1
            else:
                right = mid - 1

print(result)