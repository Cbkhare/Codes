class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        if len(A)==1:   return 0
        while A[0] == 0:
            A = A[1:]
        stack = []
        i = 0
        l = len(A)
        quantity = 0
        while i<l:
            if stack == []:
                stack.append(A[i])
            else:
                if A[i] < stack[0]:
                    stack.append(A[i])
                else:
                    while stack != []:
                        quantity += stack[0]-stack[-1]
                        stack.pop(-1)
                    stack.append(A[i])
            i+=1
        #print (stack)
        if stack != []:   # for case like 4 3 2 1 or 4 3 2 3
            quantity += self.trap(stack[::-1])
        return quantity