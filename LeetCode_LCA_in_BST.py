class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root in (None,p,q):
            return root
        ans= None
        p,q = sorted([p,q])
        if q.val<=root.val:
            ans= self.lowestCommonAncestor(root.left, p, q)
        elif root.val<=p.val:
            ans = self.lowestCommonAncestor(root.right, p ,q)
        if ans: return ans
        else:   return root



'''
s, b = sorted([p.val, q.val])
while not s <= root.val <= b:
    # Keep searching since root is outside of [s, b].
    root = root.left if s <= root.val else root.right
# s <= root.val <= b.
return root
'''