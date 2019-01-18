class Solution:
    def count_left(self, node):
        lf = 0
        while node:
            lf += 1
            node = node.left
        return lf

    def count_right(self, node):
        rt = 0
        while node:
            rt += 1
            node = node.right
        return rt

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lf = self.count_left(root)
        rt = self.count_right(root)
        if lf == rt:
            return pow(2, lf) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1