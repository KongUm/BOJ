N, M = map(int, input().split()) 

arr = [['#']*(M+2)]
start_location = [] 
monster_cnt = 1
box_cnt = 0
for i in range(N):
    s = input()
    temp = ['#']
    for j in range(M):
        temp.append(s[j])
        if s[j] == '@':
            start_location = [i+1,j+1]
        elif s[j] == 'B':
            box_cnt += 1
        elif s[j] == '&':
            monster_cnt += 1
    temp.append('#')
    arr.append(temp)
arr.append(['#']*(M+2))
arr[start_location[0]][start_location[1]] = '.'

command = input()
Monster = [] 
Item_Box = [] 
for _ in range(monster_cnt):
    a = input().split()
    for i in range(7):
        if i != 2:
            a[i] = int(a[i])
    Monster.append(a)
    Monster[_].append(a[-2])

for _ in range(box_cnt):
    a = input().split()
    for i in range(2):
            a[i] = int(a[i])
    Item_Box.append(a)

Turn_count = 0
Hero = [20,20,2,2,1,0] 
Weapon = 0
Armor = 0
Accessory = []
location = start_location[:]
RE = False
Die = False
Boss = True

def Item_Checker(iy,ix): 
    global Weapon
    global Armor
    arr[iy][ix] = '.'
    box_index = 999999999999
    for i in range(box_cnt):
        if Item_Box[i][0] == iy and Item_Box[i][1] == ix:
            box_index = i
            break

    Item_info_main = Item_Box[box_index][2]
    Item_info_sub = Item_Box[box_index][3]
    if Item_info_main == 'W': 
        Weapon = int(Item_info_sub)
    elif Item_info_main == 'A': 
        Armor = int(Item_info_sub)
    else:
        if len(Accessory) < 4 and Item_info_sub not in Accessory:
            Accessory.append(Item_info_sub)
            
def EXP(mi):
    Monster_EXP = Monster[mi][6]
    if 'EX' in Accessory:
        Monster_EXP = int(Monster_EXP*1.2)
    temp_EXP = Hero[5] + Monster_EXP
  
    if temp_EXP >= Hero[4]*5:
        Hero[5] = 0
        Hero[4] += 1
        Hero[2] += 2 
        Hero[3] += 2 
        Hero[1] += 5
        Hero[0] = Hero[1] 
    else:
        Hero[5] = temp_EXP
        
def Common_Monster(by,bx):
    Result = Battle(by,bx) 
    if Result[0] == True: 
        EXP(Result[1])
        if 'HR' in Accessory:
            if Hero[0] + 3 > Hero[1]:
                Hero[0] = Hero[1]
            else:
                Hero[0] += 3
            
    else: 
        Death(Monster[Result[1]][2])
 
def Boss_Monster(by,bx):
    global Boss
    if 'HU' in Accessory:
        Hero[0] = Hero[1]    
    Result = Battle(by,bx)
    if Result[0] == True:
        EXP(Result[1])
        if 'HR' in Accessory:
            if Hero[0] + 3 > Hero[1]:
                Hero[0] = Hero[1]
            else:
                Hero[0] += 3
        Boss = False
    else:      
        Death(Monster[Result[1]][2])
    
def Battle(by,bx):
    mi = 99999999999 
    for i in range(monster_cnt):
        if Monster[i][0] == by and Monster[i][1] == bx:
            mi = i
            break
  
    Hero_Turn = True
    First_Turn = True
    while Hero[0] > 0 and Monster[mi][5] > 0:
        if Hero_Turn == True: 
            Attack = Hero[2] + Weapon 
            if First_Turn == True:
                if 'CO' in Accessory: 
                    Attack = Attack*2
                   
                    if 'DX' in Accessory: 
                        Attack = (Attack//2)*3
                      
            Monster[mi][5] -= max(1,Attack - Monster[mi][4]) #몬스터 공격
            Hero_Turn = False
        else:
           if First_Turn == True:
               if arr[by][bx] != 'M' or 'HU' not in Accessory:
                   Hero[0] -= max(1, Monster[mi][3]-(Hero[3]+Armor))
                 
                   First_Turn = False
               
           else:
               Hero[0] -= max(1, Monster[mi][3]-(Hero[3]+Armor)) #주인공 공격           
           First_Turn = False
           Hero_Turn = True 
        
    if Hero[0] <= 0:
        Monster[mi][5] = Monster[mi][7]
        return [False, mi]
        
    elif Monster[mi][5] <= 0:
        arr[by][bx] = '.'
        return [True, mi]
        
def stat_print():
    for i in arr[1:N+1]:
        print("".join(i[1:M+1]))
    print("Passed Turns :", Turn_count)
    print("LV :", Hero[4])
    print("HP :", str(Hero[0])+"/"+str(Hero[1]))
    print("ATT :", str(Hero[2])+"+"+str(Weapon))    
    print("DEF :", str(Hero[3])+"+"+str(Armor))
    print("EXP :", str(Hero[5])+"/"+str(Hero[4]*5))
    
def Game_Over(Reason):
    Hero[0] = 0
    stat_print()
    print("YOU HAVE BEEN KILLED BY "+Reason+ "..")
    exit(0)
       
def Win():
    arr[location[0]][location[1]] = '@'
    stat_print()
    print("YOU WIN!")
    exit()
    
def Death(Reason):
    global RE
    global location
    if 'RE' in Accessory:
        RE = True
        Accessory.remove('RE')
        Hero[0] =  Hero[1]
        location = start_location[:]
    else:
        Game_Over(Reason)
   
def Spike_Trap(ty,tx):
    if 'DX' in Accessory:
        Hero[0] -= 1
    else:
        Hero[0] -= 5
    if Hero[0] <= 0:
        Death('SPIKE TRAP')

for com in command:
    Turn_count += 1
    temp_location = location[:]
    if com == 'L':
        temp_location[1] -= 1
    elif com == 'R':
        temp_location[1] += 1
    elif com == 'U':
        temp_location[0] -= 1
    else:
        temp_location[0] += 1
    y,x, = temp_location[0], temp_location[1]
    info = arr[y][x]

    if info == "#": 
        if arr[location[0]][location[1]] == '^':
            Spike_Trap(location[0], location[1]) 
        continue
    elif info == 'B':
        Item_Checker(y,x)
    elif info == '^':
        Spike_Trap(y,x)
    elif info == '&':
        Common_Monster(y,x)
    elif info == 'M':
        Boss_Monster(y,x)
        
    if RE == False:
        location = temp_location[:]
        if Boss == False:
            Win()
    else:
        RE = False

arr[location[0]][location[1]] = '@'
stat_print()
print("Press any key to continue.")