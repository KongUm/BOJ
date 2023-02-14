N = int(input())

A = list(map(int, input().split()))
frq = [0]*(1000001)
stack = []

ans = [-1]

for i in range(N):
    frq[A[i]] += 1

def Stack_Search(target):
    while True:     
        if len(stack) == 0:
            stack.append(target)
            return 0
        s = stack.pop()
        if frq[s] > frq[target]:
            stack.append(s)
            stack.append(target)
            return s      
            
stack.append(A.pop())
for i in range(N-1): # 배열의 오른쪽부터 탐색
    target = A.pop()    
    ch = Stack_Search(target)
    if ch == 0:
        ans.append(-1)
    else:
        ans.append(ch)

for i in range(N):
    print(ans.pop(), end = " ")