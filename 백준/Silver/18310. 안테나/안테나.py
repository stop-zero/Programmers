n = int(input()) 
houses = list(map(int, input().split()))

houses.sort() 

if n % 2 == 0:
    med = houses[n // 2 - 1]
else:
    med = houses[n // 2]

print(med)
