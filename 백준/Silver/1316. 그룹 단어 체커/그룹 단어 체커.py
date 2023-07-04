# 주어진 단어들 안에서 알파벳이 연속되거나 한번만 나오는 애들을 카운트 해서 출력
# 현재 문자와 이전 문자가 같으면 다음 문자 확인
# 현재 문자와 이전 문자가 다르면 이전에 기록 확인
    # 이전 기록에 있으면 종료
    # 없으면 현재 문자를 이전 기록에 추가
    
N=int(input())
group=0

for _ in range(N):
    word = input()
    p=word[0]
    used = set()
    
    for char in word:
        if char != p:
            if char in used:
                break
            else:
                used.add(p)
                p=char
    else: # 마지막 문자
        used.add(p)
        group += 1

print(group)

