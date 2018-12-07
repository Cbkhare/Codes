class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if A.next == None: return A
        temp = None
        current = A
        while current != None:
            temp_n = current.next
            current.next = temp
            temp = current
            current = temp_n

        return temp