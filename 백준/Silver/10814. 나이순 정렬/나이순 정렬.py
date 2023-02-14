N = int(input())
A = list([] for _ in range(N))
B = []
for i in range(N):
        age,name = input().split()
        A[i].append(int(age))
        A[i].append(i)
        B.append(name)
        
A.sort()
for i in range(N):
        print(A[i][0],B[A[i][1]])