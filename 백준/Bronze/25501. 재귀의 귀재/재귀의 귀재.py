count = 0
def recursion(s, l, r):
    global count
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else:
        count = count + 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count = 1
    return recursion(s, 0, len(s)-1)

T = int(input())

for i in range(T):
    S = input()
    print(isPalindrome(S),count)
    