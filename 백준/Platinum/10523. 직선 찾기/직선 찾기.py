import sys
import random
n=int(input())
p=int(input())
A=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
if n==1:
    print("possible")
    exit() 
for _ in range(150):
    D=random.sample(A,2)
    c=0
    x=D[1][0]-D[0][0]
    y=D[1][1]-D[0][1]
    for i in range(n):
        a=A[i][0]-D[0][0]
        b=A[i][1]-D[0][1]
        if x*b==y*a:
            c+=1
    if c>=n/100*p:
        print("possible")
        exit()
print("impossible")