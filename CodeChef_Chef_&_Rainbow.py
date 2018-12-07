from sys import stdin as si

class Solution:
    def __init__(self):
        self.test_num_list = []

    def validate_nums(self):
        sum_num = sum(set(map(int, self.test_num_list)))
        return sum_num == 28

    def validate_structure(self):
        return self.test_num_list == self.test_num_list[::-1]

    def validate_rainbow(self):
        if self.validate_nums() and self.validate_structure():
            return 'yes'
        else:
            return 'no'

    def get_intput(self):
        _ = int(si.readline().strip())
        self.test_num_list = si.readline().strip().split()

if __name__=="__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        S.get_intput()
        print(S.validate_rainbow())

'''
https://www.codechef.com/problems/RAINBOWA
'''