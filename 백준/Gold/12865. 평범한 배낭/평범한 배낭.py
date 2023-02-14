N, K = map(int,input().split())
W = [0]
V = [0]
for _ in range(N):
    a,b = map(int,input().split())
    W.append(a)
    V.append(b)


min_w = min(W)

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1): #i번째 가방까지 들 수 있을 때
    for j in range(min_w,K+1): #j kg까지 들 수 있을 때
    
        if j == W[i]: 
            dp[i][j] = max(dp[i-1][j],V[i])
            
        elif j > W[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]]+V[i])   
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])
           
