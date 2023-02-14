N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
index = []
value = []

def dfs(N):
    global ans
    if len(index) == M:  # 수열의 길이가 M이 되었다면
        print(' '.join(map(str, value)))  # 출력
        return
    a = []
    for i in range(len(arr)):
        
        if arr[i] in a:
            continue
        if len(index) > 0:
            if i in index:
                continue
                 
   
       
        index.append(i)
        value.append(arr[i])
        a.append(arr[i])
        dfs(N+1)
        index.pop()
        value.pop()


dfs(0)
