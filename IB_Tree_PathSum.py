class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        stack =[]
        def node(n, val,lst):
            if n.left == n.right == None:
                if val==n.val:
                    lst.append(n.val)
                    stack.append(lst)
                else:
                    pass
            else:
                #if n.val<val:
                if n.left:
                    node(n.left, val-n.val,lst+[n.val])
                if n.right:
                    node(n.right, val-n.val,lst+[n.val])
            return
        node(A,B,[])
        return stack 