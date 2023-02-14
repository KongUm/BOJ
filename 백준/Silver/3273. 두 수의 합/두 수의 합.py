N = int(input())
A = list(map(int, input().split()))
M = int(input())

A.sort()
count = 0
left = 0
right = len(A)-1

while left < right:
    if A[left] + A[right] > M:
        right -= 1
    elif A[left] + A[right] < M:
        left+= 1
    else:
        count += 1
        right -=1
        left+= 1
print(count)
         