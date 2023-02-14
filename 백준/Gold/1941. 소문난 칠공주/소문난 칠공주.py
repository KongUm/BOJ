from itertools import combinations
from collections import deque

arr = [] # arr : index 0 ~ 24 (왼쪽 위에서부터 오른쪽 아래 순으로)
for i in range(5):
    a = input()
    for j in range(5):
        if a[j] == 'S':
            arr.append(0)
        else:
            arr.append(1)
  # 이다솜파 = 0, 임도연파 = 1로 변환해서 arr에 일차원 배열로 저장 (0~24)
stack = []
count = 0
ans = []

def dfs(a,sum): # sum = 수열에 해당되는 인덱스의 arr값을 모두 더한 수 (즉 )
    global count
    if a == 7: # 수열의 길이가 7이 됬을때       
        if check(stack):
            count+= 1
        return
    else:
        if a > 0:
            lo = stack[-1]+1
        else:
            lo = 0
        for i in range(lo,25):         
            if sum + arr[i] >= 4:
                continue       
            stack.append(i)
            #print(sum+arr[i],stack)
            dfs(a+1,sum+arr[i])
            stack.pop()
                      
def check(A): #A = 배열
    Q = deque()
    cnt = 1
    Q.append(0)
    visited = [False]*7  
    visited[0]  = True
    
    while len(Q) != 0:                                     
        u = Q.popleft()
        for v in range(7):
            if visited[v] == True:
                continue
            else:
                if (A[u]-1 == A[v] and A[u]%5 != 0) or (A[u]+1 == A[v] and A[v]%5 != 0) or A[u]-5 == A[v] or A[u]+5 == A[v]:
                    Q.append(v)
                    cnt += 1
                    visited[v] = True
                    
    if cnt == 7:
        return True
    else:
        return False
                
dfs(0,0)       
print(count)