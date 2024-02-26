from collections import deque

def josephus_permutation(N, K):
    people = deque(range(1, N + 1))
    permutation = []
   
    while people:
        for _ in range(K - 1):
            people.append(people.popleft())
        permutation.append(people.popleft())
    
    return permutation

N, K = map(int, input().split())

result = josephus_permutation(N, K)
print("<" + ", ".join(map(str, result)) + ">")
