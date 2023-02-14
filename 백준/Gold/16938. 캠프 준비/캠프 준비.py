N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

used = []
stack = []
sum = 0
count = 0
ans = []
def BT(idx):
    global count
    global sum
    
    if idx > 0 and max(stack) - min(stack) >= X and L <= sum <= R:
        count += 1
        ans.append(stack[:])
    if idx == N or sum > R:
        
        return 
    l = 0  
    if len(used) > 0:
        l = used[-1]+1
                
    for i in range(l,N):
        if i not in used:
            stack.append(A[i])
            used.append(i)
            sum += A[i]           
            BT(idx + 1)
            stack.pop()
            used.pop()
            sum -= A[i]
    return
    
BT(0)
print(count)