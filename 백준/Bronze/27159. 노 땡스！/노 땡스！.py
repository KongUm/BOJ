N = int(input())
A = list(map(int, input().split()))


stack = []
ans = 0
for i in range(N):
    if len(stack) > 0 and stack[-1] + 1 == A[i]:
        stack.append(A[i])
        continue
    ans += A[i];
    stack = [A[i]]
print(ans)