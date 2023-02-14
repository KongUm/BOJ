N, K = map(int, input().split()) # 0~N까지의 정수 K개를 더해 그 합이 N이 되도록

dp = [[0]*(K+1) for _ in range(N+1)]
# dp[i][j] = j개의 정수로 i를 만드는 경우의 수

for i in range(0,N+1):
    dp[i][1] = 1
    
for i in range(2,K+1):
    for j in range(N+1):
        for p in range(N+1):
            if j-p >= 0:
                dp[j][i] += dp[j-p][i-1]
print(dp[N][K]%1000000000)
