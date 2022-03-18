# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Using The Tortoise and the Hare (Floyd’s Algorithm)

        slow, fast = head , head   # initaialising 2 pointer
        while fast and fast.next:  # checking current head and next if empty ; else return Flase
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
            