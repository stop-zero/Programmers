N, M = map(int, input().split()) 
balls = [i for i in range(N+1)]  

for _ in range(M):
    i, j = map(int, input().split())  
    balls[i], balls[j] = balls[j], balls[i]  

result = ' '.join(map(str, balls[1:])) 
print(result)  
