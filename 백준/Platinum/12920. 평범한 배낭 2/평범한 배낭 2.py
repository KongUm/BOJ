N, M = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]
W = [0]
V = [0]

for i in range(N):
    w, v, K = info[i]
    idc = 0
    while K - 2**idc > 0:
        K -= 2**idc
        W.append(2**idc*w)
        V.append(2**idc*v)
        idc += 1
    W.append(w*K)
    V.append(v*K)
        
        
dp = [[0]*(M+1) for _ in range(len(W))]
# dp[i][j] = i번째 물건까지 고려할때 j 무게인 경우의 가치의 최대 만족도  

for i in range(1,len(W)):
    for j in range(1, M+1):
        if j == W[i]: 
            dp[i][j] = max(dp[i-1][j],V[i])         
        elif j > W[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]]+V[i])   
        else:
            dp[i][j] = dp[i-1][j]

print(dp[len(W)-1][M])