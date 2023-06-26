li = []
for _ in range(6):
    li.append(int(input()))

print(sum(sorted(li[:4], reverse=True)[:3]) + max(li[4:]))
