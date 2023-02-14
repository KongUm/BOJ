N, M = map(int, input().split()) # N = 앱 개수, M = 확보해야하는 메모리 
v = list(map(int, input().split()))
v.insert(0,0)
w = list(map(int, input().split()))
w.insert(0,0)

memory = sum(v)

dp = [[0]*10001 for _ in range(N+1)]
#dp[i][j] = index i까지의 앱을 고려했을때 j비용을 사용했을때의 메모리 감소량의 최댓값

for i in range(1,N+1):
    for j in range(1,10001):
        if j-w[i] >= 0:
            dp[i][j] = max(dp[i-1][j-w[i]]+v[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
mini = 9999999999999
for i in range(N+1):
    for j in range(10001):
        if dp[i][j] >= M:
            mini = min(j, mini)
print(mini)
            