N = int(input())
a = list(map(int, input().split()))
M = max(a)
B = []

for i in range(N):
    B.append(a[i]/M*100)

print(sum(B)/N)

