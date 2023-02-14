A = [list(map(int, input().split())) for _ in range(2)]
B = [list(map(int, input().split())) for _ in range(1)]
arr = [[0]*2001 for _ in range(2001)]

for x1, y1, x2, y2 in A:
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i + 1000][j + 1000] = 1
for x1, y1, x2, y2 in B:
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i + 1000][j + 1000] = 0

ans = 0
for i in arr:
    ans += sum(i)
print(ans)