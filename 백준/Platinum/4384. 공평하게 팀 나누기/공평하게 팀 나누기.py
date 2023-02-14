N = int(input())
W = [0]
for _ in range(N):
    W.append(int(input()))
W.sort()
sum_W = sum(W)

dp = [[-1] * 45001 for _ in range(N + 1)]
# dp[i][j] = i 번째 인덱스 사람 까지 고려할 때 j의 무게를 가지는 경우의 사람 수

dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(45001):
        if j - W[i] >= 0 and dp[i-1][j - W[i]] >= 0:    
            dp[i][j] = dp[i-1][j - W[i]] + 1

        else:
            dp[i][j] = dp[i-1][j]

mini = 1000000
ans = 0

for i in range(1, N + 1):
    for j in range(45001):
        if dp[i][j] > 0 and abs(N - dp[i][j]*2) <= 1:
            if abs(sum_W - j*2) < mini:
                mini = abs(sum_W - j*2)
                ans = j

A = [ans, sum_W - ans]
A.sort()
print(A[0], A[1])
