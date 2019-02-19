class Solution:
    # @param A : list of list of integers
    # @return an integer
    def find1(self, A,i,j):
        if i<0 or i>=self.l or j>=self.b: return 0
        if (i,j) in self.d: return self.d[(i,j)]
        if j==self.b-2 or j==self.b-1:   #last or second last element 
            m = A[i][j]
        else: 
            m = A[i][j] + max(max(self.find(A,i,j+2),
                               self.find(A,i+1,j+2),
                               self.find(A,i-1,j+2)), 
                            max(self.find(A,i  ,j+3),
                                self.find(A,i+1,j+3),
                                self.find(A,i-1,j+3))
                            )
        self.d[(i,j)] = m
        return self.d[(i,j)]

    def adjacent1(self, A):
        if len(A[0])==0: return 0
        if len(A[0])==1: return max(A[0][0], A[1][0])
        self.l = 2 
        self.b = len(A[0])
        self.d = {}
        
        return max(self.find(A,0,0),
                   self.find(A,0,1),
                   self.find(A,1,0),
                   self.find(A,1,1))

    def find2(self, A,i):
        if i>=self.l: return 0
        if i in self.d: return self.d[i]
        if i==self.l-1 or i == self.l-2:
            m = A[i]
        else:
            m = A[i] + max(self.find(A,i+2), self.find(A,i+3))
        self.d[i] = m
        return self.d[i]
        
    def adjacent2(self, A):
        if len(A[0])==0: return 0
        if len(A[0])==1: return max(A[0][0], A[1][0])
        A = [max(A[0][i],A[1][i]) for i in range(len(A[0]))]
        #print (A)
        self.l = len(A)
        self.d={}
        return max(self.find(A,0),
                   self.find(A,1))


        
    def adjacent(self, A):
        if len(A[0])==0: return 0
        if len(A[0])==1: return max(A[0][0], A[1][0])
        A = [max(A[0][i],A[1][i]) for i in range(len(A[0]))]
        
        for i in range(len(A)):
            t1 = i-2
            t2 = i-3 
            if t1<0: t1=0
            else: t1 = A[t1]
            if t2<0: t2=0
            else: t2 = A[t2]
            A[i] = A[i] + max(t1,t2)
        return max(A[-1],A[-2])

        
