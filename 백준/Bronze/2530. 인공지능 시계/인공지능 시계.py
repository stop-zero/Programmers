# 현재 시각 입력 받기
current_time = input().split()
current_hour = int(current_time[0])
current_minute = int(current_time[1])
current_second = int(current_time[2])
cooking_time = int(input())

# 오븐구이 종료 시각 계산
total_seconds = (current_hour * 3600) + (current_minute * 60) + current_second + cooking_time
end_hour = (total_seconds // 3600) % 24
end_minute = (total_seconds % 3600) // 60
end_second = total_seconds % 60

print(end_hour, end_minute, end_second)
