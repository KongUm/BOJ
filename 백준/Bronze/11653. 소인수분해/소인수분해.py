N = int(input())

a = 2
if N != 1:
    while N != 1:
        if N % a == 0:
            N = N//a
            print(a)
        else:
            a = a + 1