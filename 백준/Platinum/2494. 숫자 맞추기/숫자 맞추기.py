N = int(input())
A = input(); B = input()

dp = [[int(1e9)]*(10) for _ in range(N + 1)]   
# dp[i][j] = i번째 숫자까지는 일치됨, i + 1번째 숫자는 왼쪽으로 j번 돌아가 있음 즉 "(기존 + j) % 10"
path = [[10]*10 for _ in range(N + 1)]  
value = [[10]*10 for _ in range(N + 1)]   
dp[0][0] = 0

for i in range(1, N + 1): # i번째 숫자를 돌릴지
    a, reg = int(A[i - 1]), int(B[i - 1])
    for j in range(10): # 얼마나 돌아가 있는 얘를 선택할지
        for u in range(10): # 왼쪽으로 몇번 돌릴지
            now = (a + j + u)%10
            temp = dp[i - 1][j] + u
            
            if reg <= now:
                right = now - reg
            else:
                right = 10 - abs(now - reg)
            temp += right
            if temp < dp[i][(j + u)%10]:
                dp[i][(j + u)%10] = temp
                value[i][(j + u)%10] = u - right
                path[i][(j + u)%10] = j
                
idx, ans = 0, int(1e9)                
for i in range(10):
    if dp[-1][i] < ans:
        ans = dp[-1][i]
        idx = i
stack = []
for i in range(N, 0, -1):
    stack.append(value[i][idx])
    idx = path[i][idx]

print(ans)
for i in range(1, N + 1):
    print(i, stack.pop())


