a = input()
ans = 0

for i in a:
    if ord(i) >= 65 and ord(i) <= 67:
        ans = ans + 3
    if ord(i) >= 68 and ord(i) <= 70:
        ans = ans + 4
    if ord(i) >= 71 and ord(i) <= 73:
        ans = ans + 5
    if ord(i) >= 74 and ord(i) <= 76:
        ans = ans + 6
    if ord(i) >= 77 and ord(i) <= 79:
        ans = ans + 7
    if ord(i) >= 80 and ord(i) <= 83:
        ans = ans + 8
    if ord(i) >= 84 and ord(i) <= 86:
        ans = ans + 9
    if ord(i) >= 87 and ord(i) <= 90:
        ans = ans + 10
        
print(ans)
    
 
    