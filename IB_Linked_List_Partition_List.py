# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        grtr = None
        lest = None
        head = None
        old = None
        orig = A
        while A:
            # print (A.val,grtr,lest)
            nxt = A.next
            if not grtr and A.val >= B:
                grtr = A
                old = A
            elif grtr and A.val >= B:
                old = A
            elif A.val < B:
                if not lest:
                    if not grtr:
                        lest = A
                        if not head: head = A
                        old = A
                    else:
                        A.next = grtr
                        old.next = nxt
                        lest = A
                        if not head: head = A
                elif lest:
                    if not grtr:
                        lest = A
                        old = A
                    else:
                        templ = lest.next
                        old.next = nxt  # old reamins old here
                        lest.next = A
                        A.next = templ
                        lest = A
            A = nxt
        if not head: return orig
        return head


'''
Common approach is to create 2 linked list, greater one and smaller one and join
them in the last. This takes linear time and Space

Above approach, takes linear time and Unit space. During iteration, 
- Find the least and greatest. 
- Put least in front of greatest.
- when new least is found, link old least least to new least and new least to greatest
 
- 1 5 3 2 4, B=3
- - 1 5 3 2 4, lst = 1, grtst = None
- - 1 5 3 2 4, lst = 1, grtst = 5
- - 1 5 3 2 4, lst = 1, grtst = 5
- - 1 2 5 3 4, lst = 2, grtst = 5
- - 1 2 5 3 4, lst = 2, grtst = 5 
'''