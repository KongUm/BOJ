n = int(input())
piramid = [list(map(int,input().split())) for _ in range(n)]

dp = [[piramid[0][0]]]
# dp[i][j]는 맨위에서 i층 아래에 있는 층의 / 맨 왼쪽 칸에서 i번째 칸까지의 경로의 최댓값

if n >= 2:
    for i in range(1,n):
        floor = []
        for j in range(i+1):
            if j == 0 :
                floor.append(dp[i-1][j] + piramid[i][j])
            elif j == i:
                floor.append(dp[i-1][j-1] + piramid[i][j])
            else:
                floor.append(max(dp[i-1][j],dp[i-1][j-1]) + piramid[i][j])
        dp.append(floor)
    print(max(dp[n-1]))
else:
    print(dp[0][0])