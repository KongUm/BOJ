N = int(input())
A = list(map(int, input().split()))

num = []
for i in range(N):
    str_num = str(A[i])
    str_num = str_num + (12 - len(str_num))*str_num[len(str(A[i]))-1]
    num.append([int(str_num) ,A[i]])
num.sort(reverse = True)

ans = ""
ans2 = ""
for i in range(N):
    ans += str(num[i][1])
    ans2 += str(num[N-1-i][1])
    
print(max(int(ans), int(ans2)))