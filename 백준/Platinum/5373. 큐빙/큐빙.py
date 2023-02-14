T = int(input())

num = [[0, 3, 6], [2, 5, 8]]
move_num = [[2, 5, 8, 1, 4, 7, 0, 3, 6], [6, 3, 0, 7, 4, 1, 8, 5, 2]]
rotate_num = [[0, 3, 6, 7, 8, 5, 2, 1], [0, 1, 2, 5, 8, 7, 6, 3]]
UD_num = [2,3,4,5]
FB_num = [0,1,4,5]
LR_num = [0,1,2,3]

# cube[0] = LR, cube[1] = UD, cube[2] = FB

def Move(pg, cn, ci):  # pg = progress, cn = cube number
    for i in num[ci]:
        temp = cube[cn][pg[0]][i]
        cube[cn][pg[0]][i] = cube[cn][pg[1]][i]
        cube[cn][pg[1]][i] = cube[cn][pg[2]][i]
        cube[cn][pg[2]][i] = cube[cn][pg[3]][i]
        cube[cn][pg[3]][i] = temp
    return


def Rotate(color, cw):  # cn = cube number, color = 면의 색깔, cw = 정방향 -> 0, 역방향 -> 1
    for i in range(3):
        for _ in range(2):
            temp = cube[i][color][rotate_num[cw][0]]
            for j in range(7):
                cube[i][color][rotate_num[cw][j]] = cube[i][color][rotate_num[cw][j + 1]]
            cube[i][color][rotate_num[cw][7]] = temp
    return

def UD_copy():
    for j in range(9):
        cube[0][2][move_num[1][j]] = cube[1][2][j] # 빨강
        cube[0][3][move_num[0][j]] = cube[1][3][j] # 오렌지
        cube[2][4][move_num[1][j]] = cube[1][4][j] # 초록
        cube[2][5][move_num[0][j]] = cube[1][5][j] # 파랑
    return
def FB_copy():
    for j in range(9):
        cube[0][0][move_num[0][j]] = cube[2][0][j] #하얀색
        cube[0][1][move_num[1][j]] = cube[2][1][j] #노란색
        cube[1][4][move_num[0][j]] = cube[2][4][j] #초록색
        cube[1][5][move_num[1][j]] = cube[2][5][j] #파란색
    return

def LR_copy():
    for j in range(9):
        cube[1][2][move_num[0][j]] = cube[0][2][j] # 빨간색
        cube[1][3][move_num[1][j]] = cube[0][3][j] # 오렌지색
        cube[2][0][move_num[1][j]] = cube[0][0][j] # 하양색
        cube[2][1][move_num[0][j]] = cube[0][1][j]  # 하양색
    return


def U(cw):  # 흰색면을 보고 회전
    if cw == '+':
        Move([4, 2, 5, 3], 1, 1)
        UD_copy()
        Rotate(0,0)

    else:
        Move([4, 3, 5, 2], 1, 1)
        UD_copy()
        Rotate(0,1)

def D(cw):  # 노란색면을 보고 회전
    if cw == '+':
        Move([4, 3, 5, 2], 1, 0)
        UD_copy()
        Rotate(1,0)
    else:
        Move([4, 2, 5, 3], 1, 0)
        UD_copy()
        Rotate(1,1)

def F(cw):  # 빨간색면을 보고 회전
    if cw == '+':
        Move([4, 1, 5, 0], 2, 1)
        FB_copy()
        Rotate(2, 0)
    else:
        Move([4, 0, 5, 1], 2, 1)
        FB_copy()
        Rotate(2, 1)

def B(cw):  # 오렌지색면을 보고 회전
    if cw == '+':
        Move([5, 1, 4, 0], 2, 0)
        FB_copy()
        Rotate(3, 0)
    else:
        Move([5, 0, 4, 1], 2, 0)
        FB_copy()
        Rotate(3, 1)

def L(cw):  # 초록색면을 보고 회전
    if cw == '+':
        Move([1, 2, 0, 3], 0, 0)
        LR_copy()
        Rotate(4,0)
    else:
        Move([1, 3, 0, 2], 0, 0)
        LR_copy()
        Rotate(4, 1)


def R(cw):  # 파랑색면을 보고 회전
    if cw == '+':
        Move([2, 1, 3, 0], 0, 1)
        LR_copy()
        Rotate(5, 0)
    else:
        Move([2, 0, 3, 1], 0, 1)
        LR_copy()
        Rotate(5, 1)


for _ in range(T):
    n = int(input())
    cube = [[['w'] * 9, ['y'] * 9, ['r'] * 9, ['o'] * 9, ['g'] * 9, ['b'] * 9],
            [['w'] * 9, ['y'] * 9, ['r'] * 9, ['o'] * 9, ['g'] * 9, ['b'] * 9],
            [['w'] * 9, ['y'] * 9, ['r'] * 9, ['o'] * 9, ['g'] * 9, ['b'] * 9]]
    # cube[0] = LR, cube[1] = UD, cube[2] = FB

    # 흰색 = 0, 노랑 = 1, 빨강 = 2, 오렌지 = 3, 초록 = 4,파랑 = 5
    command = list(input().split())
    for c in command:

        if c[0] == "U":
            U(c[1])
        elif c[0] == "D":
            D(c[1])

        elif c[0] == "F":
            F(c[1])
        elif c[0] == "B":
            B(c[1])
        elif c[0] == "L":
            L(c[1])
        elif c[0] == "R":
            R(c[1])
    for i in range(9):
        if (i+1) % 3 == 0:
            print(cube[0][0][i])
        else:
            print(cube[0][0][i], end = "")


