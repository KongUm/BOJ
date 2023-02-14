N = int(input())
A = set(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

possess = list(A&set(B))
possess.sort()

def binary_search(arr,target,start,end):
        if start > end:
                return 0 
        mid = (start+end)//2
        if arr[mid] == target:
                return 1
        elif arr[mid] < target:
                return binary_search(arr,target,mid+1,end)
        else:
                return binary_search(arr,target,start,mid-1)
 
for i in range(M):
        print(binary_search(possess, B[i], 0, len(possess)-1), end = " ")