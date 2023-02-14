N, M = map(int, input().split())
stack = []

def dfs(a):
    if a == M:
        for i in range(M):
            if i == M-1:
                print(stack[i])
            else:
                print(stack[i], end = " ")
        return
    else:
        if a > 0:
            lo = stack[-1]+1
        else:
            lo = 1
        for i in range(lo,N+1):
            stack.append(i)
            dfs(a+1)
            stack.pop()
dfs(0)