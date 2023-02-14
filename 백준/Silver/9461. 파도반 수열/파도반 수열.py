T = int(input())
N = []
for i in range(T):
    N.append(int(input()))

max = max(N)

memo = [0 for i in range(max+1)]
memo[1] = 1
memo[2] = 1
memo[3] = 1

def P(N):
    if memo[N] != 0:
        return memo[N]
    else:
        memo[N] = P(N-2) + P(N-3)
        return memo[N]

for i in range(T):
    print(P(N[i]))