n = int(input()) 
words = []

for _ in range(n):
    words.append(input())  

# 중복 제거
words = list(set(words))

# 정렬 조건에 따라 정렬
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
