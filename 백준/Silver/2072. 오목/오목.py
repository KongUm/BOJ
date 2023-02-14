N = int(input()) # 놓는 돌의 개수

arr = [[2]*21 for _ in range(21)]

def Search_Row(x,y,color):
    cnt = 1
    i, j = 1,1
    while arr[y][x+i] == color:
        i += 1
        cnt += 1
    while arr[y][x-j] == color:
        j += 1
        cnt += 1
    if cnt == 5:
        return True
    else:
        return False
    
def Search_Column(x,y,color):
    cnt = 1
    i, j = 1,1
    while arr[y+i][x] == color:
        i += 1
        cnt += 1
    while arr[y-j][x] == color:
        j += 1
        cnt += 1
    if cnt == 5:
        return True
    else:
        return False
        
def Search_Diagonal(x,y,color):
    cnt = 1
    i, j = 1,1
    while arr[y+i][x+i] == color:
        i += 1
        cnt += 1
    while arr[y-j][x-j] == color:
        j += 1
        cnt += 1
    if cnt == 5:
        return True
    else:
        return False

def Search_Diagonal_2(x,y,color):
    cnt = 1
    i, j = 1,1
    while arr[y+i][x-i] == color:
        i += 1
        cnt += 1
    while arr[y-j][x+j] == color:
        j += 1
        cnt += 1
    if cnt == 5:
        return True
    else:
        return False
    
    
for i in range(1,N+1): 
    y, x = map(int, input().split())
    color = i % 2 # 홀수번째는 흑(1), 짝수번째는 백(0)

    arr[y][x] = color
    if Search_Row(x,y,color):
        print(i)
        exit(0)
       
    if Search_Column(x,y,color):
        print(i)
        exit(0)
       
    if Search_Diagonal(x,y,color):
        print(i)
        exit(0)
        
    if Search_Diagonal_2(x,y,color):
        print(i)
        exit(0)
        
print(-1)
    
