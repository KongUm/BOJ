N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

checker = False
same = False
if A == B:
        same = True

for i in range(N-1,0,-1): #맨앞의 원소를 제외하고 맨뒤의 원소부터 하나씩 기준원소로 잡는다
        max_index = i
        for j in range(i-1,-1,-1): #기준원소를 바로 전 원소부터 모든 원소를 탐색
                if A[j] > A[max_index]:
                        max_index = j
        if A[i] < A[max_index]:
                A[i],A[max_index] = A[max_index],A[i]
                if A == B:
                        checker = True
                        break
if same == True:
        print(1)
elif checker == True:
        print(1)
else:
        print(0)