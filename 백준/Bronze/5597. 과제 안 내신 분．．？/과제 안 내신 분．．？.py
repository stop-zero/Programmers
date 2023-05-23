s = [i for i in range(1, 31)]

for _ in range(28):
    applied = int(input())
    s.remove(applied)
    
print(min(s))
print(max(s))