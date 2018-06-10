class Solution:
    def __init__(self):
        self.max = -100000000

    def maxPathSum(self, root):
        if root is None:    return 0
        self.toing(root)
        return self.max

    def toing(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        l = self.toing(root.left)
        r = self.toing(root.right)

        n = l+r+root.val            # on-node
        t = max(l,r) + root.val     # with child
        self.max = max(self.max, n, t, root.val)
        return max(t, root.val)
