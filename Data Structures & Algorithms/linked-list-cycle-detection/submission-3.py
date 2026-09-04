# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #empty list or single node list
        if not head or not head.next:
            return False
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next #move 1 step
            fast = fast.next.next #move 2 steps
            if slow == fast:
                return True
        #fast pointer reached end, no cycle
        return False
        