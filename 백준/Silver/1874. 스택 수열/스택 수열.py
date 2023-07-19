n = int(input()) 
sequence = [int(input()) for _ in range(n)]  

stack = []
result = [] 
current = 1  

for num in sequence:
    # 현재 숫자가 스택의 top과 같을 때까지 push를 수행
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    # 스택의 top이 현재 숫자와 다르면 수열을 만들 수 없음
    if stack[-1] != num:
        print('NO')
        exit(0)

    # 스택의 top이 현재 숫자와 같을 경우 pop
    stack.pop()
    result.append('-')

for op in result:
    print(op)
