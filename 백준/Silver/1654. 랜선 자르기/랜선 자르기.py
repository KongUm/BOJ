import sys
K, N = map(int, input().split())
A = [0]*K
for i in range(K):
    A[i] = int(sys.stdin.readline())


def search(target,lo,hi):
    cp = 0
    mid = (lo+hi)//2
    
    for i in range(K):
        cp = cp + A[i]//mid
    
    if cp < target:
        return search(target,lo,mid-1)
    else:
        if mid+1 > hi:
            return mid
        else:
            return search(target,mid+1,hi)
    

if N == 1:
    print(A[0])
else:
    print(search(N, 1, max(A)))
        
