# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def find_mid(self, node_head):
        if not node_head: return node_head
        mid = node_head
        l = 0
        while node_head:
            l += 1
            if l % 2 == 0:
                mid = mid.next
            node_head = node_head.next
        if l % 2 == 0:
            return mid  # 2 in 1 2 3 4
        else:

            return mid.next  # 3 in 1 2 3 4 5

    def reverse_from_mid(self, A):
        old = None
        node = A
        while node:
            t = node
            nxt = node.next  # IMP Note
            node.next = old
            node = nxt
            old = t
        return old

    def redefine(self, A, reverse_head):
        old = None
        head = A
        while reverse_head:
            # print (reverse_head.val)
            # subtract and reverse
            A.val = reverse_head.val - A.val
            t = reverse_head
            nxt = reverse_head.next  # IMP
            reverse_head.next = old
            old = t
            reverse_head = nxt
            A = A.next
        # A.next = o
        return head

    def subtract(self, A):
        if not A or not A.next: return A
        begin_from = self.find_mid(A)
        # print (begin_from.val, begin_from.next)
        reverse_head = self.reverse_from_mid(begin_from)
        A = self.redefine(A, reverse_head)
        return A


'''
https://www.interviewbit.com/problems/subtract/

1) find mid
2) reverse linked list from 
    1->2->3->4->5 becomes 1->2->3->4<-5 and 4-> None
3) Start from Head and reverse_head 1 and 5. Keep on reversing the reverse_head

time complexity O(n), Space Complexity O(1)

Note: line no. 30 and 44'''