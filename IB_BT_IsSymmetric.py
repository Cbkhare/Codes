class Solution:
    # @param A : root node of tree
    # @return an integer
    def check_mirror(self, n1,n2):
        if not n1 and not n2:
            return 1
        if (n1 and not n2) or (n2 and not n1) or (n1.val != n2.val):
            return 0 
        return self.check_mirror(n1.left,n2.right) and self.check_mirror(n1.right, n2.left)
    def isSymmetric(self, A):
        if not A:
            return 1
        else:
            return self.check_mirror(A.left,A.right)
