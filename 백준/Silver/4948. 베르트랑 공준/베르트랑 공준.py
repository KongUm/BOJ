def prime(N): #N까지 소수 판별
    checker_list = [True]*(N+1) #2~N까지의 수를 소수라고 가정
    checker_list[0] = False
    checker_list[1] = False
    prime_cnt = N-1 #2~N까지의 수의 개수
    m = N//2 

    for i in range(2,m+1):
        if checker_list[i] == True:
            for j in range(i*2,N+1,i):
                if checker_list[j] == True:    
                    checker_list[j] = False
                    prime_cnt = prime_cnt - 1
    return prime_cnt

while True:
    n = int(input())
    if n == 0:
        break
    print(prime(2*n)-prime(n))