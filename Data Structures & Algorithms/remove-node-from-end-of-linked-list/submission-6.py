# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #compute total nodes
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        targetIndex = N - n
        if targetIndex == 0:
            return head.next
        #traverse and find node before target node
        curr = head
        for i in range(N - 1):
            if (i + 1) == targetIndex:
                curr.next = curr.next.next #sever target node
                break
            curr = curr.next
        return head
        