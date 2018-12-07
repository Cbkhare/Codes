
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A==None or A.next==None: return A
        old = A
        cur = A.next
        while cur != None:
            temp = cur.next
            if old.val==cur.val:
                # break the reference
                old.next = temp
                cur = temp
            else:
                old=cur
                cur = cur.next
        return A