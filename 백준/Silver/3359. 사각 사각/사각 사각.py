n = int(input())
A = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 2 for _ in range(n + 1)]

dp[1] = A[1][::-1]

for i in range(2, n + 1):
    for j in range(2):
        for u in range(2):
            dp[i][u] = max(dp[i - 1][j] + abs(A[i - 1][j] - A[i][u]) + A[i][1 - u], dp[i][u])

print(max(dp[n]))