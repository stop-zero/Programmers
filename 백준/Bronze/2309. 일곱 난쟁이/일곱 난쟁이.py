# 다른 방법
data = []
other_1=0
other_2=0

for _ in range(9):
    data.append(int(input()))

result = sum(data)

for i in range(8):
    for j in range(i+1, 9):
        if result-(data[i]+data[j])==100:
            other_1=data[i]
            other_2=data[j]
            
data.remove(other_1)
data.remove(other_2)

data.sort()

for i in data:
    print(i)