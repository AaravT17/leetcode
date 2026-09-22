# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode()
        curr = dummy
        nxt_grp = head
        while True:
            grp_head, grp_tail, nxt_grp = self._reverse_group(nxt_grp, k)
            curr.next = grp_head
            curr = grp_tail
            if not nxt_grp:
                break
 
        return dummy.next
        # Time: O(n), Space: O(1)

    def _reverse_group(self, head: ListNode, k: int) -> tuple[ListNode | None, ListNode | None, ListNode | None]:
        """
        Reverse a group and return the head and tail of the group as well as the head of the next group.
        If there are not enough elements after head to form a group of size k, do not reverse the group.
        """
        # first, check length of group, if len(group) < k, do not reverse
        prev, curr = None, head
        i = 0
        while curr and i < k:
            i += 1
            prev, curr = curr, curr.next

        if i < k:
            # len(group) < k
            return head, prev, None

        # len(group) == k, reverse group and return new head and tail + head of next group
        prev, curr = None, head
        i = 0
        while i < k:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
            i += 1
        return prev, head, curr
        