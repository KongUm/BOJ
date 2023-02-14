# 주사위의 모서리에서는 모서리에서 보일 수 있는 두 면의 숫자의 합의 최솟값을 더해준다
# 모서리와 꼭짓점을 제외한 나머지 부분은 영향을 받지 않으므로 면 중에 가장 작은 숫자를 더해준다
# 주사위의 꼭짓점에서 보일 수 있는 세면의 숫자의 합의 최솟값을 더해준다
# 단, 바닥과 붙어있는 꼭짓점은 두 면만 보이므로 모서리와 같게 취급한다

N = int(input())
num = list(map(int, input().split()))
two = 10000
three = 10000
for i in range(6):
    for j in range(6):
        if j != 5-i and i != j:
            two = min(num[i]+num[j], two)

a = [[0,1,2],[0,1,3],[0,2,4],[0,3,4],[5,1,3],[5,1,2],[5,3,4],[5,2,4]]
for p,q,r in a:
    three = min(num[p]+num[q]+num[r], three)

ans = 0
ans += min(num)*(N-2)**2*5+min(num)*(N-2)*4 # 중심부분
ans += three*4
ans += two*(N-2)*8 + two*4
if N == 1:
    print(sum(num)-max(num))
else:
    print(ans)
        