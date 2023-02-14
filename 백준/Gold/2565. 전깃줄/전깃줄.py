N = int(input())
cord = [] # cord[i][0] = 시작지점 기준 i+1번째 전선의 시작지점
          # cord[i][1] = 시작지점 기준 i+1번째 전선의 끝지점
for _ in range(N):
    cord.append(list(map(int,input().split())))
cord.sort()

dp = [1] * N
# dp[i] = 시작지점 기준 i+1번째 전선까지 고려할때 없애야하는 전선 개수의 최솟값

for i in range(N):
    for j in range(0,i+1):
        if cord[j][1] < cord[i][1]:
            dp[i] = max(dp[j]+1, dp[i])
    
print(N-max(dp))


