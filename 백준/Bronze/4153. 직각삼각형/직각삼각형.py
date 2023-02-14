while True:
        s = list(map(int,input().split()))
        c = max(s)
        if c == 0:
                break
        s.remove(c)
        
        if (s[0]**2)+(s[1]**2) == c**2:
                print("right")
        else:
                print("wrong")