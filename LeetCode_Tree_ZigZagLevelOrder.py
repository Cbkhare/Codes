# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return [] 
        l = [] 
        stack = [root]
        right =  False
        while len(stack)!=0: 
            # fill stack
            temp_stack = [] 
            p_stack = [] 
            for i in range(len(stack)):
                p_stack.append(stack[i].val)
                child = []
                if stack[i].left:
                    child.append(stack[i].left)
                if stack[i].right:
                    child.append(stack[i].right)
                temp_stack.extend(child)
            if right:
                l.append(p_stack[::-1])
            else: 
                l.append(p_stack)
            stack = temp_stack
            right = not right 
        return l
