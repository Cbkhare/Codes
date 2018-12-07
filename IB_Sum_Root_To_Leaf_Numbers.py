class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers_slow(self, A):
        if not A: return 0

        def find_nums(node):
            if node.left == node.right == None:
                return [str(node.val)]
            else:
                l = r = []
                if node.left:
                    l = [str(node.val) + v for v in find_nums(node.left)]
                if node.right:
                    r = [str(node.val) + v for v in find_nums(node.right)]

                return l + r

        return sum(map(int, find_nums(A))) % 1003

    def sumNumbers(self, A):
        if not A: return 0
        self.some = 0

        def find_nums(node, num_string):
            if node.left == node.right == None:
                self.some += int(num_string + str(node.val))
            else:
                if node.left:
                    find_nums(node.left, num_string + str(node.val))
                if node.right:
                    find_nums(node.right, num_string + str(node.val))
            return

        find_nums(A, '')
        return self.some % 1003