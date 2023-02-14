import sys
N = int(input())

input = lambda: sys.stdin.readline().rstrip()

arr = [[0,0]]
for i in range(1,N+1):
    arr.append([int(input()), i])
arr.append([0,N+1])

stack = []
maxi = 0

for i in range(N+2):
    last_change = -1    
    while len(stack) > 0:
        if arr[i][0] < stack[-1][0]: # 만약 길이가 바로 직전 스택보다 작다면
            l = stack.pop()
            maxi = max(maxi,l[0]*(arr[i][1] - l[1]))
            last_change = l[1]
        else:           
            break
    if last_change > 0:
        stack.append([arr[i][0],last_change])
    else:
        stack.append([arr[i][0],i])
    
print(maxi)   