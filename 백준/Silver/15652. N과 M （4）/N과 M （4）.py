N,M = map(int,input().split())

def BT(index, letter):
        global ans
        if index > M-1:
                print(letter)
                return
        for i in range(1,N+1):
                if index == 0:
                        BT(index+1, letter + str(i))
                else:
                        if i >= int(letter[-1]):
                                BT(index+1, letter + " " + str(i))                
BT(0,"")