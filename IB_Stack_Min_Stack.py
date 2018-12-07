from sys import maxsize as m


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = m

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        self.min = min(self.min, x)

    # @return nothing
    def pop(self):
        if self.stack != []:
            p = self.stack.pop(-1)
            if p == self.min:
                if self.stack != []:
                    self.min = min(self.stack)
                else:
                    self.min = m
        else:
            return -1

    # @return an integer
    def top(self):
        if self.stack != []:
            return self.stack[-1]
        else:
            return -1


            # @return an integer

    def getMin(self):
        if self.min == m:
            return -1
        else:
            return self.min

    def __del__(self):
        del self.stack
