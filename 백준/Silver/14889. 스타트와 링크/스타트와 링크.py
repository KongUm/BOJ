N = int(input()) # 사람은 1번부터 ~ N번
arr = []
start_stack = []
link_stack = [i for i in range(1,N+1)]
ans = []

for _ in range(N):
    S = list(map(int, input().split()))
    arr.append(S)
    
def dfs(a):
    if a == N//2:
        start_score = 0
        link_score = 0
        for i in start_stack:
            for j in start_stack:
                if i != j:
                    start_score += arr[i-1][j-1]
                    start_score += arr[j-1][i-1]
        for i in link_stack:
            for j in link_stack:
                if i != j:
                    link_score += arr[i-1][j-1]
                    link_score += arr[j-1][i-1]
        ans.append(abs(start_score-link_score))            
    else:
        for i in range(1,N+1):
            if i in start_stack:
                continue
            if a >= 1:
                if i < start_stack[-1]:
                    continue
            start_stack.append(i)
            link_stack.remove(i)
            dfs(a+1)
            start_stack.pop()
            link_stack.append(i)
dfs(0)
print(min(ans)//2)