N = int(input())
arr = list(map(int,input().split()))
dp = [1]*N
LIS = []
# dp[i] = 0 ~ j 범위내에 있는 LIS의 길이의 최댓값 (DP Table)

for i in range(N):
    LIS.append([])
    for j in range(0,i+1):
        if arr[j] < arr[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                #LIS[i].append(arr[j])
                
           
        #elif i == j:
            #LIS[i].append(arr[i])
            
maxi  = max(dp)
print(maxi)
ans = []

for i in range(N-1,-1,-1):
    if maxi == dp[i]:
        ans.append(arr[i])
        maxi = maxi -1
for _ in range(max(dp)):
    print(ans.pop(), end = " ")
        
        
    