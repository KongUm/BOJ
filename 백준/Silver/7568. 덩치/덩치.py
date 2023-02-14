N = int(input())
w = []
h = []
ans = []
for i in range(N):
    a, b = map(int , input().split())
    w.append(a)
    h.append(b)

for i in range(N):
    an = 1
    for j in range(N):
        if w[j] > w[i] and h[j] > h[i]:
            an = an + 1
    ans.append(an)

for i in range(N):
    print(ans[i], end=' ')