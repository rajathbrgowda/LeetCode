# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if self.head == None:
            return 0
        itr = self.head
        pos =[]
        while itr:
            if itr.next == None:
                return None
            for i in pos:
                if itr == i:
                    return True
                else:
                    pos.append(itr)
            itr = itr.next
        return False
    
            