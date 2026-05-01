from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Idea: We want 2 pointers, AHEAD and BEHIND, such that when AHEAD gets
        # to the end, BEHIND will be at the nth node from the end, to achieve
        # this, we move AHEAD n positions ahead of BEHIND before then moving
        # them in parallel (maintain a distance of n positions between them),
        # actually, we want BEHIND to be in a position to skip over the nth node
        # from the end, so we move AHEAD n + 1 positions ahead of BEHIND
        # Cleaner implementation using a dummy node
        dummy = ListNode(next=head)
        ahead = behind = dummy
        i = 0
        while i < n + 1:
            ahead = ahead.next
            i += 1

        while ahead:
            behind, ahead = behind.next, ahead.next

        behind.next = behind.next.next

        return dummy.next
        # Time: O(l), Space: O(1), where l is the length of the linked list
