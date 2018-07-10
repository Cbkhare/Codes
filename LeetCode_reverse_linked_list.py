# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # When head is given
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        old = None
        temp = head
        while temp != None:
            t_next = temp.next
            temp.next = old
            old = temp
            temp = t_next
        return old

    # Using self.head
    def reverseList_withself(self):
        # Code here
        if self.head is None:
            return None
        reve = None

        while self.head:
            t_next = self.head.next
            self.head.next = reve
            reve = self.head
            if t_next == None:   break
            self.head = t_next

'''
Input: [1,2,3,4,5]
Output: [5,4,3,2,1]

'''