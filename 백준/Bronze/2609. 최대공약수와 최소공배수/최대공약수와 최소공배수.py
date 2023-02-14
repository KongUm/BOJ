A, B = map(int, input().split())
maxi = 1
for i in range(1,max(A,B)+1):
    if A%i == 0 and B%i == 0:
        maxi = i
print(maxi)  
print(A*B//maxi)