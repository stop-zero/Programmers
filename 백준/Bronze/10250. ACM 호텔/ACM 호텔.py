# 문제 규칙 찾기
# 손님이 들어갈 층수 = 손님 % 높이
# 손님이 들어갈 번호 = 손님 // 높이 + 1
 
n = int(input())
 
for i in range(n):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1
    
    # 예외! 높이가 나눠 떨어질 떄
        # 손님이 들어갈 층수 = 높이
    if floor == 0:
        room -= 1
        floor = H
 
    print(floor*100 + room)