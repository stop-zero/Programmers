def valid(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

T = int(input())

for _ in range(T):
    x = input()
    if valid(x):
        print("YES")
    else:
        print("NO")
        
# ( 이면 스택에 추가, ) 이면 가장 최근데 추가된 ( 삭제
# 문자열이 비어있는지 확인 후 스택이 비어있으면 올바른 문자열 