n= int(input())

for _ in range(n):
    ox = input() # ox 입력
    
    score = 0   # 현재 점수
    sum_score = 0   # 연속해서 나온 개수 
    
    for result in ox:
        if result =='O':
            sum_score += 1
            score += sum_score
        else:
            sum_score=0        
    print(score)    