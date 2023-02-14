W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
# W = 종이 가로, H = 종이 세로, f = 크게 한번 접는선, c = 여러번 접는 선의 개수
# (x1, y1) = 칠하는 직사각형 부분의 왼쪽 위, (x2, y2) = 오른쪽 아래

painted = 0
if f > W//2:
    f = W-f
if f <= x1: # 전부 1번만 접혔을때
    painted = (x2-x1)*(y2-y1)*(c+1)
elif f >= x2:
    painted = (x2-x1)*(y2-y1)*(c+1)*2
else:
    painted = (f-x1)*(y2-y1)*(c+1)*2+(x2-f)*(y2-y1)*(c+1)

print(W*H-painted)