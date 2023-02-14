N = int(input())
good_sq = ""
global_checker = True
ans = ""
def dfs(a):
    global global_checker
    global good_sq
    global ans
    if a == N:
        global_checker = False
        ans = good_sq
        return 
    else:
        for n in range(1,3+1):
            if global_checker == False:
                return
            checker = True
            temp = good_sq + str(n)
            leng = len(good_sq)+1
            for i in range(1,(a+1)//2+1):
                if temp[leng-i*2:leng-i] == temp[leng-i:leng]:
                    checker = False
                    break
            if checker == False:
                continue
            good_sq = temp        
            dfs(a+1)
            good_sq = good_sq[:-1]
dfs(0)
print(ans)