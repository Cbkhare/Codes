# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        # Without recursion
        s_left = [A]
        while s_left[-1].left is not None:
            s_left.append(s_left[-1].left)

        s_right = [A]
        while s_right[-1].right is not None:
            s_right.append(s_right[-1].right)

        while s_left and s_right and s_left[-1].val < s_right[-1].val:
            if s_left[-1].val + s_right[-1].val < B:
                u = s_left.pop()
                u = u.right
                if u is not None:
                    s_left.append(u)
                    while s_left[-1].left is not None:
                        s_left.append(s_left[-1].left)
            elif s_left[-1].val + s_right[-1].val > B:
                u = s_right.pop()
                u = u.left
                if u is not None:
                    s_right.append(u)
                    while s_right[-1].right is not None:
                        s_right.append(s_right[-1].right)
            else:
                return 1

        return 0

    def t2Sum_1(self, A, B):
        # with recursion
        if not A: return False
        self.st = set([])

        def check(node):
            if node.val not in self.st:
                self.st.add(B - node.val)
            else:
                return True
            l = r = False
            if node.left:
                l = check(node.left)
            if node.right:
                r = check(node.right)
            return l or r

        r = check(A)
        # print (self.st)
        return 1 if r else 0


