N = int(input())
arr = list(map(int,input().split()))
a_list = list([] for _ in range(40001))
a_ans = []
all_same = True

def Fa(front,back,b,n):
        if n < 1:
                return
        if front == 0:
                if front+b == back: #사실상 back == b
                        return 999999999
                else:
                        return
        
        a = (back - b)/front
        if int(a) == a:
                return int(a)
        else:
                return

if N > 1:
        for b in range(-19999,20000):
                for n in range(1,N):
                        a = Fa(arr[n-1],arr[n],b,n)
                        if a != None:
                                if b < 0:
                                        a_list[b*(-1)].append(a)
                                        
                                else:
                                        a_list[b+20000].append(a)
                                   
        for i in range(40001):
                if len(a_list[i]) == N-1:
                        for j in range(N-1):
                                if a_list[i][j] == 999999999:
                                        a_list[i][j] = min(a_list[i])
                        
                        checker = True
                        for j in range(N-2):
                                if a_list[i][j] != a_list[i][j+1]:
                                        checker = False
                        if checker == True:
                                a_ans.append(a_list[i][0])
        for i in range(1,N):
                if arr[i-1] != arr[i]:
                        all_same = False
                        
                                
#print(all_same,"all")        
#print(a_ans)
if N == 1:
        print("A")        
elif arr[0] != arr[1] and len(a_ans) > 1:
        print("A")
elif all_same == True:
        print(arr[0])
elif N == 2:
        print("A")
elif len(a_ans) == 0:
        print("B")
else:        
        B = arr[1] - arr[0]*a_ans[0]
        print(arr[-1]*a_ans[0] + B)