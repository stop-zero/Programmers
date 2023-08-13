# if 문으로 조건 주기
E, S, M = map(int, input().split())

year = 1 # 맨 처음 연도 설정
while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    year += 1