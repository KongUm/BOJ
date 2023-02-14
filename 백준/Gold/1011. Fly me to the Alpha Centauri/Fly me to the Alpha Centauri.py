import sys

T = int(input())
data = [sys.stdin.readline().strip().split() for i in range(T)]

for i in range(T):
    y = int((data[i])[1])-int((data[i])[0])

    k = 1
    bonus = 0
    while y > k*2:
        y = y - k*2
        k = k+1

    if y > k:
        y = y-k
        bonus = bonus+1

    if y > 0:
        bonus = bonus+1

    print((k-1)*2+bonus)