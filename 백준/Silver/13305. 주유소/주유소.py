N = int(input())
dis = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_cost = cost[0]
ans = 0
for i in range(N-1):
    ans = ans + min_cost * dis[i]
    min_cost = min(min_cost, cost[i+1])
print(ans)