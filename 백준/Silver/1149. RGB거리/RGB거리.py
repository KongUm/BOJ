N = int(input())

cost = [[]]
for _ in range(N):
    cost.append(list(map(int,input().split())))
    
dp = [[] for _ in range(N+1)]
dp[1] = cost[1]
# dp[p][q] = p번째 집까지 q번째 색으로 색칠했을 때 비용의 최솟값 
# 즉 max(dp[N])에 최종적으로 출력해야할 답이 들어있을 것임

for i in range(2,N+1):
    dp[i].append(min(dp[i-1][1], dp[i-1][2]) + cost[i][0])
    dp[i].append(min(dp[i-1][0], dp[i-1][2]) + cost[i][1])
    dp[i].append(min(dp[i-1][0], dp[i-1][1]) + cost[i][2])
    
print(min(dp[N]))