A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

if B < C:
    print(A//(C-B)+1)
else: print(-1)