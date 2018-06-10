class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:    return True
        return self.chck_mirror(root.left, root.right)

    def chck_mirror(self, ln, rn):  # ln->left_node, rn->right_node
        
        if ln == None or rn == None:    return bool(ln == rn)  # ln==rn==None
        if ln.val != rn.val:    return False
        return self.chck_mirror(ln.left, rn.right) & self.chck_mirror(ln.right,
                                                                      rn.left)