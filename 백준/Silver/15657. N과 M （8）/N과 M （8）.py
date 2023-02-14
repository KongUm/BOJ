N,M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
 
def dfs():
    if len(s) == M: # 수열의 길이가 M이 되었다면
        print(' '.join(map(str,s))) #출력
        return
    
    for i in arr: 
        if len(s) != 0:
            if i < s[-1]:
                continue
        s.append(i)
        dfs()
        s.pop()
 
dfs()
