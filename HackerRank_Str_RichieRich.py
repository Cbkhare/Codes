import sys


def richieRich(s, n, k):
    # Complete this function
    l = len(s)
    limit, i = int(len(s)/2), 0    # limit is the floor of l
    # Make s a palindrome within k > 0
    while i < limit:
        if s[i] == s[l-i-1]:
            i += 1
        else:
            s = s[:i] + '9' + s[i+1:l-i-1] + '9' + s[l-i:]
            if k <= 0:
                return -1
            else:   k -= 1
    return s


if __name__=='__main__':

    for i in range(int(input())):
        n, k = map(int, input().strip().split())
        s = input().strip()
        result = richieRich(s, n, k)
        print(result)