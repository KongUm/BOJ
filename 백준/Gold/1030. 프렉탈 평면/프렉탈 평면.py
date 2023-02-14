s, N, K, y1, y2, x1, x2 = map(int, input().split())

arr = [[0]*(x2-x1+1) for _ in range(y2-y1+1)]

def fractal(t,x,y): #t = 시간, x = 중심 x좌표, y = 중심 y좌표
    if t == 0:
        return
    else:
        
        d = N**(t-1)*K # 검은색 변의 크기      
        low_x, low_y = x-d//2, y-d//2, 
        high_x, high_y = x+d//2, y+d//2
        
        if t > 1:
            if x-N**t//2 > x2 or x+N**t//2-1< x1 or y-N**t//2 > y2 or y+N**t//2-1 < y1:
               return
        
        if low_x < x1: low_x = x1
        if low_y < y1: low_y = y1
        if high_x > x2: high_x = x2
        if high_y > y2: high_y = y2
       
        for i in range(low_y, high_y+1):
            for j in range(low_x, high_x+1):
                arr[i-y1][j-x1] = 1
                
        
               
        else:
            for i in range(-N//2,N//2+1):
                for j in range(-N//2, N//2+1):
                    
                    fractal(t-1, x+N**(t-1)*i, y+N**(t-1)*j)


def fractal_2(t,x,y): #t = 시간, x = 중심 x좌표 +1, y = 중심 y좌표 +1
   if t == 0:
       return
   else:
       
       d = N**(t-1)*K
       a = N**(t-1)//2
       low_x, low_y = x-(d//2), y-(d//2)
       high_x, high_y = x+(d//2-1), y+(d//2-1)
       
       if t > 1:
           if x-N**t//2 > x2 or x+N**t//2-1< x1 or y-N**t//2 > y2 or y+N**t//2-1 < y1:
               return
       if low_x < x1: low_x = x1
       if low_y < y1: low_y = y1
       if high_x > x2: high_x = x2
       if high_y > y2: high_y = y2
       
       for i in range(low_y, high_y+1):
            for j in range(low_x, high_x+1):
                arr[i-y1][j-x1] = 1
               
      
       else:
           for i in range(-(N//2)*2-1,(N//2)*2+1,2):
               for j in range(-(N//2)*2-1,(N//2)*2+1,2):
                
                   fractal_2(t-1, x+a*i,y+a*j)

if N%2 == 0:
    fractal_2(s,N**s//2,N**s//2)
else:
    fractal(s,N**s//2,N**s//2)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if j == len(arr[i])-1:
            print(str(arr[i][j]))
        else:
            print(str(arr[i][j]), end = "")
        
                
        
