N, M = map(int, input().split())

house = []
chicken = []
score = []
stack = []

for i in range(N):
    S = list(map(int, input().split()))
    for j in range(N):
        if S[j] == 1:
            house.append([j,i])
        elif S[j] == 2:
            chicken.append([j,i])

for i in range(len(house)):
    a = []
    for j in range(len(chicken)):
        sx = abs(house[i][0] - chicken[j][0])
        sy = abs(house[i][1] - chicken[j][1])
        a.append(sx+sy)
    score.append(a)
#print(score)



sum_ans = 99999999999
def dfs(a):
    global sum_ans
    global min_ans
    
    if a == M:
        min_ans = [999]*len(house)
        for i in stack:
            
            for j in range(len(house)):
                min_ans[j] = min(min_ans[j],score[j][i])
            sum_ans = min(sum_ans,sum(min_ans))
                
       
        return
    else:
        if a == 0:
            lo = 0
        else:
            lo = stack[-1]+1
        for i in range(lo,len(chicken)):
            stack.append(i)
            dfs(a+1)
            stack.pop()

dfs(0)

print(sum_ans)
