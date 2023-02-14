P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))

xs = P2[0] - P1[0]
ys = P2[1] - P1[1]

x = P3[0] - P2[0]
y = P3[1] - P2[1]

if xs*y < ys*x:
    print(-1)
elif xs*y == ys*x:
    print(0)
else:
    print(1)