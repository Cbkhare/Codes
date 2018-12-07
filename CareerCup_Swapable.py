from sys import stdin as si


def enume(strig):
    d = {}
    for k, v in enumerate(strig):
        if k % 2 == 0:
            k = 'e'
        else:
            k = 'o'
        d[v] = k
    return sorted(d.items())


if __name__ == "__main__":
    for i in range(int(si.readline())):
        w1, w2 = si.readline().strip().split(",")
        print(len(w1) == len(w2) and enume(w1) == enume(w2))


"""
Given two string check if they can be made equivalent by performing some operations on one or both string.

swapEven: swap a character at an even - numbered index with a character at another even-numbered index

swapOdd: swap a character at an odd - numbered index with a character at
another odd-numbered index

Given: s = "cdab", x = "abcd"
s -> cdab ->swap
a and c ->adcb(swapEven)-> swap
b and d(swapOdd) -> s = "abcd" = x = "abcd"

Given: s = "dcba", x = "abcd"
no amount of operation will move character from an odd index to even index,
so the two string will never be equals

Given: s = "abcd", x = "abcdcd", x length to big so will never be equals

"""
