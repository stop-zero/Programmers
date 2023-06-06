
# 조건 : 7개를 더했을 때 100보다 작아야 한다.  
import itertools

def find_seven_dwarfs(heights):
    # 아홉 난쟁이 중 일곱 난쟁이를 선택하는 모든 조합 확인
    combinations = itertools.combinations(heights, 7)

    for combo in combinations:
        if sum(combo) == 100:
            return sorted(combo)

# 아홉 난쟁이의 키 입력 받기
heights = []
for _ in range(9):
    height = int(input())
    heights.append(height)

# 일곱 난쟁이 찾기
result = find_seven_dwarfs(heights)

# 결과 출력
for height in result:
    print(height)
