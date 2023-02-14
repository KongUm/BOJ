N = int(input())
score = [0]
for _ in range(N):
    score.append(int(input()))
dp = [[0]*2 for _ in range(N+1)]
#dp[i][j] = i번째 계단까지 점수를 얻었고 j개의 계단을 연달아 올랐을 때
dp[1][0] = score[1]
if N > 1:
    for i in range(0,N):
        dp[i+1][1] = dp[i][0] + score[i+1]
        if i <= N-2:
            dp[i+2][0] = max(dp[i]) + score[i+2] 
print(max(dp[N]))