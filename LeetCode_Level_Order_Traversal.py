# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.data = {}

    def set_data(self, count, node):
        if not node:
            return
        if node.left:
            self.set_data(count + 1, node.left)
        if node.right:
            self.set_data(count + 1, node.right)

        self.data[count] = self.data.get(count, []) + [node.val]

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.set_data(0, root)
        if not self.data: return []
        ans_list = [[]] * (max(self.data) + 1)

        for k, v in self.data.items():
            ans_list[k] = v

        return (ans_list)

'''
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''