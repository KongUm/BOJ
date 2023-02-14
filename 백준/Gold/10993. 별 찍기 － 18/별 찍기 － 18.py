N = int(input())
a = [0,1]
h = [0,1]
for i in range(1,N): 
    a.append(a[i] + 2**(i+1))
    h.append(h[i]*2 + 1)
# a = 삼각형의 가로 길이, h = 삼각형의 세로 길이

#print(a,h)
arr = [[' ']*a[-1] for _ in range(h[-1])]

def piramid (n,x,y):
    #print("piramid",n,x,y)
    for i in range(h[n]):
        #print(n, i)
        if n%2 != 0:
            arr[y+i][x-i] = '*'
            arr[y+i][x+i] = '*'
            
        else:
            arr[y-i][x-i] = '*'
            arr[y-i][x+i] = '*'
            
    for i in range(a[n]):
        if n%2 != 0:
            #print("x", x-h[n]+1+i, "y", y+h[n]-1)
            arr[y+h[n]-1][x-h[n]+1+i] = '*'
   
        else:
            #print("x", x-h[n]+1+i, "y", y-h[n]+1)
            arr[y-h[n]+1][x-h[n]+1+i] = '*'
    if n > 1:
        if n%2 != 0:
            return piramid(n-1,x,y + h[n]-2)
        else:
            return piramid(n-1,x,y - h[n]+2)
    else:
        return
        
if N%2 != 0:
    piramid(N,a[N]//2,0)
else:
    #print(a[N]//2, h[N]-1)
    piramid(N,a[N]//2,h[N]-1)

for i in range(h[-1]):
    ans = "".join(arr[i]).rstrip()
    print(ans)
