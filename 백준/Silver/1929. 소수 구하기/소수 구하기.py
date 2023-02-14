M,N = map(int,input().split())

def prime(N): #N까지 소수 판별
    checker_list = [True]*(N+1) #2~N까지의 수를 소수라고 가정
    checker_list[0] = False
    checker_list[1] = False
    m = N//2

    for i in range(2,m+1):
        if checker_list[i] == True:
            for j in range(i*2,N+1,i):
                checker_list[j] = False
    return checker_list

B = prime(N)

for i in range(M,N+1):
    if B[i] == True:
        print(i)