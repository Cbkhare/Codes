def solve(s):
    N = list(s);Flag = False 
    i =1
    while True: 
        if i>=len(N) or len(N)==1:   break 
        if N[i]==N[i-1]:
            del N[i]
            Flag = True
        elif Flag:    del N[i-1];i-=1;Flag=False
        else:  i +=1
    if Flag:  del (N[-1]) 
    return ''.join(N)

import sys

a = sys.argv[1]
print (solve(a))



'''
BGGY -> BY
BGGYYGGT-> BT
BGYYGGY -> BY
'''