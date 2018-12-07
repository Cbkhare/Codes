class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        self.count = B
        self.kth = None
        def rec(node):
            if node.left:
                rec(node.left)
            self.count-=1
            if self.count==0:
                self.kth = node.val
                return
            if node.right:
                rec(node.right)
            return
        rec(A)
        return self.kth 