# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkBalance(root)[0]

    def checkBalance(self, node):
        if node == None:
            return True, 1
        else:
            lc = rc = 0
            if node.left:
                judgel, lc = self.checkBalance(node.left)
                if not judgel:  return False, 0
            if node.right:
                judger, rc = self.checkBalance(node.right)
                if not judger:
                    return False, 0
            if abs(lc - rc) > 1:   return False, 0
            return True, max(lc, rc) + 1


'''Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.
'''