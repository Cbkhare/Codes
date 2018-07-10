from sys import stdin as si

d = {}
def lcs(X, Y, m, n):
    print(X[m], Y[n],m,n)
    if (m,n) in d:  return d[(m,n)]
    if m < 0 or n < 0: return  []
    if m==0 and n==0:
        out = [] if X[0] != Y[0] else [X[0]]

    elif X[m] == Y[n]:
        if m == 0 and n >= 0:
            out = lcs(X, Y, m, n - 1)
        elif m >= 0 and n == 0:
            out = lcs(X, Y, m - 1, n)
        else:
            out = lcs(X, Y, m-1, n-1)
        out.append(X[m])
    else:
        if m == 0 and n >= 0:
            out = lcs(X, Y, m, n - 1)
        elif m >= 0 and n == 0:
            out = lcs(X, Y, m - 1, n)
        else:
            out = max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n), key=lambda x: len(x))
    # print(out)
    d[(m,n)] = out
    return out

def lcs_chars(X, Y, m, n):
    print(X[m], Y[n],m,n)
    if (m,n) in d:  return d[(m,n)]
    if m < 0 or n < 0: return  ''
    if m==0 and n==0:
        out = '' if X[0] != Y[0] else X[0]

    if X[m] == Y[n]:
        if m == 0 and n >= 0:
            out = lcs_chars(X, Y, m, n - 1) + str(X[m])
        elif m >= 0 and n == 0:
            out = lcs_chars(X, Y, m - 1, n) + str(X[m])
        else:
            out = lcs_chars(X, Y, m-1, n-1) + str(X[m])
    else:
        if m == 0 and n >= 0:
            out = lcs_chars(X, Y, m, n - 1)
        elif m >= 0 and n == 0:
            out = lcs_chars(X, Y, m - 1, n)
        else:
            out = max(lcs_chars(X, Y, m, n-1),
                      lcs_chars(X, Y, m-1, n), key=lambda x: len(x))

    d[(m,n)] = out
    return out


if __name__=="__main__":

    #x = list(si.readline().strip())
    #y = list(si.readline().strip())
    x = si.readline().strip().split()
    y = si.readline().strip().split()
    print (lcs(x,y,len(x)-1,len(y)-1))
    print(len(d))

'''
Optimal substructure:- 
             abc/acb
        /       |        \
    ab/acb    ab/ac     abc/ac
    m-1/n    m-1/n-1    m/n-1

Overlapping subproblems
Check substrucutre
'''