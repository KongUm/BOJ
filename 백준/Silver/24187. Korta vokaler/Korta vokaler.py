A = input()
N = len(A)
arr = [-1]
alpha = ['a','e','i','o','u','y']; alpha = set(alpha)
for i in A:
    if i in alpha:
        arr.append(1)
    else:
        arr.append(0)


dp = [[0]*3 for _ in range(N + 1)]

dp[0][0] = 1
for i in range(1, N + 1):
    if arr[i] == 0:
        for j in range(0, i):
            dp[i][0] += dp[j][0] # 모음을 선택 안했을 때 + 자음
            dp[i][2] += dp[j][1] # 모음을 선택한 직후 일때 + 자음
    else:
        for j in range(0, i):
            dp[i][1] += dp[j][0] + dp[j][1] + dp[j][2]

cnt = 0
for i in range(1, N + 1):
    cnt += sum(dp[i])
print(cnt)