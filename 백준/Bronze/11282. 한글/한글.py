# 초성, 중성, 종성의 개수로 나누어 나머지와 몫 계산
# 각각의 인덱스 구하고 인덱스로 초성, 중성, 종성 구하기
# N = int(input()) 

# initials_count = 19
# vowels_count = 21
# finals_count = 28

# initial_index = (N-1) // (vowels_count * finals_count)
# vowel_index = ((N-1) // finals_count) % vowels_count
# final_index = (N-1) % finals_count

# # 초성
# initials = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# initial = initials[initial_index]

# # 중성
# vowels = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# vowel = vowels[vowel_index]

# # 종성
# finals = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# final = finals[final_index]

# # UTF-8 인코딩
# print(initial + vowel + final)

# 다 틀렸고 겁나 간단하게 풀린 문제..ㅠㅠ
print(chr(44031+int(input())))

