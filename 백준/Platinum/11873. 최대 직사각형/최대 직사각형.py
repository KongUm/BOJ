import sys
ans = []
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  
    
    maxi = 0
    
    for i in range(N):       
        arr = [[0,0]]
        for j in range(1,M+1):
            if A[i][j-1] == 1:
                if i == 0:
                    arr.append([1,j])
                else:
                    arr.append([A[i-1][j-1] + 1, j])
                    A[i][j-1] = A[i-1][j-1] + 1
            else:
                arr.append([0, j])
        arr.append([0,M+1])
        
        stack = [] 
             
        for p in range(M+2):
            last_change = -1    
            while len(stack) > 0:
                if arr[p][0] < stack[-1][0]: # 만약 길이가 바로 직전 스택보다 작다면
                    l = stack.pop()
                    maxi = max(maxi,l[0]*(arr[p][1] - l[1]))
                    last_change = l[1]
                else:           
                    break
            if last_change > 0:
                stack.append([arr[p][0],last_change])
            else:
                stack.append([arr[p][0],p])
    ans.append(maxi)
for i in ans:
    print(i)