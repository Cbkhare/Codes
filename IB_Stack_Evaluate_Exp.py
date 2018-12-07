class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
		stack = []
		for t in A:
			if t in ['+','-','*','/']:
				n1, n2 = int(stack.pop()), int(stack.pop())
				if t=='+':
					n = n1+n2
				elif t=='-':
					n = n2-n1
				elif t=='*':
					n = n2*n1
				else:
					n= n2//n1
				stack.append(n)
			else:
				stack.append(t)
		return stack[-1]