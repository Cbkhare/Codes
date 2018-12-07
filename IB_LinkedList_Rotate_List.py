class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if not A or not A.next or B==0: return A
        head = A
        old = None
        k = 0
        back  = None
        first = False
        l =0
        while A:
            l+=1
            A=A.next
        A = head
        if B>=l:
            B = B%l
        if B==0:
            return head
        while A:
            if k==B:
                if first:
                    back = head
                    first = False
                else:
                    back=back.next
            else:
                k+=1
                if k==B: first = True
            old = A
            A = A.next
        new_head = back.next
        back.next = None
        old.next = head
        return new_head
