N = int(input())

dp = [0,1]

for i in range(N):

    ans = (dp[0] + dp[1])%15746

    dp[0] = dp[1]

    dp[1] = ans

    

print(dp[1])

    