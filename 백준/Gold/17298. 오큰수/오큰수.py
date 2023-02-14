N = int(input())
stack = list(map(int,input().split()))
major_stack = []
ans = []
last_num = 0

for i in range(N): #수열의 각 원소 지정
        target = stack[-1] #스택의 맨위에 있는 원소를 타겟으로 설정
        checker = True
        
        if i == 0: #가장 오른쪽 원소일때
                ans.append(-1)
                major_stack.append(-1)
                
        else:
                if last_ta > target: #바로 인접한 오른쪽 원소가 자기보다 클때
                        ans.append(last_ta)
                        major_stack.append(last_ta)
                        
                elif major_stack[-1] > target: #major스택의 윗부분이 자기보다 클때
                        ans.append(major_stack[-1])
                        
                else: #major스택에서 탐색해야할때
                        checker = False
                        while True:
                                if major_stack[-1] > target:
                                        checker = True
                                        break
                                if len(major_stack) == 1:
                                        break
                                major_stack.pop()
                                
                        if checker == True: #major스택에 타겟보다 큰수가 존재할때
                                ans.append(major_stack[-1])
                        else:
                                ans.append(-1)      
        last_ta = stack.pop()
        
for i in range(N-1,-1,-1):
        print(ans[i],end = " ")