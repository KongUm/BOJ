A = " " + input()
B = " " + input()

dp = [[0]*len(B) for _ in range(len(A))]
# dp[i][j] = A[i]와 B[j]까지 고려할떄 최댓값

for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
cnt = dp[len(A)-1][len(B)-1]
stack = []
sx, sy = len(A),len(B)

for i in range(len(A)-1, 0, -1):
    for j in range(len(B)-1 ,0, -1):
        if i >= sx or j >= sy:
            continue

        if dp[i][j] == cnt and A[i] == B[j]:
            cnt -= 1
            stack.append(A[i])
            sx, sy = i, j
            
print(dp[len(A)-1][len(B)-1])
for i in range(len(stack)):
    print(stack.pop(), end = "")