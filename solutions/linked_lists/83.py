from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1
        # if not head:
        #     return None

        # prev, curr = head, head.next

        # while curr:
        #     while curr and prev.val == curr.val:
        #         curr = curr.next
        #     if not curr:
        #         prev.next = None
        #         break
        #     prev.next = curr
        #     prev, curr = curr, curr.next

        # return head

        # Approach 2
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
