class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        from heapq import heapify as hp, heappush as hpu, heappop as hpo
        x= []
        hp(x)
        for ll in A:
            while ll:
                hpu(x,ll.val)
                ll=ll.next
        head = None
        cur = None
        while x:
            if not head:
                head = ListNode(hpo(x))
                cur = head
            else:
                cur.next = ListNode(hpo(x))
                cur = cur.next
        return head