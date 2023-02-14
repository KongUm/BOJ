N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

possess = set(A)&set(B)

dict = {}

for i in list(possess):
        dict[i] = 0                             
for i in range(N):
        if A[i] in possess:
                dict[A[i]] += 1

for i in range(M):
        if B[i] in possess:
                print(dict[B[i]], end = " ")
        else:
                print("0", end = " ")                                                     
