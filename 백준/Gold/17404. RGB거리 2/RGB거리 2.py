N = int(input())

color = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(3)] for _ in range(N)]

#dp[i][j][k] = i번째 집을 (맨처음 칠한 색은 j) k색으로 칠했을때
d = [[1,2],[0,2],[0,1]]
for i in range(3):
    dp[0][i][i] = color[0][i]
    for j in d[i]:
        dp[0][i][j] = int(1e10)

for i in range(1,N):
    for j in range(3):
        dp[i][j][0] = min(dp[i-1][j][1], dp[i-1][j][2]) + color[i][0]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + color[i][1]
        dp[i][j][2] = min(dp[i-1][j][0], dp[i-1][j][1]) + color[i][2]
mini = int(1e10)

for i in range(3):
    for j in d[i]:
        mini = min(dp[N-1][i][j], mini)
print(mini)