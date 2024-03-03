# 오름차순 정렬
# 카드들 중에서 3장을 선택하여 만들 수 있는 합 구하기
# 이 값들 중에서 M을 넘지 않으면서 최대한 M에 가까운 값 찾기N, M = map(int, input().split())
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
