from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Approach 1
        # O(n) space
        # curr = head
        # s = set()

        # while curr:
        #     if curr in s:
        #         return True
        #     else:
        #         s.add(curr)

        # return False

        # Approach 2
        # Floyd's cycle finding algorithm, O(1) space
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False
