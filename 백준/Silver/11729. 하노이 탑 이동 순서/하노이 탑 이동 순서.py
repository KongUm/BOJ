N = int(input())
loca = []

for i in range(N+1):
    loca.append(1)

def Hanoi(N, frm, to):
    print(frm, to)
    loca[N] = to # 함수실행 = 이동

    if N == 1:
        return

    for i in range(1,N):
        if (check(i)+check(N-1))%2 == 0:
            Hanoi(i,loca[i],to)
        else:
            Hanoi(i,loca[i],6-loca[i]-to)


def check(num):
    if num%2 == 0:
        return 1
    else: return 0


print(2**N-1)
for i in range(1,N+1):
    if (check(i)+check(N))%2 == 0: #홀홀 이던지 짝짝 이던지 하면 ok
        dest = 3
    else:
        dest = 2
    Hanoi(i, 1, dest)

