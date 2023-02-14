C = input() #암호

dp = [0]*len(C)
# dp[i] = index i까지 암호를 해석했을 때 가지수의 최댓값
checker = True

for i in range(len(C)):
    if i == 0:
        if int(C[0]) != 0:
            dp[0] = 1
        else:
            print(0)
            checker = False
            break
            
    elif i == 1:
        ok = False
        if int(C[1]) != 0:
            dp[1] = dp[1] + 1
            ok = True
        if 0 < int(C[0] + C[1]) <= 26:
            dp[1] = dp[1] + 1
            ok = True
            
        if ok == False:
            print(0)
            checker = False
            break
       
    else:
        ok = False
        if int(C[i]) != 0:
            dp[i] = dp[i-1]
            ok = True
        if 0 < int(C[i-1]+C[i]) <= 26 and int(C[i-1]) != 0:
            dp[i] = dp[i] + dp[i-2]
            ok = True
           
        if ok == False:
            print(0)
            checker = False
            break    
if checker == True:
    print(dp[len(C)-1]%1000000)       
            