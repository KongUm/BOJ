N = int(input())

arr = list(map(int,input().split()))

dp = [[1]*2 for _ in range(N)]

# dp[i] = i 가 기준일때 바이토닉 수열의 길이의 최댓값 (DP Table)

for std in range(N): #기준 0 ~ std 감소, std ~ N -1 증가

    lf_cnt = 0

    rg_cnt = 0

    for i in range(0,std+1):

        if arr[i] < arr[std]:

            if dp[i][0]+1 > dp[std][0]:

                dp[std][0] = dp[i][0]+1

           

for std in range(N-1,-1,-1):          

    for i in range(std,N):

        if arr[i] < arr[std]:

            if dp[i][1]+1 > dp[std][1]:

                dp[std][1] = dp[i][1]+1

                                         

                

                

    

            

sum_dp = []

for i in range(N):

    sum_dp.append(sum(dp[i])-1)

        

    

    

print(max(sum_dp))

