q, n, D = map(int, input().split())
f1 = input()
f2 = input()

dp = [[0]*(D+1) for _ in range(n+1)]
# dp[i][j] = 길이가 i이고 두 초점과의 거리가 D 수열의 개수

dp[0][0] = 1
for i in range(1,n+1):
    if f1[i-1] == f2[i-1]:
        dp[i][0] += dp[i-1][0] 
        
    
for i in range(1,n+1):
    for j in range(1,D+1):
        if f1[i-1] == f2[i-1]:
            if j-2 >= 0:
                dp[i][j] += dp[i-1][j-2]*(q-1)
            dp[i][j] += dp[i-1][j]
        else:
            if j-2 >= 0:
                dp[i][j] += dp[i-1][j-2]*(q-2)
            dp[i][j] += dp[i-1][j-1]*2

print(dp[n][D])