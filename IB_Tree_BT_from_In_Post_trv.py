class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def bt(self, A, B,ai,aj,bi,bj): 
        if bj-1 in self.b or (aj-1<ai or bi>bj-1): return None
        #print (ai,aj,bi,bj)
            
        self.b[bj-1] = True
        if aj-1==ai or bi==bj-1:
            return TreeNode(B[bj-1])   #only single elemenet left
        root = TreeNode(B[bj-1])
        ior = self.a[B[bj-1]]
        #print(ior)
        root.left = self.bt(A, B, ai, ior, bi, bi+ior-ai)
        root.right = self.bt(A, B, ior+1, aj, bi+ior-ai,bj-1)
        return root 
        
    def buildTree(self, A, B):
        if 0 in [len(A),len(B)] or len(A) != len(B): return None
        self.a = {A[i]: i for i in range(len(A))}
        self.b={}
        return self.bt(A,B, 0,len(A), 0, len(B))
