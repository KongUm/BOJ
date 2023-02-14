N = int(input())
arr = list(map(int,input().split()))
dp = [1]*N 
# dp[i] = 0 ~ j 범위내에 있는 LIS의 길이의 최댓값 (DP Table)

for i in range(N): # 0 ~ i까지의 범위를 설정 각 i당 dp[i] 설정
    for j in range(0,i):
        if arr[j] > arr[i]: 
            #j는 i의 왼쪽에 있으므로 arr[j] > arr[i]여야 한다.
            #감소하는 수열의 기본 전제 조건
            dp[i] = max(dp[j]+1,dp[i])
            # dp[j]에는 0~j까지 범위의 LIS의 길이의 최댓값이 이미 구해져 있다.
            # 즉 j커서가 계속 오른쪽으로 가면서 현재 j커서의 위치 상에서
            # 그 시점 직전까지 가장 길었던 LIS의 값이 저장 되어 있던 dp[i]보다
            # dp[j] + 1의 값이 커질 때 dp[i]의 값을 dp[j] + 1 로 갱신한다
print(max(dp))
