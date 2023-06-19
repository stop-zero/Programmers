# 몬스터 방어율 수치 a , 유저의 방무 b
a ,b=map(int, input().split())

D=a-(a*(b*0.01))

if D >= 100:
    print (0)
else:
    print(1)

