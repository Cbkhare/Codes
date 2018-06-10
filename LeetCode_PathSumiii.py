class Solution:

    def __init__(self):
        self.count =0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.sum = sum
        self.genPathSum(root)
        return self.count

    def genPathSum(self, root):
        l = r = []
        if root == None:    return
        if root.left:
            l = self.genPathSum(root.left)
        if root.right:
            r = self.genPathSum(root.right)
        i = 0
        while True:
            if i >= len(l): break
            if l[i] + root.val == self.sum:
                self.count += 1
            l[i] = l[i] + root.val
            i += 1
        i = 0
        while True:
            if i >= len(r): break
            if r[i] + root.val == self.sum:
                self.count += 1
            r[i] = r[i] + root.val
            i += 1
        if root.val == self.sum:
            self.count += 1
        return l + r + [root.val]


'''
Solved using space O(n)
'''
