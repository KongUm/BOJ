S = input()
N = len(S)

p = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        left = i - j; right = i + j
        if 0 <= left and right < N and S[left] == S[right]:
            p[left].append(j * 2 + 1)
        else:
            break
            
for i in range(N - 1):
    for j in range(N):
        left = i - j; right = i + j + 1
        if 0 <= left and right < N and S[left] == S[right]:
            p[left].append(j * 2 + 2)
        else:
            break

dp = [int(1e9)] * (N + 1)
dp[0] = 0

for i in range(1, N + 1): # i번째 글짜부터 시작 하는 펠린드롬을 추가
    for j in p[i - 1]:
        dp[i + j - 1] = min(dp[i - 1] + 1, dp[i + j - 1])
print(dp[-1])
        