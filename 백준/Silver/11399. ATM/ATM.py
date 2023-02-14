N = int(input())

P = list(map(int, input().split()))
P.sort()
sum = 0
ans = 0

for i in P:
    sum = (sum + i)
    ans += sum
    
print(ans)
    