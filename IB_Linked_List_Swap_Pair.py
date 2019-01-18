class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        swap = False
        old = None
        told =  None
        head = None
        while A:
            nxt = A.next
            if swap:
                if told:    told.next = A
                A.next = old
                old.next = nxt
                if not head:
                    head = A
                swap = False
                told = old
            else:
                old = A
                swap = True
            A = nxt
        return head 