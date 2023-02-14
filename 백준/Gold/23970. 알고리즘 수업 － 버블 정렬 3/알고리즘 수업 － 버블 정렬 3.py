N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

same = False

if A == B:
       same = True
        
        
checker = False

for i in range(len(A)): #리스트 원소 선택 (0번부터 ~)
        for j in range(len(A)-i-1): #이미 정렬된 원소 예외 처리
                if A[j] > A[j+1]:
                        temp = A[j]
                        A[j] = A[j+1]
                        A[j+1] = temp
                        if A[0] == B[0] and A[j] == B[j]: #스왑이 끝날때 마다 A와 B의 맨 앞과 뒤를 비교
                                checker = True #일단 일치한다고 가정
                                for p in range(1,len(A)-1):
                                        if B[p] != A[p]:
                                                checker = False #틀린부분이 하나라도 있다면 False로 바꾸고 포문 탈출
                                                break
                                if checker == True:
                                        break     
        if checker == True:
                break                                
        if B[len(A)-1-i] != A[len(A)-1-i] and i>0:
                break
                
                
if same == True:
        print(1)    
elif checker == True:
        print(1)
else:
        print(0)