T = int(input())

memo = [0,1]   #n번째 피보나치 수열이 들어왔을 때 출력되는 0과 1의 수

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif len(memo) <= n:
        memo.append(fibonacci(n-1) + fibonacci(n-2))
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return memo[n]

for i in range(T):
    N = int(input())
    fibonacci(N)
    if N == 0:
        print(1,0)
    else:print(memo[N-1],memo[N])