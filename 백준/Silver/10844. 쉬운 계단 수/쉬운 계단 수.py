N = int(input())

dp = [[0]*10 for _ in range(N+1)]

for i in range(1,10):

    dp[1][i] = 1

    

for i in range(2,N+1):

    dp[i][1] += dp[i-1][0]

    dp[i][8] += dp[i-1][9]

    for j in range(1,8+1):

        dp[i][j-1] += dp[i-1][j]

        dp[i][j+1] += dp[i-1][j]

print(sum(dp[N])%1000000000)

  