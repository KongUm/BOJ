N = int(input())
A = []
same = []
for i in range(N):
        word  = input()
        A.append(word)
        
A.sort()

for key in range(1,N):
        for i in range(key,0,-1):
                if len(A[i-1]) > len(A[i]):
                        A[i-1],A[i] = A[i],A[i-1]
               
before = ""
for i in range(N):
        if A[i] != before:
                print(A[i])
                before = A[i]