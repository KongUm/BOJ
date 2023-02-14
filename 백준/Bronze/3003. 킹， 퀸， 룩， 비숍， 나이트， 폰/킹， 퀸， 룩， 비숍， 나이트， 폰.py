A = list(map(int,input().split()))
emp = [1,1,2,2,2,8]

for i in range(6):
    print(emp[i] - A[i],end=' ')