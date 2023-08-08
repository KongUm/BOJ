n = int(input())
A = list(map(int, input().split()))

MAX = 100005
arr = []
dp = [0] * MAX 
path = [-1] * MAX
visited = [0] * MAX
for i in range(n):
    arr.append((A[i], i))
arr.sort(reverse=True) # 오름차순 

assert(sum(A) > 0)

for i in range(n):

    if arr[i][0] == 0:
        continue

    for j in range(MAX - 1, 0, -1):
        
        if j - arr[i][0] >= 0 and (j == arr[i][0] or dp[j - arr[i][0]] != 0) and dp[j] == 0:   
            dp[j] = arr[i][0]
            path[j] = i
                

s = sum(A) // 2 + 1
v = []
for i in range(s, MAX):
    if i - dp[i] >= 0 and i - dp[i] < s:
        maxi, mini = i, dp[i]

while maxi > 0: 
    v.append(arr[path[maxi]][1])
    maxi -= arr[path[maxi]][0]

v.sort()
print(len(v))
for i in v:
    print(i + 1, end = " ")
            
    