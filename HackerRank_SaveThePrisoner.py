def saveThePrisoner(n, m, s):
    x = ((m % n) + s - 1) % n
    if x == 0:
        return n
    else:
        return x

'''
https://www.hackerrank.com/challenges/save-the-prisoner/problem

'''