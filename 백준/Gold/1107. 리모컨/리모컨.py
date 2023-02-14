N = int(input())
M = int(input())
arr = []
if M > 0:
    broken_button = list(map(str,input().split()))

for i in range(0,1000001):
    checker = False
    s_100 = abs(100 - N)
    if M > 0:
        checker = True
        for j in str(i):
            if j in broken_button:
                checker = False
                break
    else:
        checker = True
    if checker == True:
        s_numberpad = abs(i - N) + len(str(i))
        if s_100 > s_numberpad:
            arr.append(s_numberpad)
        else:
            arr.append(s_100)
    else:
        arr.append(s_100)
print(min(arr))