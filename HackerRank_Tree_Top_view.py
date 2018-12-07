class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

class Solution:
    def __init__(self):
        self.data_left = {}
        self.data_right = {}

    def set_data_left(self, count, node):
        if not node:
            return

        self.data_left[count] = self.data_left.get(count, []) + [node.info]

        # Left first and then Right
        if node.left:
            self.set_data_left(count - 1, node.left)
        if node.right:
            self.set_data_left(count + 1, node.right)

    def set_data_right(self, count, node):
        if not node:
            return

        self.data_right[count] = self.data_right.get(count, []) + [node.info]

        # Right first and then Left
        if node.right:
            self.set_data_right(count + 1, node.right)
        if node.left:
            self.set_data_right(count - 1, node.left)

    def print_top_view(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        root_val = root.info
        self.set_data_left(-1, root.left)
        self.set_data_right(1, root.right)
        print (self.data_left)
        print (self.data_right)
        from sys import maxsize  as m
        mnl = mnr = m
        mxl = mxr = -m
        if self.data_left:
            mnl = min(self.data_left)
        if self.data_right:
            mnr = min(self.data_right)

        if self.data_left:
            mxl = max(self.data_left)
        if self.data_right:
            mxr = max(self.data_right)
        mn = min(0, mnl, mnr)
        mx = max(0, mxl, mxr)
        #mn = min(min(self.data_left), min(self.data_right))
        #mx = max(max(self.data_left), max(self.data_right))
        ans = []
        for i in range(mn, mx+1):
            if i == 0:
                ans.append(root_val)
            if i <0:
                if i in self.data_left:
                    ans.append(self.data_left[i][0])
                else:
                    ans.append(self.data_right[i][0])
            if i > 0:
                if i in self.data_right:
                    ans.append(self.data_right[i][0])
                else:
                    ans.append(self.data_left[i][0])
            
        print (*ans)
        #print (self.data)

def topView(root):
    S = Solution()
    S.print_top_view(root)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)