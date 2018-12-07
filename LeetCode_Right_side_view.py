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

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.set_data(0, root)
        ans = []
        if not self.data: return ans
        #Modify Level order Traversal
        for k in range(max(self.data)+1):
            ans.append(self.data[k][-1])

        return (ans)


    def rightSideView_new(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.lr=-1
        result = []
        def right_tree(node, depth):
            if depth>self.lr:
                result.append(node.val)
                self.lr+=1
            if node.right:
                right_tree(node.right, depth+1)
            if node.left:
                right_tree(node.left, depth+1)
        right_tree(root,0)
        return result
'''
Hint:- Modify level order Traversal 
https://leetcode.com/problems/binary-tree-right-side-view/
'''