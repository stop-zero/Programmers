R = int(input())

for _ in range(R):
    cnt, word = input().split()
    cnt = int(cnt)
    word = str(word)
    for x in word:
        print(x*int(cnt), end="")
    print()