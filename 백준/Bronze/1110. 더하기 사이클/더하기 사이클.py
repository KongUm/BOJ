a = int(input())
N = int(str(a%10) + str((a//10 + a%10)%10))
i = 1

while N != a:
    N = int(str(N%10) + str((N//10 + N%10)%10))
    i = i + 1

print(i)