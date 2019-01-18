class Solution:
	# @param A : string
	# @return an integer
	def power(self, A):
	    A = int(A)
	    A1 = A-1
	    if A in [0,1]:
	        return 0
	    else:
	        return 1 if not A & A1 else 0