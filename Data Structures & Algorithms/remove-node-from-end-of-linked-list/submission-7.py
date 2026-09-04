# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #use 2 pointers so that the gap between them is n
        dummy = ListNode(0, head)
        left, right = dummy, head
        #move right pointer ahead n steps
        for i in range(n):
            right = right.next
        #move both pointers
        while right:
            left = left.next
            right = right.next
        #when right reaches end, left will sit just before target

        #sever target node
        left.next = left.next.next
        return dummy.next
        