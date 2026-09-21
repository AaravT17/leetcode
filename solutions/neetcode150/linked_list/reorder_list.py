# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Steps:
        #   1. Reverse the second half of the linked list
        #   2. Merge the first and second half, alternating elements from each

        # locate the start of the second half, and disconnect the first and second half
        # note: if the list has an odd number of elements, the middle element belongs to the first half
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is at the last element of the first half, second half starts at slow.next
        second = slow.next
        slow.next = None

        # reverse the second half
        prev, curr = None, second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        # head is the start of the first half, prev is the start of the second half
        # we must modify the links such that head becomes the start of the merged list
        first, second = head, prev
        dummy = ListNode()
        curr = dummy
        while second:
            first_nxt, second_nxt = first.next, second.next
            first.next = second
            second.next = first_nxt
            first, second = first_nxt, second_nxt
        # Time: O(n), Space: O(1)
