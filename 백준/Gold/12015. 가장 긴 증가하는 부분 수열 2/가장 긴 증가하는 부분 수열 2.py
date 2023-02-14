import bisect
N = int(input())
A = list(map(int,input().split()))

dp = [0]*N
# dp[i] = arr[i]를 가장 큰 수로 가지는 LIS의 최댓값
D = []

def lower_bound(arr, target):    
    low, high = 0, len(arr)-1 # 탐색범위 low ~ high
    
    while low <= high:

        mid = (low+high)//2    
        
        if target > arr[mid]: 
            low = mid+1
        else:
            high = mid-1
    return low
                            
for i in range(N):
    if i == 0:
        D.append(A[0])
        dp[0] = 1
    else:
        if D[-1] < A[i]:
            D.append(A[i])
            dp[i] = dp[i-1] + 1
            
        else: # D[-1] >= A[i]일때
            loc = lower_bound(D, A[i])
            #loc = bisect.bisect_left(D,A[i])
            D[loc] = A[i]
            dp[i] = dp[i-1]
print(dp[-1])
