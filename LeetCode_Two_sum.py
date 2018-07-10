class Solution:
    def __init__(self):
        self.m = {}
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root==None:  return False
        l=r=False
        if root.left:
            l = self.findTarget(root.left, k)
        if root.right:
            r = self.findTarget(root.right, k)
        d = k-root.val
        if d in self.m:
            return True
        else:
            self.m[root.val]=1
            return l or r

    def findTarget_nonRecursive(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root:
            queue, cache = [root], set()
            for node in queue:

                if node.val in cache: return True
                cache.add(k - node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)

        return False

'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''