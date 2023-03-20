T = int(input())

def sol(n, x, y):
    for i in range(n):
        matrix[y][i] += 1
        matrix[i][x] += 1
    matrix[y][x] -= 1
    

for _ in range(T):
    n = int(input())
    arr = [list(map(str, input().split())) for _ in range(n)]
    matrix = [[0] * n for _ in range(n)]
    res = 0
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 'V':
                sol(n, x, y)
    
    for y in range(n):
        for x in range(n):
            res += (matrix[y][x] % 2)
    print(res)