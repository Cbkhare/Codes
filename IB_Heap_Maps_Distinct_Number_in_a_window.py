class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if B>len(A):
            return []
        result = []
        map = {}
        distinct = 0
        for j in range(0,len(A)):
            #print (j,j-B,map)
            if A[j] in map and map[A[j]]>0:
                map[A[j]]+=1
            else:
                map[A[j]]=1
                distinct +=1
            if j==B-1:
                result.append(distinct)
            if j>=B:
                popped = A[j-B]
                map[popped] -=1
                if map[popped]==0:
                    distinct-=1
                else:
                    pass
                    #distinct wont change
                result.append(distinct)
        return result
