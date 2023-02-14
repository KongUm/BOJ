N = int(input())
command = [[] for _ in range(N)]
stat = [[0,-1] for _ in range(8)] # 대문자 = 0 ~ 3 / 소문자 = 4 ~ 7
# stat[i][0] = 윷길 번호 , stat[i][1] = 위치

for i in range(N):
    a = list(map(str, input().split()))
    char = a[0]
    if ord(char) < 69:
        command[i].append(ord(char)-65)
    else:
        command[i].append(ord(char)-93)
    front, back = 0, 0
    for j in range(4):
        if a[1][j] == "F":
            front += 1
        else:
            back += 1
    if back == 4:  #모 일경우
        command[i].append(5)
    else:
        command[i].append(front)

#print(command)

p = [[],[[] for _ in range(12)],[[] for _ in range(17)],[[] for _ in range(17)],[[] for _ in range(21)]]


def Move(pn, before, after):
    temp_arr = p[pn][before][:] + p[pn][after][:]
    if Check(temp_arr): # 만약 이동 할 자리에 상대 팀 말이 없다면
        p[pn][after] = temp_arr[:]
        p[pn][before] = []
    else:
        Reset(p[pn][after])
        p[pn][after] = p[pn][before][:]
        p[pn][before] = []
    for i in p[pn][after]:
        stat[i][1] = after
        
def Check(arr):
    upper_checker = False
    lower_checker = False
    for i in arr:
        if 0 <= i <= 3: # 대문자면
            upper_checker = True
        else: # 소문자면
            lower_checker = True
    if upper_checker == True and lower_checker == True:
        # 대문자 소문자 둘다 있다면
        return False
    else:
        return True
            
def Reset(arr):
    for i in arr:
        stat[i] = [0,-1] 
               
    

def Path_1(target, num):
    before = stat[target][1] # 이동 전 위치
    after = before + num  # 이동 할 위치
    if after > 11:  # 판 밖으로 넘어 갈때
        p[1][before] = [] 
    else:
        Move(1, before, after)
        
def Path_2(target, num):
    before = stat[target][1] 
    after = before + num 
    if after > 16: 
        p[2][before] = []
    else:
        Move(2, before, after)
            
def Path_3(target, num):
    before = stat[target][1] 
    after = before + num 
    if after > 16: 
        p[3][before] = []
    elif after == 8:
        for i in p[3][before]:
            stat[i] = [1,stat[i][1]]
        p[1][before] = p[3][before][:]
        Path_1(target, num)
    else:
        Move(3, before, after)
        
def Path_4(target, num):
    before = stat[target][1]
    after = before + num 
    
    if after > 20: #판을 넘었을때
        p[4][before] = []
        
    elif after == 5:
        for i in p[4][before]:
            stat[i] = [3,stat[i][1]]
        p[3][before] = p[4][before][:]
        Path_3(target,num)
        
    elif after == 10:
        for i in p[4][before]:
            stat[i] = [2,stat[i][1]]
        p[2][before] = p[4][before][:]
        Path_2(target,num)
    else:
        Move(4, before, after)
    

for i in range(N):
    target, num = command[i][0], command[i][1] 
    #target = 말의 번호 / num = 필요한 이동 수
    
    if stat[target][0] == 0: # 윷판에 들어오지 않았을때
        stat[target] = [4,0]
        p[4][0].append(target)
        
    if stat[target][0] == 1: 
        Path_1(target, num)
      
    elif stat[target][0] == 2: 
        Path_2(target, num)
        
    elif stat[target][0] == 3:
        Path_3(target, num)
        
    elif stat[target][0] == 4:
        Path_4(target, num)

arr = []
a = []
a.append("..----..----..----..----..----..")
a.append("..    ..    ..    ..    ..    ..")
a.append("| \                          / |")
a.append("|  \                        /  |")
a.append("|   \                      /   |")
a.append("|    ..                  ..    |")
a.append("..   ..                  ..   ..")
a.append("..     \                /     ..")
a.append("|       \              /       |")
a.append("|        \            /        |")
a.append("|         ..        ..         |")
a.append("|         ..        ..         |")
a.append("..          \      /          ..")
a.append("..           \    /           ..")
a.append("|             \  /             |")
a.append("|              ..              |")
a.append("|              ..              |")
a.append("|             /  \             |")
a.append("..           /    \           ..")
a.append("..          /      \          ..")
a.append("|         ..        ..         |")
a.append("|         ..        ..         |")
a.append("|        /            \        |")
a.append("|       /              \       |")
a.append("..     /                \     ..")
a.append("..   ..                  ..   ..")
a.append("|    ..                  ..    |")
a.append("|   /                      \   |")
a.append("|  /                        \  |")
a.append("| /                          \ |")
a.append("..    ..    ..    ..    ..    ..")
a.append("..----..----..----..----..----..")

alphabet = ['A','B','C','D','a','b','c','d']
edge = [[30,30],[30,24],[30,18],[30,12],[30,6],[30,0],[24,0],[18,0],[12,0],[6,0],[0,0],[0,6],[0,12],[0,18],[0,24],[0,30],[6,30],[12,30],[18,30],[24,30],[30,30]]

dig1 = [[0,0],[5,5],[10,10],[15,15],[20,20],[25,25],[30,30]]
dig2 = [[15,15],[20,20],[25,25],[30,30]]
dig3 = [[30,0],[25,5],[20,10],[15,15],[10,20],[5,25],[0,30],[6,30],[12,30],[18,30],[24,30],[30,30]]

for y in range(32):
    arr.append([])
    for x in range(32):
        arr[y].append(a[y][x])

    
for i in range(8):
    u = stat[i]
    n = u[1]
    x = 0
    y = 0
    if u[0] == 0:
        continue
    elif u[0] == 4:
        x = edge[n][0]
        y = edge[n][1]
    elif u[0] == 2:
        x = dig1[n-10][0]
        y = dig1[n-10][1]
    elif u[0] == 1:
        x = dig2[n-8][0] #안되면 8
        y = dig2[n-8][1]
    elif u[0] == 3:
        x = dig3[n-5][0]
        y = dig3[n-5][1]
        
    if i%4 == 1:
        x += 1
    elif i%4 == 2:
        y += 1
    elif i%4 == 3:
        y += 1
        x += 1
    arr[y][x] = alphabet[i]
        
for i in range(32):
    print("".join(arr[i]))
    
    
    
