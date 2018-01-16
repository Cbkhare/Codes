from Abstract_Data_Types import kmp_failure


def pattern_index(p, t):
    n, m = len(t), len(p)
    Kmp = kmp_failure.Kmp_failure(p)
    pattern = Kmp.compute_kmp()
    j, k = 0, 0
    while j < n:
        if p[k] == t[j]:
            if k == m-1: #match is complte
                return j - m+1
            j += 1
            k += 1
        elif k > 0:
            k = pattern[k-1]
        else:
            j+=1
    else:
        return -1


if __name__=="__main__":
    for i in range(int(input().strip())):
        p,t = input().split()
        print (pattern_index(p,t))

