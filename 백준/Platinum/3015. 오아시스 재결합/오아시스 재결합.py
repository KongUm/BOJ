# 문제 뭐같네 진짜 ㅅㅂ
import sys
import bisect
N = int(input())

stack = [int(input())]

count = 0

def lower_bound(target, left, right):
    while left < right:
        mid = (left+right)//2
        if stack[mid] > target:
            left = mid+1
        else:
            right = mid
    return left
        

for i in range(1,N):
    target = int(sys.stdin.readline())
    
    while True:
        
        
        if len(stack) == 0: # target이 가장 커서 stack에 아무것도 남지 않았을 때
            stack.append(target) 
          
            break
       
        a = stack.pop()
        count += 1
       
        if target < a:
         
            stack.append(a)
            stack.append(target)            
            break
            
        elif target == a:
            stack.append(a) 
            stack.append(target)
            
            same = lower_bound(target, 0, len(stack))
            
            if same > 0:
                count += len(stack)-same-1
           
            else:count += len(stack)-same-2
            break
     
        
            
    
        
           
print(count)
            
        
