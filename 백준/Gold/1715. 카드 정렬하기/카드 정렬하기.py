import heapq

def minimum_comparison(cards):
    # 우선순위 큐를 사용하여 최소 힙 생성
    heap = []
    for card in cards:
        heapq.heappush(heap, card)

    result = 0  # 비교 횟수 저장 변수

    # 우선순위 큐에 묶음이 2개 이상 남아있는 동안 반복
    while len(heap) > 1:
        # 가장 작은 두 묶음 선택
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        # 두 묶음을 합쳐서 새로운 묶음 생성
        new_card = a + b

        # 비교 횟수 갱신
        result += new_card

        # 새로운 묶음을 우선순위 큐에 추가
        heapq.heappush(heap, new_card)

    return result

# 입력 받기
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

# 최소 비교 횟수 계산
answer = minimum_comparison(cards)

# 결과 출력
print(answer)
