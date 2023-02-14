N = int(input())
K = int(input())

dp = [[0]*(K + 1) for _ in range(N + 1)]
# dp[i][j] = i개를 가진 색 상환 중에서 j개를 인접 하지 않게 선택 하는 경우의 수
div = 1000000003

for i in range(N + 1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, N + 1):
    for j in range(2, K + 1):
        if i == N:
            dp[i][j] = (dp[i - 3][j - 1] + dp[i - 1][j]) % div
        else:
            dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % div
print(dp[N][K] % div)