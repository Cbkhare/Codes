class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.ans = []
        self.evl = {}

    def can_be_inserted(self, lst):
        if tuple(lst) not in self.evl:
            self.evl[tuple(lst)] = True
            return True
        else:
            return False

    def calc(self, lst):
        if len(lst) == 1:
            self.evl[tuple(lst)] = True
            self.ans.append(lst)
        else:
            n = lst[0]
            self.calc(lst[1:])
            temp = self.ans[:]
            print('self.ans')
            for i in range(len(self.ans)):
                tar = [n] + self.ans[i]
                if self.can_be_inserted(tar):
                    self.ans[i] = tar
                else:
                    del self.ans[i]
            if self.can_be_inserted([n]):
                self.ans = [[n]] + self.ans + temp
            else:
                self.ans = self.ans + temp

        return

    def subsetsWithDup(self, A):
        if A == []: return [[]]
        self.calc(sorted(A))
        return [[]] + sorted(self.ans)

