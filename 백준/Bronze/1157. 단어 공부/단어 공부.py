a = input().upper()
max = 0
mx = ""
b = "".join(set(a))

for i in range(len(b)):
    aa = a.replace(b[i], "") 
    cur = len(a) - len(aa)
    if cur > max:
        max = cur
        mx = b[i]
    elif cur == max:
        mx = "?"
        
print(mx)