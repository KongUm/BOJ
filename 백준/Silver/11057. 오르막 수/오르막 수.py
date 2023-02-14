N = int(input())
dp = [[],[1]*10]

for i in range(2,N+1):
    dp.append([0]*10)
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])
print(sum(dp[N])%10007)