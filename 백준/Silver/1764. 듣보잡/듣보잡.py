N,M = map(int,input().split())
NH = list(input() for _ in range(N))
NS = list(input() for _ in range(M))

ans = list(set(NH)&set(NS))
ans.sort()

print(len(ans))
for i in range(len(ans)):
        print(ans[i])