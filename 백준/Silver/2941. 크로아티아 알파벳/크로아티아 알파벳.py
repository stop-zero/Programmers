N = input()
list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in list:
    N = N.replace(i, ' ')
print(len(N))