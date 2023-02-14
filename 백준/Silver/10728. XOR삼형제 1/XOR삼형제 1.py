import sys
from itertools import combinations

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [i for i in range(1, N+1)]
    maxi = 0
    ans = []
    for i in range(1, N+1):
        for j in combinations(arr, i):
            checker = True
            for k in combinations(j, 3):
                if k[0] ^ k[1] ^ k[2] == 0:
                    checker = False
                    break
            if checker == True and i > maxi:
                maxi = i
                ans = j
    print(maxi)
    for i in ans:
        print(i, end=" ")
    print()

