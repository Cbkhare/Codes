# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def length(self, head):
        l = 1
        if head == None:  return 0
        while head.next != None:
            l += 1
            head = head.next
        return l

    def reverse(self, head):
        old = None
        current = head
        while current != None:
            temp = current
            temp_n = current.next
            current.next = old
            old = temp
            current = temp_n
        return old

    def lPalin(self, A):
        l = self.length(A)
        if l <= 1: return 1
        if l % 2 == 0:
            m = l // 2
        else:
            m = l // 2 + 1
        i = 1
        current = A
        while i < m:
            current = current.next
            i += 1
        # reached mid
        reverse_head = self.reverse(current.next)

        original = A
        reverse = reverse_head
        i = 0
        while i <= m and reverse != None:
            if original.val != reverse.val:
                return 0
            else:
                original = original.next
                reverse = reverse.next
            i += 1
        return 1

'''
Time O(n)
Auxiliary space:- O(1)
'''