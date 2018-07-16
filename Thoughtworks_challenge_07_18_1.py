from sys import stdin as si

def toggle(string,a=None,b=None,c=None):
    xchar = string[b]
    char = '0' if xchar=='1' else '1'
    if a!=None and string[a] == xchar:
        string[a]=char
    if b!=None:
        string[b] = char
    if c!=None and string[c] == xchar:
        string[c] = char


if __name__ == "__main__":
    for i in range(int(si.readline().strip())):
        x = int(si.readline().strip())
        b = list(bin(x)[2:])
        l = len(b)
        for j in range(len(b)):
            if j==0:
                if l>1:
                    toggle(b=j,c=j+1,string=b)
                else:
                    toggle(b=j, string=b)
            elif j==l-1:
                toggle(a=j-1,b=j, string=b)
            else:
                toggle(a=j-1, b=j,c=j+1, string=b)
        n = int(''.join(b),2)
        print(l,n)
        F = 'X'
        L = 'Y' if l%2==0 else 'X'
        if n==x or abs(n-x)==1:
            print(L) #print last person
        else:
            print ('X' if L=='Y' else 'Y') #print opposite of last person

