# a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)
# a 🍰 b = c >> 에서 b 구하기

a = list(map(int, input().split()))
c = list(map(int, input().split()))
# b = (c.x - a.z, c.y / a.y, c.z - a.x)

print(c[0]-a[2],c[1]//a[1],c[2]-a[0])