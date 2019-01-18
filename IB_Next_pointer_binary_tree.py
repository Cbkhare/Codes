class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        curr = root
        while curr:
            temp = curr
            while temp and temp.left:
                temp.left.next = temp.right
                nxt = temp.next
                if nxt and nxt.left:
                    temp.right.next = nxt.left
                temp = nxt
            curr = curr.left
