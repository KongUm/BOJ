import sys

N = int(input())
# 전깃줄의 개수
C = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    C.append([a,b])
C.sort()

def lower_bound(arr, target):
    low, high = 0, len(arr)-1 # 탐색범위 low ~ high
    
    while low <= high:
        mid = (low + high) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target <= arr[mid]:
            high = mid - 1
    return low

memo = []
dp = []

for i in range(N):
    if i == 0:
        memo.append(C[i][1])
        dp.append(1)
    elif C[i][1] > memo[-1]:
        memo.append(C[i][1])
        dp.append(len(memo))
    else:
        loca = lower_bound(memo, C[i][1])
        memo[loca] = C[i][1]
        dp.append(loca+1)
        
maxi = max(dp)

print(N-maxi)
stack = []

for i in range(N-1,-1,-1):
    if dp[i] == maxi:
        maxi -= 1
    else: #dp[i] != maxi 라면
        stack.append(C[i][0])

for i in range(len(stack)):
    print(stack.pop())