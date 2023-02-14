N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0]*N for _ in range(N+1)]
# dp[i][j] = index j부터 시작한 i개 행렬의 곱으로 이루어진 행렬 index(j ~ j+i-1)

for i in range(2,N+1):
    for j in range(0,N-i+1):
        mini = 9999999999999
        for p in range(1,i):
            mini = min(dp[p][j] + dp[i-p][j+p] + arr[j][0]*arr[j+p-1][1]*arr[i+j-1][1], mini)
        dp[i][j] = mini

print(dp[N][0])