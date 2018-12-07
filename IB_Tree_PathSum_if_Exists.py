class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A: return 0
        def validate(node, some):
            #print (node.val, some)
            if node.left == node.right == None:
                if node.val==some:
                    return True
                else:
                    return False
            else:
                if node.left:
                    r = validate(node.left,some=some-node.val)
                    if r:
                        # This is to avoid going to node.right if found true
                        return True
                if node.right:
                    r = validate(node.right, some=some-node.val)
                    if r:
                        return True
            return False
        if validate(A,B):
            return 1
        else:
            return 0
'''
https://www.interviewbit.com/problems/path-sum/
'''