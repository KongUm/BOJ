n = int(input())

mx = 65
my = 35
arr = [[0] * mx for _ in range(my)]

sy = 0; sx = 0
for i in range(31):
    if (n & (1 << i)) != 0 :
        for j in range(sy, my):
            arr[j][sx] = 1

    arr[sy][sx] = 1
    arr[sy + 1][sx] = 1
    arr[sy][sx + 1] = 1
    arr[sy + 1][sx + 1] = 1
    arr[sy + 1][sx + 2] = 1
    sy += 1; sx += 2

for i in range(mx):
    arr[my - 1][i] = 1

print(my, mx)
for i in range(my):
    for j in range(mx):
        print(1 - arr[i][j], end = "")
    print()