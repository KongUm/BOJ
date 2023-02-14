N, M = map(int, input().split())
# N = 주어진 나무의 수
# M = 필요한 나무의 길이
arr = list(map(int, input().split()))

def search(target,lo,hi):
    cp = 0
    mid = (lo+hi)//2
    
    for i in range(N):
        if mid < arr[i]:
            cp = cp + (arr[i]-mid)
    
    if cp < target:
        return search(target,lo,mid-1)
    else:
        if mid+1 > hi:
            return mid
        else:
            return search(target,mid+1,hi)
   
print(search(M, 0, max(arr)))
        
