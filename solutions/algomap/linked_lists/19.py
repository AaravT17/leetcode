from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Approach 1
        # if not head:
        #     return None

        # count = 0
        # curr = head
        # while curr:
        #     count += 1
        #     curr = curr.next

        # if n == count:
        #     return head.next

        # i = 0
        # curr = head
        # while curr:
        #     i += 1
        #     if count - i == n:
        #         # This is the basis for Approach 2, to maintain a distance of n
        #         # positions between 2 pointers so that when one hits the end,
        #         # the other is in the correct position (n nodes from the end)
        #         curr.next = curr.next.next
        #     curr = curr.next

        # return head

        # Approach 2
        # Idea: We want 2 pointers, AHEAD and BEHIND, such that when AHEAD gets
        # to the end, BEHIND will be at the nth node from the end, to achieve
        # this, we move AHEAD n positions ahead of BEHIND before then moving
        # them in parallel (maintain a distance of n positions between them),
        # actually, we want BEHIND to be in a position to skip over the nth node
        # from the end, so we move AHEAD n + 1 positions ahead of BEHIND
        # ahead = behind = head

        # i = 0
        # while i < n + 1:
        #     if not ahead:
        #         # if we encounter this scenario, it means we are trying to
        #         # remove the first node i.e. the head of the linked list
        #         return head.next
        #     ahead = ahead.next
        #     i += 1

        # while ahead:
        #     ahead = ahead.next
        #     behind = behind.next

        # behind.next = behind.next.next

        # return head

        # Cleaner implementation using a dummy node
        dummy = ListNode(next=head)
        ahead = behind = dummy

        i = 0
        while i < n + 1:
            ahead = ahead.next
            i += 1

        while ahead:
            ahead = ahead.next
            behind = behind.next

        behind.next = behind.next.next

        return dummy.next
        # The dummy node helps handle edge cases more smoothly
