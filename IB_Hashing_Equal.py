from collections import OrderedDict as od
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        m=od()
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                s = A[i]+A[j]
                if s in m:
                    if len(m[s])>2: continue
                    pi,pj=m[s]
                    if pj!=j and pi!=j and pi!=i and pj!=i:
                        if i<pi:
                            m[s] = (i,j,pi,pj)
                        elif i>pi:
                            m[s] = (pi,pj,i,j)
                else:
                    m[s]=(i,j)
        for k,v in m.items():
            if len(v)>2:
                return list(v)
        else:
            return []