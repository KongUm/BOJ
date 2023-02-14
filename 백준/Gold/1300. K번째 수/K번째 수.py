N = int(input())
k = int(input())

low = 1
high = N**2+1

def lower_bound(target, left, right, multi):
    
    while left < right:
        mid = (left + right) // 2
        if mid*multi >= target:
            right = mid
        else:
            left = mid + 1
    
    return left

while low < high: # low <= 범위 < high
    middle = (low + high) // 2
    count = 0
    for i in range(1,N+1):
        count += lower_bound(middle, 1, N+1, i)-1
        
    if count >= k:
        high = middle
    else:
        low = middle + 1
print(low-1)
