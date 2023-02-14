import itertools

T = int(input())

n = 10000000
a = [False, False] + [True]*(n-1)

for i in range(2, n+1):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False
  
visited = []
stack = []
count = 0

def BT(arr, idx):
    global count
    
    number = ""
    for i in stack:
        number += str(i)
    
    if len(number) > 0 and a[int(number)] and int(number) not in ans:
        ans.add(int(number))
        count += 1
        
    if idx == len(arr):
        return
        
    for i in range(len(S)):
        if visited[i] == False:
            visited[i] = True
            
            stack.append(arr[i])
            BT(arr, idx + 1)
            stack.pop()
            visited[i] = False
    return

for _ in range(T):
    S = input()
    num = []
    for i in S:
        num.append(int(i))
    visited = [False]*len(S)
    stack = []
    count = 0
    ans = set()
    BT(num, 0)    
    print(count)