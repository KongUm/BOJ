a = input()
a = a.replace("dz=", "a").replace("lj", "a").replace("nj", "a").replace("=", "").replace("-", "")
print(len(a))