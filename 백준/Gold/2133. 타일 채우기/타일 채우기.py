N=int(input())
if(N%2!=0):
    print(0);exit()
dp=[0]*31
dp[0]=1
dp[1]=3
p=4
for i in range(2,31):
    dp[i]=dp[i-1]+p*2
    p+=dp[i] 
print(dp[N//2])
    