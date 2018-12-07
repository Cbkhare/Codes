class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        '''
        Add A.val and B.val and store it in A and return A list. Make sure you
        update B in A if it exists.
        Alternatively check the length of A and B and update the one with larger
        lenght
        '''
        if not A or not B:
            return A if A else B
        carry = 0
        head = A
        oldA = None
        while A and B:
            A.val = A.val + B.val
            A.val, carry = self.logic(A.val, carry)
            oldA = A  # Needed for B
            A = A.next
            B = B.next
        last = None  # Needed for carry
        if A:
            while A:
                A.val, carry = self.logic(A.val, carry)
                last = A
                A = A.next

        elif B:
            B_head = B
            while B:
                B.val, carry = self.logic(B.val, carry)
                last = B
                B = B.next
            oldA.next = B_head
        if carry:
            if last:
                last.next = ListNode(carry)
            else:
                oldA.next = ListNode(carry)
        return head

    def logic(self, val, carry):
        val += carry
        if val >= 10:
            carry = val // 10
            val %= 10
        else:
            carry = 0
        return val, carry

    def logic_length(self, C, D):
        carry = 0
        head = C
        while C and D:
            C.val = C.val + D.val
            C.val, carry = self.logic(C.val, carry)
            C = C.next
            D = D.next
        last = None
        if C:
            while C:
                C.val, carry = self.logic(C.val, carry)
                last = C
                C = C.next
        if carry:
            last.next = ListNode(carry)
        return head

    def addTwoNumbers_length(self, A, B):
        '''
        Add A.val and B.val and store it in A and return A list. Make sure you
        update B in A if it exists.
        Alternatively check the length of A and B and update the one with larger
        lenght
        '''
        if not A or not B:
            return A if A else B
        la = lb = 0
        tempA = A
        tempB = B
        while tempA:
            la+=1
            tempA=tempA.next
        while tempB:
            la+=1
            tempB=tempB.next

        if la>=lb:
            return self.logic_length(A,B)
        else:
            return self.logic_length(B,A)