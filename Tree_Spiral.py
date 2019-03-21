class Solution:
    def spiraLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return [] 
        l = [] 
        stack = [root]
        right =  True 
        while len(stack)!=0: 
            # fill stack
            temp_stack = [] 
            p_stack = [] 
            if right:
                stack = stack[::-1]
            for i in range(len(stack)):
                p_stack.append(stack[i].val)
                child = []
                if stack[i].left:
                    child.append(stack[i].left)
                if stack[i].right:
                    child.append(stack[i].right)
                temp_stack.extend(child)
            l.append(p_stack)
            stack = temp_stack
            right = not right 
        return l
