import sys
N = int(input())
stack = []
stack_cnt = []
cnt = 0
arr = []
INF = 10000000000000
for i in range(N+1):
  
    if i == N:
        x = INF
    else:
        x = int(sys.stdin.readline())
    while len(stack) > 0:     
        if x >= stack[-1][0]: # Top에 있는 값이 추가 될 값보다 클때
            a = stack.pop()
            cnt += i - a[1] -1
        else: # 추가될 x값이 Stack에서 가장 작은 값일 때
            break
    stack.append([x,i]) # index 0 = 빌딩의 높이, index 1 = 빌딩의 index
print(cnt)
            
    
