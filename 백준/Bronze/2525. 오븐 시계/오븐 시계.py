A, B = input().split()
A = int(A)
B = int(B)
C = int(input())

sum = A*60+B+C
if sum >= 24*60:
    sum = sum - 24*60

print(sum//60, sum%60)