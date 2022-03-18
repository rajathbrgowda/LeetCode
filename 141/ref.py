# Two pointers Solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast: return True
        return False

# Dictionary Solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        D={}
        while head:
            if head in D: return True
            D[head]=True
            head=head.next
        return False

#Set Solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        S=set()
        while head:
            if head in S: return True
            S.add(head)
            head=head.next
        return False