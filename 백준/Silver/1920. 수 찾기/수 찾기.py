N = int(input())
A = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))
A.sort()

def binary_search(target,low,high):
    mid = (low+high)//2
    
    if target == A[mid]:
        print(1)
        return
    if low >= high:
        print(0)
        return
    elif target > A[mid]:
        binary_search(target,mid+1,high)
    else:
        binary_search(target,low,mid-1)

for i in range(M):
    binary_search(T[i], 0, len(A) - 1)