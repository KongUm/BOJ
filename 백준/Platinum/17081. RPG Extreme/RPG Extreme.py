N, M = map(int, input().split()) # N = 세로, M = 가로

arr = [['#']*(M+2)]
# arr = 그리드 (그리드 밖은 벽으로 감싸져 있음) (그리드 안쪽은 1,1부터 시작)
start_location = [] # Y좌표, X좌표
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
Monster = [] #[Y, X, Name, 공격력, 방어력, 현재 체력, 경험치, 최대 체력]
Item_Box = [] #[Y, X, T, T에 대한 부과설명]
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
Hero = [20,20,2,2,1,0] #[체력, 최대체력, 공격력, 방어력, 현재 레벨, 현재 경험치]
Weapon = 0
Armor = 0
Accessory = []
location = start_location[:]
RE = False
Die = False
Boss = True

def Item_Checker(iy,ix): # 아이템 상자 Open
    global Weapon
    global Armor
    arr[iy][ix] = '.' # 상자 소멸
    box_index = 999999999999
    for i in range(box_cnt):
        if Item_Box[i][0] == iy and Item_Box[i][1] == ix:
            box_index = i
            break

    Item_info_main = Item_Box[box_index][2]
    Item_info_sub = Item_Box[box_index][3]
    #print("Accessory box", Item_info_main,Item_info_sub)
    if Item_info_main == 'W': #무기라면
        Weapon = int(Item_info_sub)
    elif Item_info_main == 'A': #방어구라면
        Armor = int(Item_info_sub)
    else:
        if len(Accessory) < 4 and Item_info_sub not in Accessory:
            Accessory.append(Item_info_sub)
            
            
def EXP(mi):
    Monster_EXP = Monster[mi][6]
    if 'EX' in Accessory:
        Monster_EXP = int(Monster_EXP*1.2)
    temp_EXP = Hero[5] + Monster_EXP
  
    if temp_EXP >= Hero[4]*5: # 레벨업 조건 만족
        Hero[5] = 0 #경험치 초기화
        Hero[4] += 1 #레벨업
        Hero[2] += 2 #공격력 + 2
        Hero[3] += 2 #방어력 + 2
        Hero[1] += 5 #최대체력 + 5
        Hero[0] = Hero[1] # 체력 전부 회복
    else:
        Hero[5] = temp_EXP
        
     

       
            
def Common_Monster(by,bx):
    Result = Battle(by,bx) # Result[0] = True : 승리 , False: 패배 / Result[0] = mi
    if Result[0] == True: #승리
        EXP(Result[1])
        if 'HR' in Accessory:
            if Hero[0] + 3 > Hero[1]:
                Hero[0] = Hero[1]
            else:
                Hero[0] += 3
            
    else: #패배
        Death(Monster[Result[1]][2])
 
def Boss_Monster(by,bx):
    global Boss
    if 'HU' in Accessory:
        Hero[0] = Hero[1]    
        #print(Hero)
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
    mi = 99999999999 # Monster_ Index
    for i in range(monster_cnt):
        if Monster[i][0] == by and Monster[i][1] == bx:
            mi = i
            break
  
    Hero_Turn = True
    First_Turn = True
    while Hero[0] > 0 and Monster[mi][5] > 0:
        if Hero_Turn == True: # 주인공 턴이라면
            Attack = Hero[2] + Weapon # 공격력 스텟 + 무기 스텟
            if First_Turn == True: # 첫번째 공격이라면
                if 'CO' in Accessory: # CO 악세사리가 있다면
                    Attack = Attack*2
                   
                    if 'DX' in Accessory: # DX 악세사리도 있다면
                        Attack = (Attack//2)*3
                      
            Monster[mi][5] -= max(1,Attack - Monster[mi][4]) #몬스터 공격
            Hero_Turn = False #공수 교대
        else:
           if First_Turn == True:
               if arr[by][bx] != 'M' or 'HU' not in Accessory:
                   Hero[0] -= max(1, Monster[mi][3]-(Hero[3]+Armor))
                   #print("M")
                   First_Turn = False
               
           else:
               Hero[0] -= max(1, Monster[mi][3]-(Hero[3]+Armor)) #주인공 공격           
           First_Turn = False
           Hero_Turn = True #공수교대 
        #print(Hero[0],Monster[mi][5])
    
    # 어느 한쪽이 사망
    if Hero[0] <= 0:
        Monster[mi][5] = Monster[mi][7]
        return [False, mi]
        
    elif Monster[mi][5] <= 0:
        arr[by][bx] = '.' #몬스터 소멸
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
    
       
 
def Game_Over(Reason): #죽어서 게임 오버
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
        Accessory.remove('RE') #주인공이 사망했을 때 장신구 소멸
        Hero[0] =  Hero[1] # 체력을 최대체력까지 회복
        location = start_location[:] # 첫 시작위치로 돌려보냄
        #print('RE',start_location)
        #TODO : 몬스터에게 죽었을때 목스터 체력회복 구현 필요
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

    if info == "#": # 이동할려는 블록이 벽일때
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
    #print(Hero[0])
    

    # 모든 행동이 끝났다면
    if RE == False: #정상적으로 마무리 됬다면
        location = temp_location[:]
        if Boss == False:
            Win()
    else:
        RE = False

arr[location[0]][location[1]] = '@'
stat_print()
print("Press any key to continue.")



