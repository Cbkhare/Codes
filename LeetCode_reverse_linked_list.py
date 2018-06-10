# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
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


'''
Input: [1,2,3,4,5]
Output: [5,4,3,2,1]

'''