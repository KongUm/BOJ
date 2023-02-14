import sys
import random

N = int(input())
E = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
if N <= 2:
    print("success")
    exit()
for _ in range(1000):
    G1 = random.sample(E, 2)
    G2 = random.sample(E, 2)
    x1 = G1[0][0] - G1[1][0]
    y1 = G1[0][1] - G1[1][1]
    x2 = G2[0][0] - G2[1][0]
    y2 = G2[0][1] - G2[1][1]
    count = 0
    for i in range(N):
        xc1 = E[i][0] - G1[0][0]
        yc1 = E[i][1] - G1[0][1]
        xc2 = E[i][0] - G2[0][0]
        yc2 = E[i][1] - G2[0][1]
        if x1*yc1 == y1*xc1 or x2*yc2 == y2*xc2:
            count += 1
    if count == N:
        print("success")
        exit()
print("failure") 