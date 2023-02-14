N = int(input())
dp = [0]*(N+1) # dp[i] = i를 1로 만들기 위해 필요한 연산의 최솟값
        
for i in range(1,N):
    if dp[i+1] == 0:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = min(dp[i]+1, dp[i+1])
        
    if i <= N//2:
        if dp[i*2] == 0:
            dp[i*2] = dp[i] + 1
        else:
            dp[i*2] = min(dp[i]+1, dp[i*2])
    if i <= N//3:
        if dp[i*3] == 0:
            dp[i*3] = dp[i] + 1
        else:
            dp[i*3] = min(dp[i]+1, dp[i*3])
print(dp[N])