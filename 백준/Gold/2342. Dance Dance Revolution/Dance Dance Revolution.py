p = list(map(int, input().split()))

if p[0] == 0:
    print(0)
    exit()

dp = [[[1000000]*(len(p)-1) for _ in range(5)] for i in range(5)]
# dp[i][j][k] = k를 실행한후 (i, j)에 있을때 사용한 최소 힘

dp[0][p[0]][0] = 2
dp[p[0]][0][0] = 2

for c in range(1,len(p)-1):
    com = p[c]
    for i in range(5): # 전에 있던곳 선택
        for j in range(5): # 전에 있던곳 선택
            if dp[i][j][c-1] > 0:
                # i를 움직일때
                if com == i:
                    dp[com][j][c] = min(dp[i][j][c-1] + 1, dp[com][j][c])
                elif i == 0:
                    dp[com][j][c] = min(dp[i][j][c-1] + 2, dp[com][j][c])
                elif (com+i)%2 == 0:
                    
                    dp[com][j][c] = min(dp[i][j][c-1] + 4, dp[com][j][c])
                else:
                    dp[com][j][c] = min(dp[i][j][c-1] + 3, dp[com][j][c])
                
                if com == j:
                    dp[i][com][c] = min(dp[i][j][c-1] + 1, dp[i][com][c])
                elif j == 0:
                    
                    dp[i][com][c] = min(dp[i][j][c-1] + 2, dp[i][com][c])
                elif (com+j)%2 == 0:
                    dp[i][com][c] = min(dp[i][j][c-1] + 4, dp[i][com][c])
                else:
                    dp[i][com][c] = min(dp[i][j][c-1] + 3, dp[i][com][c])
ans = int(1e9)
for i in range(5):
    for j in range(5):
        if dp[i][j][len(p)-2] > 0:
            ans = min(ans, dp[i][j][len(p)-2])

print(ans)