N, M = map(int, input().split())

S = []
for i in range(M):
    A = list(map(int, input().split()))
    S.append(set(A[1:]))

used = set()
stack = []
ans = int(1e9)
def BT():
    global ans
    global used

    if len(used) == N:
        ans = min(ans, len(stack))
        return

    if len(stack) > 0:
        s = stack[-1] + 1
    else:
        s = 0

    for i in range(s, M):
        stack.append(i)
        used = used.union(S[i])
        BT()
        stack.pop()
        used = set()
        for j in stack:
            used = used.union(S[j])
BT()
if ans == int(1e9):
    print(-1)
else:
    print(ans)