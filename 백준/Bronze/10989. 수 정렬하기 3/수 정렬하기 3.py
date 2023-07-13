import sys
input = sys.stdin.readline

n = int(input())  
numbers = [0]*(10000+1) # 계수정렬

for _ in range(n):
    numbers[int(input())] += 1  # 수 입력받기

for i in range(len(numbers)):
    if numbers[i] != 0: # 입력 받은 데이터 출력
        for _ in range(numbers[i]):
            print(i)
