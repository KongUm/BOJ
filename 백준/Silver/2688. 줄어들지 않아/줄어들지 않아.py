T = int(input())

for _ in range(T):
    N = int(input())
    dp = [[0]*10 for _ in range(N)]

    for i in range(10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            for u in range(j + 1):
                dp[i][j] += dp[i - 1][u]
    print(sum(dp[N - 1]))