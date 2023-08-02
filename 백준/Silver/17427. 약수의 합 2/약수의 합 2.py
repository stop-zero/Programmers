# f(A)=A의 약수의 합
# g(N)=f(1)+f(2)+...+f(N)
# g(N)은?
# N의 배수는 N을 항상 약수로 갖는다
# N이하의 자연수 중에서 i 를 약수로 갖는 개수는 N/i개

N=int(input())
sum = 0

for i in range(1, N+1):
    sum+=(N//i)*i

print(sum)
