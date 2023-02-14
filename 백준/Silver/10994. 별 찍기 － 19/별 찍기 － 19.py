N = int(input())
a = (N-1)*4+1
arr = [[' ']*a for _ in range(a)]

def square(n):
    if n == N+1:
        return
    elif n == 1:
        arr[a//2][a//2] = '*'
        return square(n+1)
    else:
        b = (n-1)*4+1
        for i in range(b):
            arr[a//2-b//2][a//2-b//2+i] = '*'
        for i in range(b):
            arr[a//2+b//2][a//2-b//2+i] = '*'
        for i in range(b):
            arr[a//2-b//2+i][a//2-b//2] = '*'
        for i in range(b):
            arr[a//2-b//2+i][a//2+b//2] = '*'
        return square(n+1)
square(1)

for i in range(a):
    ans = "".join(arr[i]).rstrip()
    print(ans)  