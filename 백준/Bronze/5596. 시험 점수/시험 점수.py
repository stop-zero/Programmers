def total(scores):
    return sum(scores)

Mg =list(map(int, input().split()))
Ms = list(map(int, input().split()))

Mg_total=total(Mg)
Ms_total=total(Ms)

if Mg_total >= Ms_total:
    print(Mg_total)
else:
    print(Ms_total)