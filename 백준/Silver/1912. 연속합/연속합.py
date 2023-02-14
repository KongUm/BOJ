n = int(input())
arr = list(map(int,input().split()))
memo = [0]*(n+1)
maxi = max(arr)
mini = 0

for i in range(1,n+1):
    memo[i] = memo[i-1] + arr[i-1]
    if memo[i] < mini:
        mini = memo[i]
    elif memo[i] - mini > maxi:
        maxi = memo[i] - mini
print(maxi)