y1, x1, y2, x2 = map(int, input().split())
# (x1,y1) = 왼쪽 위 지점, (x2,y2) = 오른쪽 아래 지점
dx, dy = x2-x1+1, y2-y1+1

arr = [[0]*dx for _ in range(dy)]

nx ,ny = 0, 0
cnt = 1
adv = 1
checker = True # True = 같은 adv로 한번 더 전진 가능, False = 불가능 (adv+1)

empty = dx*dy
if x1 <= 0 <= x2 and y1 <= 0 <= y2:
    arr[ny-y1][nx-x1] = 1
    empty -= 1

    
while True:
    if empty == 0:
        break
  
    for i in range(adv):
            if adv % 2 != 0: # 홀수개 전진이라면
                if checker == True:
                    nx += 1
                    cnt += 1
                else:
                    ny -= 1
                    cnt += 1
            else: # 짝수개 전진이라면
                if checker == True:
                    nx -= 1
                    cnt += 1    
                else:
                    ny += 1
                    cnt += 1
            
            if x1 <= nx <= x2 and y1 <= ny <= y2:
                arr[ny-y1][nx-x1] = cnt
                empty -= 1
    if checker == True:
        checker = False
    else:
        adv += 1
        checker = True

max_len = 1             
for i in range(dy):
    for j in range(dx):
        max_len = max(len(str(arr[i][j])), max_len)
        
for i in range(dy):
    for j in range(dx):
        t = str(arr[i][j])
        sp = max_len - len(t)
        if j == dx-1:
            print(" "*sp + t)
        else:
            print(" "*sp + t, end =" ")
        
           