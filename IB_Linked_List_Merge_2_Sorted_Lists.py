class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        head = None
        cur = None
        while A and B:
            t = None
            if A.val <= B.val:
                t=A
                A = A.next
            else:
                t = B
                B = B.next
            if not head:
                head = t
                cur = head
            else:
                cur.next = t
                cur = cur.next
        if A:
            cur.next = A
        elif B: cur.next = B
        return head