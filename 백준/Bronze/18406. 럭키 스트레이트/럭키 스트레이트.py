N=input() 
M=len(N) # 길이

left=0
right=0

for i in range(M//2):
    left += int(N[i])

for i in range(M//2, M):
    right += int(N[i])
    
if left == right:
    print('LUCKY')
else:
    print("READY")