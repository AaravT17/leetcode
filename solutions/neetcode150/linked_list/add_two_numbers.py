from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            val = a + b + carry
            curr.next = ListNode(val=val % 10)
            carry = val // 10
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry == 1:
            curr.next = ListNode(val=1)

        return dummy.next
        # Time: O(max(m, n)), Space: O(1), where m = len(l1), n = len(l2)
