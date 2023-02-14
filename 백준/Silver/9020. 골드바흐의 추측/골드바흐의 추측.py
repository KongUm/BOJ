T = int(input())

def prime(N): #N까지 소수 판별
    checker_list = [True]*(N+1) #2~N까지의 수를 소수라고 가정
    checker_list[0] = False
    checker_list[1] = False

    for i in range(2,N//2+1): #어떤 소수의 배수는 소수*2가 최소이므로
        if checker_list[i] == True:
            for j in range(i*2,N+1,i):
                checker_list[j] = False
    return checker_list
    
checker_list = prime(10000)
    
for i in range(T):
    target = int(input())
    half = target//2
    if target%2 == 0:
        left = half
        right = half
    else:
        left = half
        right = half + 1
        
    for j in range(1,half):
        if checker_list[left] == True and checker_list[right] == True:
            print(left,right)
            break 
        left = half - j
        right = half + j