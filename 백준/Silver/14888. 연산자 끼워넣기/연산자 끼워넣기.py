N = int(input())
arr = list(map(int, input().split()))
opt = list(map(int, input().split()))
# + = 0 , - = 1 , * = 2 , // = 3  (index)
stack = []
ans = []

def dfs(a):
    global opt
    if a == N-1:
        
        score = arr[0]
        for i in range(1,N):
            if stack[i-1] == 0:
                score = score + arr[i]
            elif stack[i-1] == 1:
                score = score - arr[i]
            elif stack[i-1] == 2:
                score = score * arr[i]
            else:
                if score < 0:
                    score = (score*(-1)//arr[i])*(-1)
                else:
                    score = score//arr[i]
        ans.append(score)
        return
    else:
        for i in range(4):
            if opt[i] == 0:
                continue
            stack.append(i)
            opt[i] -= 1
            dfs(a+1)
            stack.pop()
            opt[i] += 1
dfs(0)
print(max(ans))
print(min(ans))