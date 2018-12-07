# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        B = 1 if B == 0 else B
        # maintain a counter to have the note of nth value
        count = 0
        ignore = False
        head = A
        delhe = None
        while A.next:
            if not ignore:
                count += 1
            if count == B:
                delhe = delhe.next if delhe else head
                ignore = True
            A = A.next
        # if l < B: return head
        if delhe:
            to_be_del = delhe.next
            forward = delhe.next.next
            delhe.next = forward
        else:
            head = head.next  # when value to be del is first
        return head

    def removeNthFromEnd_diff(self, A, B):
        B = max(1, B)  # to handle -ve and zero
        l = 0
        head = A
        node = None
        old = None
        ignore = False
        count = 1
        # maintain the counter to have n-1th index
        while A:
            if not ignore:
                l += 1
            if l == B and not ignore:
                ignore = True
                A = A.next
                count = 0
                continue
            if count == 0:
                node = node.next if node else head
            A = A.next

        if head == node or node == None:  # only when node is head
            head = head.next
        else:
            node.next = node.next.next
        return head


