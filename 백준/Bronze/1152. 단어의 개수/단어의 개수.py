a = input().strip()
aa = a.replace(" ", "")

if a == "" or a == " ":
    print(0)
else: print(len(a)-len(aa)+1)
