import sys
M = int(input())

S = set()

for i in range(M):
    A = sys.stdin.readline().split()
    
    if A[0] == "add":
        S.add(int(A[1]))
    elif A[0] == "remove":
        if int(A[1]) in S:
            S.remove(int(A[1]))
    elif A[0] == "check":
        if int(A[1]) in S:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif A[0] == "toggle":
        if int(A[1]) in S:
            S.remove(int(A[1]))
        else:
            S.add(int(A[1]))
    elif A[0] == "all":
        S = set(p for p in range(1,21))
    else:
        S = set()
        