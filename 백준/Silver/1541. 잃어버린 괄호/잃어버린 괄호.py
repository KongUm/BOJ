S = input()
minus_checker = False

num = []
op = []
a = ""
for i in S:
    a = a + i
    if i == '+' or i == '-':
        op.append(i)
        num.append(int(a[:len(a)-1]))
        a = ""
num.append(int(a))

ans = num[0]
for i in range(len(op)):
    if op[i] == '-':
        minus_checker = True
    if minus_checker == True:
        ans = ans-num[i+1]
    else:
        ans = ans+num[i+1]
print(ans)
