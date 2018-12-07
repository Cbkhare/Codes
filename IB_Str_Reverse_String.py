class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        A = A.split()[::-1]
        return ' '.join(A)
