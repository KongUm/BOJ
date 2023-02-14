N, T = map(int,input().split())
w = [0] 
v = [0]
for i in range(N):
    a, b = map(int,input().split())
    w.append(a)
    v.append(b) 
dp = [[0]*(T+1) for _ in range(N+1)]

for i in range(N+1): # ~i번째 과목 까지만 넣을 수 있음
    for j in range(T+1): #시험까지 공부할 수 있는 시간이 j시간일때
        if j < w[i]:  #i번째 과목을 추가할 수 없을때 (시간부족)
            dp[i][j] = dp[i-1][j] #i번째 과목을 추가 하지 않았을때의 최댓값(dp[i-1][j])을 집어 넣는다
        else: #i번째 과목을 추가할 수 있을때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i]) #i번째 과목을 추가 하지 않았을때의 최댓값(dp[i-1][j])과
                                                             #추가 했을때의 최댓값(dp[i-1][j-w[i]]+v[i]) 중 더 큰 값을 집어 넣는다
print(dp[N][T])