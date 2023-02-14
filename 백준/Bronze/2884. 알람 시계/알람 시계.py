h,m = input().split()
h,m = int(h), int(m)

if(m >= 45):
    print("%d %d" %(h, m-45))
elif(h == 0):
    print("%d %d" %(23, 60+m-45))
else:
    print("%d %d" %(h-1, 60+m-45))
    