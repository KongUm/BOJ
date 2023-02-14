T = int(input())

for _ in range(T):
    K = int(input())
    C = list(map(int, input().split()))
    dp = [[0]*(K+1) for _ in range(K+1)]
    # dp[i][j][u] = 파일 i개를 j 번째 부터 j+i-1번째 더했을 때 드는 비용의 최솟값
    sum_C = [0]
    for i in range(K):
        sum_C.append(sum_C[-1]+C[i])        
        
    for i in range(2,K+1): # 만들 파일의 개수 선택
        for j in range(1,K-i+2): # 파일의 시작 j번째 선택
            dp[i][j] = 99999999999999
            for p in range(1,i): # p개 + i-p개 중 p를 선택 (1 ~ i-1)
                dp[i][j] = min(dp[i][j], dp[p][j] + dp[i-p][j+p] + sum_C[j+i-1] - sum_C[j-1])
    #print(dp)
    print(dp[K][1])
            
            
    
    
    
