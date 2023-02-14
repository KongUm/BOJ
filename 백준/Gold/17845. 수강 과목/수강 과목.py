N, K = map(int,input().split())
w = [0] 
v = [0]
for i in range(K):
    a, b = map(int,input().split())
    v.append(a)
    w.append(b) 
dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(K+1): 
    for j in range(N+1):
        if j < w[i]:  
            dp[i][j] = dp[i-1][j] 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])                                                              
print(dp[K][N])