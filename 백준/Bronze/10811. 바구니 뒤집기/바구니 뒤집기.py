# 10813 역순으로
N, M = map(int, input().split())
b = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    # balls[i], balls[j] = balls[j], balls[i] #10813
    b[i - 1 : j] = b[i - 1 : j][::-1] # 해당 범위의 바구니 순서를 역순으로 변경

result = " ".join(map(str, b))
print(result)
