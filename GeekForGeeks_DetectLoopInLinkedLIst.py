def detectLoop(head):
    while head:
        if head.data=='visited':
            return 1
        else:
            head.data = 'visited'
        head=head.next
    return 0

'''
https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1
'''